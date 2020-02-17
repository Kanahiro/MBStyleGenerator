from qgis.core import QgsMapLayer, QgsVectorLayer

class VectorTilesMaker:
    def __init__(self, layers: [QgsVectorLayer]):
        self.layers = layers

    def generateBinaryTiles(self, filepath, maxzoom=22, minzoom=0):
        return