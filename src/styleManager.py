from qgis.core import QgsProject, QgsMapLayer, QgsMapLayerStyle, QgsRasterLayer, QgsVectorLayer
from .qmlTranslator import QmlTranslator
from .vectorTilesMaker import VectorTilesMaker

PLACEHOLDER_URL = r'http://MVT_HOSTING_URL/{z}/{x}/{y}.pbf'

class StyleManager:
    def __init__(self, project: QgsProject):
        self.project = project

    def write_mbstyle(self, output_path:str, vtsource_url:str, isMVTMakeMode:bool):
        import json
        visible_layers = self._get_visible_layers()

        mblayers = []
        vector_layers = []
        raster_layers = []

        #mapbox layers making
        for layer in visible_layers:
            mblayer = {}
            qml_str = self._qml_of(layer)
            qmlt = QmlTranslator(qml_str)
            if layer.type() == QgsMapLayer.VectorLayer:
                vector_layers.append(layer)
                mblayer = {
                    'id':layer.id(),
                    'source':'mvt',
                    'source-layer':layer.name(),
                    'type':qmlt.mbtype(),
                    'paint':qmlt.mbpaint()
                }
            elif layer.type() == QgsMapLayer.RasterLayer and layer.providerType() == 'wms':
                raster_layers.append(layer)
                mblayer = {
                    'id':layer.id(),
                    'source':layer.id(),
                    'type':'raster',
                    'paint':qmlt.mbpaint()
                }
            mblayers.insert(0, mblayer)
        
        #mapbox sources making
        ##RASTER
        mbsources = {}
        for rlayer in raster_layers:
            rsource = self._make_raster_source(rlayer)
            mbsources.update(rsource)
        
        ##VECTOR
        if len(vector_layers) > 0:
            if vtsource_url == '':
                vtsource_url = PLACEHOLDER_URL
            vtsource = {
                'mvt':{
                    'type':'vector',
                    'tiles':[vtsource_url]
                }
            }
            mbsources.update(vtsource)

        mbstyle = {
            'version':8,
            'sources':mbsources,
            'layers':mblayers
        }

        with open(output_path + '/style.json', 'w') as f:
            json.dump(mbstyle, f, indent=4)

        if isMVTMakeMode:
            vtmaker = VectorTilesMaker(vector_layers)
            vtmaker.generateBinaryTiles(output_path + '/pbf')

    def _make_raster_source(self, rlayer:QgsRasterLayer) -> dict:
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
            id:{
                'type':'raster',
                'tiles':[decoded_url],
                'tileSize':256
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