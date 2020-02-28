import os
import unittest

import togeojsontiles


class TestToGeoJsonTiles(unittest.TestCase):
    gpx_file = 'data/test/test1.gpx'
    geojson_file = 'data/test/test1.geojson'
    mbtiles_file = 'data/test/out.mbtiles'
    tippecanoe_dir = 'lib/'
    tiles_dir = 'data/test/tiles/'

    def setUp(self):
        if os.path.exists(self.geojson_file):
            os.remove(self.geojson_file)
        self.assertFalse(os.path.exists(self.geojson_file))
        if os.path.exists(self.mbtiles_file):
            os.remove(self.mbtiles_file)
        self.assertFalse(os.path.exists(self.mbtiles_file))

    def test_gpx_to_geojsontiles(self):
        self.gpx_to_geojson()
        self.geojson_to_mbtiles()
        self.mbtiles_to_geojsontiles()

    def gpx_to_geojson(self):
        self.assertTrue(os.path.exists(self.gpx_file))
        self.assertFalse(os.path.exists(self.geojson_file))
        togeojsontiles.gpx_to_geojson(self.gpx_file, self.geojson_file)
        self.assertTrue(os.path.exists(self.geojson_file))

    def geojson_to_mbtiles(self):
        togeojsontiles.geojson_to_mbtiles(
            filepaths=[self.geojson_file],
            tippecanoe_dir=self.tippecanoe_dir,
            mbtiles_file=self.mbtiles_file,
            maxzoom=14
        )
        self.assertTrue(os.path.exists(self.mbtiles_file))

    def mbtiles_to_geojsontiles(self):
        togeojsontiles.mbtiles_to_geojsontiles(self.tippecanoe_dir, self.tiles_dir, self.mbtiles_file)
        self.assertTrue(os.path.exists(self.mbtiles_file))
        tile_file = os.path.join(self.tiles_dir, '14/8426/5393.geojson')
        self.assertTrue(os.path.exists(tile_file))
        os.remove(tile_file)


if __name__ == '__main__':
    unittest.main()