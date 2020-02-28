import os
import tempfile
import json
from qgis.core import QgsMapLayer, QgsVectorLayer, QgsVectorFileWriter, QgsCoordinateReferenceSystem
from .exlib.togeojsontiles import togeojsontiles
from .exlib.mbutil import mbutil

TIPPECANOE_PATH = os.path.dirname(__file__) + '/exlib/tippecanoe/'
TMP_MBTILES_PATH = tempfile.gettempdir() + '/tmp.mbtiles'
TMP_GEOJSON_PATH = tempfile.gettempdir()

class VectorTilesMaker:
    def __init__(self, layers: [QgsVectorLayer]):
        self.layers = layers

    def generateBinaryTiles(self, output_path, maxzoom=22, minzoom=0):
        geojson_filepaths = []
        for layer in self.layers:
            geojson_filepath = self.write_tmp_geojson(layer)
            geojson_filepaths.append(geojson_filepath)
        togeojsontiles.geojson_to_mbtiles(
            filepaths=geojson_filepaths,
            tippecanoe_dir=TIPPECANOE_PATH,
            mbtiles_file=TMP_MBTILES_PATH,
            extra_args=('-pC',)
        )
        mbutil.mbtiles_to_disk(TMP_MBTILES_PATH, output_path, format='pbf', scheme='xyz')

    def write_tmp_geojson(self, layer: QgsVectorLayer) -> str:
        filename = TMP_GEOJSON_PATH + '/' + layer.id() + '.geojson'
        crs = QgsCoordinateReferenceSystem()
        crs.createFromUserInput('WGS84')
        QgsVectorFileWriter.writeAsVectorFormat(
            layer=layer,
            fileName=filename,
            fileEncoding='utf-8',
            destCRS=crs,
            driverName='GeoJSON'
        )
        return filename