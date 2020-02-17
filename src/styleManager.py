from qgis.core import QgsProject, QgsMapLayer, QgsMapLayerStyle, QgsRasterLayer
from .qmlTranslator import QmlTranslator
from .vectorTilesMaker import VectorTilesMaker

class StyleManager:
    def __init__(self, project: QgsProject):
        self.project = project

    def export_mbstyle(self, filepath):
        sources = self.make_mbsources(self.project)

        visible_layers = self._get_visible_layers(self.project)
        layers = self.make_mblayers(sources['id'], visible_layers)

        mbstyle = {
            'version':8,
            'sources':sources,
            'layers':layers
        }

        return qmls

    def make_mbstyle(self, project: QgsProject, output_path='', vtsource_url=''):
        visible_layers = self._get_visible_layers(project)
        vector_layers = []
        raster_layers = []
        for layer in visible_layers:
            if layer.type() == QgsMapLayer.VectorLayer:
                vector_layers.append(layer)
            elif layer.type() == QgsMapLayer.RasterLayer:
                raster_layers.append(layer)
        
        sources = {}

        for rlayer in raster_layers:
            if rlayer.providerType == 'wms':
                rsource = self._make_raster_source(rlayer)
                sources.update(rsource)

        #mvt making process
        '''
        if vtsource_url == '':
            #generate binary mvt
            vtmaker = VectorTilesMaker(vector_layers)
            vtmaker.generateBinaryTiles()
            vtsource_url = r'./tiles/{z}/{x}/{y}.pbf'
        '''
        
        vtsource = {
            'mvt':{
                'type':'vector',
                'url':vtsource_url,
            }
        }
        sources.update(vtsource)

    def _make_raster_source(self, rlayer:QgsRasterLayer):
        data_provider = rlayer.dataProvider()
        metadata = data_provider.dataSourceUri()
        params = metadata.split('&')
        provider_data = {}
        for param in params:
            #kv[0] = key, kv[1] = value
            kv = param.split('=')
            provider_data[kv[0]] = kv[1]
        url = provider_data['url']
        id = rlayer.id()
        rsource = {
            id:{
                'type':'raster',
                'url':url,
                'tileSize':256
            }
        }
        return rsource
    
    def _get_visible_layers(self, project: QgsProject):
        visible_layers = []
        for treeLayer in project.layerTreeRoot().findLayers():
            if treeLayer.isVisible():
                visible_layers.append(treeLayer.layer())
        return visible_layers

    def _qml_of(self, layer: QgsMapLayer):
        qgs_style = QgsMapLayerStyle()
        qgs_style.readFromLayer(layer)
        return qgs_style.xmlData()