import os
import json

from qgis.core import QgsProject, QgsMapLayer, QgsMapLayerStyle, QgsRasterLayer, QgsVectorLayer
import processing

from .qgis2gl import Qgis2Gl
from .vectorTilesMaker import VectorTilesMaker

PLACEHOLDER_URL = r'http://MVT_HOSTING_URL/{z}/{x}/{y}.pbf'


class StyleManager:
    def __init__(self, project: QgsProject):
        self.project = project

    def write_mbstyle(self, output_path: str, vtsource_url: str, is_mvt_mode: bool):
        visible_layers = self._get_visible_layers()

        mblayers = []
        vector_layers = []
        raster_layers = []

        # mapbox layers making
        for layer in visible_layers:
            mblayer = {}
            qml_str = self._qml_of(layer)
            qgis2gl = Qgis2Gl(qml_str)

            if layer.type() == QgsMapLayer.VectorLayer:
                vector_layers.append(layer)
                # categorized styling or not
                categories = qgis2gl.qgs_style.get('categories')
                if categories is None:
                    # one qgis-layer one gl-layer
                    mblayer = {
                        'id': layer.id(),
                        'source': 'mvt',
                        'source-layer': layer.name(),
                        'type': qgis2gl.mbtype(),
                        'paint': qgis2gl.mbpaint()
                    }
                    mblayers.insert(0, mblayer)
                else:
                    # one qgis-layer some gl-layer
                    for i in range(len(categories)):
                        if not qgis2gl.category_is_visible(i):
                            continue
                        mblayer = {
                            'id': layer.id() + str(i),
                            'source': 'mvt',
                            'source-layer': layer.name(),
                            'type': qgis2gl.mbtype(idx=i),
                            'paint': qgis2gl.mbpaint(idx=i)
                        }
                        mblayers.insert(0, mblayer)

            elif layer.type() == QgsMapLayer.RasterLayer and layer.providerType() == 'wms':
                raster_layers.append(layer)
                mblayer = {
                    'id': layer.id(),
                    'source': layer.id(),
                    'type': 'raster',
                    'paint': qgis2gl.mbpaint()
                }
                mblayers.insert(0, mblayer)

        # mapbox sources making
        # RASTER
        mbsources = {}
        for rlayer in raster_layers:
            rsource = self._make_raster_source(rlayer)
            mbsources.update(rsource)

        # VECTOR
        if len(vector_layers) > 0:
            if vtsource_url == '':
                vtsource_url = PLACEHOLDER_URL
            vtsource = {
                'mvt': {
                    'type': 'vector',
                    'tiles': [vtsource_url]
                }
            }
            mbsources.update(vtsource)

        mbstyle = {
            'version': 8,
            'sources': mbsources,
            'layers': mblayers
        }

        with open(os.path.join(output_path, 'style.json'), 'w') as f:
            json.dump(mbstyle, f, indent=4)

        if is_mvt_mode:
            vtmaker = VectorTilesMaker(vector_layers)
            vtmaker.generateBinaryTiles(os.path.join(output_path, 'pbf'))

    def _make_raster_source(self, rlayer: QgsRasterLayer) -> dict:
        import urllib.parse
        metadata = rlayer.styleURI()
        params = metadata.split('&')
        provider_data = {}
        for param in params:
            #kv[0] = key, kv[1] = value
            kv = param.split('=')
            provider_data[kv[0]] = kv[1]
        url = provider_data['url']
        decoded_url = urllib.parse.unquote(url)
        id = rlayer.id()
        rsource = {
            id: {
                'type': 'raster',
                'tiles': [decoded_url],
                'tileSize': 256
            }
        }
        return rsource

    def _get_visible_layers(self) -> [QgsMapLayer]:
        visible_layers = []
        for treeLayer in self.project.layerTreeRoot().findLayers():
            if treeLayer.isVisible():
                visible_layers.append(treeLayer.layer())
        return visible_layers

    def _qml_of(self, layer: QgsMapLayer) -> str:
        ls = QgsMapLayerStyle()
        ls.readFromLayer(layer)
        return ls.xmlData()
