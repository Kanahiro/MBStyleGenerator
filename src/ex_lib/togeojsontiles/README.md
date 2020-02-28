# togeojsontiles
[![PyPI version](https://badge.fury.io/py/togeojsontiles.svg)](https://badge.fury.io/py/togeojsontiles)  
Create geojson-tiles from gpx, mbtiles or geojson files.

togeojsontiles is a Python 3 package with bindings for [tippecanoe](https://github.com/mapbox/tippecanoe) (C++) and [togeojson](https://github.com/mapbox/togeojson) (javascript) 
that allows to create geojson vector tiles, `tiles/{z}/{x}/{y}.geojson`, from gpx, mbtiles or geojson files.  

The tiles allow to display large amounts of vector data on interactive maps without losing performance. 

The generated tiles can be shown on interactive slippy map like [OpenLayers](https://github.com/openlayers/ol3) and [Leaflet](https://github.com/Leaflet/Leaflet).

## Installation
togeojsontiles is compatible with Python 3.3, 3.4, 3.5. It is listed on PyPi as 'togeojsonfiles'.  
The recommended way to install is via pip,
```
$ pip install togeojsontiles
```

## Dependencies 
This package provides Python bindings for tippecanoe (C++) to create the tiles, and togeojson (javascript) to convert gpx to geojson.
These libraries do all the work and are required.

##### tippecanoe
See [tippecanoe](https://github.com/mapbox/tippecanoe) for installation instructions. It has a few system level dependencies, but is rather easy to build.

##### togoejson
To install togoejson (javascript) in your path,
```
$ npm install -g togeojson
```

## Usage
##### gpx to geojson
```python
import togeojsontiles

togeojsontiles.gpx_to_geojson(file_gpx='test.gpx', file_geojson='test.geojson')
```

##### geojson to mbtiles
```python
import togeojsontiles

TIPPECANOE_DIR = '/usr/local/bin/'

togeojsontiles.geojson_to_mbtiles(
    filepaths=['./data/test1.geojson', './data/test2.geojson'],
    tippecanoe_dir=TIPPECANOE_DIR,
    mbtiles_file='out.mbtiles',
    maxzoom=14
)
```

##### mbtiles to geojson-tiles
```python
import togeojsontiles

TIPPECANOE_DIR = '/usr/local/bin/'

togeojsontiles.mbtiles_to_geojsontiles(
  tippecanoe_dir=TIPPECANOE_DIR, 
  tile_dir='project/data/tiles/', 
  mbtiles_file='out.mbtiles'
)
```
