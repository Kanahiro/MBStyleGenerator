import processing
from qgis.core import QgsVectorLayer


class VectorTilesMaker:
    def __init__(self, layers: [QgsVectorLayer]):
        self.layers = layers

    def generateBinaryTiles(self, output_path, maxzoom=18, minzoom=0):
        processing.run('native:writevectortiles_xyz', {
            'EXTENT': None,
            'LAYERS': self.make_dict_for_processing(),
            'MIN_ZOOM': minzoom,
            'MAX_ZOOM': maxzoom,
            'XYZ_TEMPLATE': r'{z}/{x}/{y}.pbf',
            'OUTPUT_DIRECTORY': output_path
        })

    def make_dict_for_processing(self):
        dicts_for_processing = []
        for layer in self.layers:
            tmp_dict = {}
            tmp_dict['layer'] = layer
            dicts_for_processing.append(tmp_dict)
        return dicts_for_processing
