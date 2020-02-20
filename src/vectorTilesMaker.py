import os
import tempfile
from qgis.core import QgsMapLayer, QgsVectorLayer
from .exlib.togeojsontiles import togeojsontiles
from .exlib.mbutil import mbutil

TIPPECANOE_PATH = os.path.dirname(__file__) + '/exlib/tippecanoe/'
TMP_MBTILES_PATH = tempfile.gettempdir() + '/tmp.mbtiles'

class VectorTilesMaker:
    def __init__(self, layers: [QgsVectorLayer]):
        self.layers = layers

    def generateBinaryTiles(self, filepath, maxzoom=22, minzoom=0):
        return

    def write_tmp_geojson(self, layer: QgsVectorLayer, output_path):
        return {}
    

    def write_tmp_mbtiles(self, geojsons:[object], maxzoom, minzoom):
        togeojsontiles.geojson_to_mbtiles(
            filepaths=geojsons,
            tippecanoe_dir=TIPPECANOE_PATH,
            mbtiles_file=TMP_MBTILES_PATH,
            maxzoom=maxzoom,
            minzoom=minzoom
        )

    def mbtiles_to_pbf(self):
        print(mbutil.disk_to_mbtiles())
        return