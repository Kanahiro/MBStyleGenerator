import subprocess
import os
import fnmatch


def gpx_to_geojson(file_gpx, file_geojson):
    args = ['togeojson', file_gpx]
    try:
        output = subprocess.check_output(args)
    except subprocess.CalledProcessError as e:
        print(e)
        raise

    with open(file_geojson, 'w') as fileout:
        fileout.write(output.decode('utf-8'))
        print(file_geojson + ' created!')


def geojson_to_mbtiles(
        filepaths,
        tippecanoe_dir,
        mbtiles_file='out.mbtiles',
        maxzoom=14,  # Maxzoom: the highest zoom level for which tiles are generated
        minzoom=0,  # Minzoom: the lowest zoom level for which tiles are generated
        full_detail=12,  # Detail at max zoom level
        lower_detail=12,  # Detail at lower zoom levels
        min_detail=7,  # Minimum detail that it will try if tiles are too big at regular detail
        extra_args=()
    ):
    args = [
        os.path.join(tippecanoe_dir, 'tippecanoe'),
        # '-B', str(base_zoom),  # Base zoom, the level at and above which all points are included in the tiles
        '-d', str(full_detail),  # Detail at max zoom level
        '-D', str(lower_detail),  # Detail at lower zoom levels
        '-m', str(min_detail),  # Minimum detail that it will try if tiles are too big at regular detail
        '-f', # Delete the mbtiles file if it already exists instead of giving an error
        # '-al',
        # '-g', str(1000),
        # '-r', str(5),
        '-o', mbtiles_file,
        '-z', str(int(maxzoom)),
        '-Z', str(int(minzoom))
    ]
    for arg in extra_args:
        args.append(arg)

    for filepath in filepaths:
        args.append(filepath)
    output = subprocess.check_output(args)
    print(output.decode('utf8'))


def mbtiles_to_geojsontiles(tippecanoe_dir, tile_dir, mbtiles_file='out.mbtiles'):
    tilelistfile = 'tilelist.txt'
    args = [os.path.join(tippecanoe_dir, 'tippecanoe-enumerate'), mbtiles_file]
    output = subprocess.check_output(args)
    with open(tilelistfile, 'w') as fileout:
        fileout.write(output.decode('utf-8'))
    with open(tilelistfile, 'r') as filein:
        for line in filein:
            line = line.rstrip()  # line has format '<path>/out.mbtiles 14 8423 5390'
            args = [os.path.join(tippecanoe_dir, 'tippecanoe-decode')]
            words = line.split()
            for word in words:
                args.append(word)
            output = subprocess.check_output(args)
            filename = os.path.join(tile_dir, words[1] + '/' + words[2] + '/' + words[3] + '.geojson')
            mkdir_p(os.path.dirname(filename))
            with open(filename, 'w') as fileout:
                fileout.write(output.decode('utf-8'))
    os.remove(tilelistfile)


def gpxdir_to_geojson(gpx_dir='data/gpx/', geojson_dir='tmp/'):
    files_created = []
    for rootdir, subdirs, filenames in os.walk(gpx_dir):
        for fname in fnmatch.filter(filenames, '*.gpx'):
            file_gpx = os.path.join(rootdir, fname)
            mkdir_p(geojson_dir)
            file_geojson = os.path.join(geojson_dir, fname.replace('.gpx', '.geojson'))
            gpx_to_geojson(file_gpx, file_geojson)
            files_created.append(file_geojson)
    return files_created


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        pass
