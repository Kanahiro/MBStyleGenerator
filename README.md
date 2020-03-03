<img src='sample.png'>

## Caution
Now this plugin is EXPERIMENTAL yet.
Simple object such as Polygon, Line, Point are supported (this mean Text are not supported now).

## Abtract
You can use this plugin in two ways.
One, to generate only Mapbox Style file style.json.
Another, generate style.json and also MVT files - tiled .pbf files.

## Usage
In menu bar, Web->MBStyleGenerator, then a dialog will be shown.
You set some paramaters, following
- Output Path (style.json will be written)
- MVT Source Url (.pbf files URL, Optional)
- Make MVT Source or not

Press Run and style.json will be generated on the directory you choosed.
It takes some minuites to make MVT Source, many vector means longer time to make.

## Tips
- This plugin will read only VISIBLE layers on your project, including raster tile.
- When MVT Source URL are not set but any vector layer are visible on your project, you have to set hosting URL of MVT Source on style.json manualy.
- A layer name in MVT Source is same to the name in QGIS project.

## License
This plugin use following libraries.
- [mapbox/tippecanoe](https://github.com/mapbox/tippecanoe)
- [bartromgens/togeojsontiles](https://github.com/bartromgens/togeojsontiles)
- [mapbox/mbutil](https://github.com/mapbox/mbutil)

## Classes
<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;www.draw.io\&quot; modified=\&quot;2020-03-03T07:46:55.356Z\&quot; agent=\&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36\&quot; etag=\&quot;MrfBlPPFQo07_cx6cPr1\&quot; version=\&quot;12.7.9\&quot; type=\&quot;device\&quot;&gt;&lt;diagram id=\&quot;C5RBs43oDa-KdzZeNtuy\&quot; name=\&quot;Page-1\&quot;&gt;7VptU+I6FP41zNz7gR3aQsGPAurq4h3xdffTTqChRNOmplHAX39P2vQ1KAVx8V5hGKbnNDkheZ6cPElbs3re/ISjYHrOHExrZsOZ16x+zTTtdgd+pWMRO6zmQexwOXFil5E5rsgLVs6G8j4RB4eFgoIxKkhQdI6Z7+OxKPgQ52xWLDZhtNhqgFysOa7GiOreO+KIaeztmO3M/x0Td5q0bNiqfx5KCquehFPksFnOZR3VrB5nTMRX3ryHqRy7ZFzuThd3dPBgn5wNw0d00/1x/c9tPQ52vE6VtAsc+2Lj0C8Pk+Pvt837n8HF8XDWODkcndVVlcYzok9qvK7EguJz5MO4cNVv6YlvhjPiUeSD1Z0wX1ypOzAUXUSJ68P1GP4j1LS6z5gLAjgcqhuCBeAdTwl1BmjBnmRPQoHGD4nVnTJOXiAsonDLAAfc5kJRyrQLJa5kTXA3wMtxCGUukuExUtcAhUKVGTNKURCSUfSHZREPcZf4XSYE85JA7Ml3sKOsFO/IEJw9pAyS9SuCosCTo4HnOUoqkE4w87DgCyii7qZ8UxPOSOxZRl/DVr5pjroHyofUjHHT0GlrlzDDkO/CGGTNWaXmmhWbA0AKzSEKuPtI4K4cxTDPRbjI9TRzRQxdg62GxtaAs/soaxyCf+iGF8ouExfGXuRISvFEvErRMEBj4ruDqEy/mXkuVeeli0HdCY3oMSWOg/2IPgIJFDNMciZgxBfR6LS68IUx7DW+tWot+EM9sI3Mhq8szkWP+cA0RCJKYaDvDEsKLyHbm9N5NdkWRRDXBTvPrQLK60La1CDVsKMkSjhT4WV5oTwZVwDrAUQyXILktQS6Xzc0tC0dbWsJshSNML1gIRGEyfg8LltCfFegtsxqoHY+CNOWhumME4F/e6MI1b/+3k/PikjaG+birUFpa1AOPXrNkR9SJFhlgdDYC4TtCQSjtGKb7YosMQxzE4VQbs/qfF6F0Nb4+ujR34BNrBDkxRfNPXZlmn0WaXCwlwZbB3XX0sDQN5zeKJD9/x+qgvwK2Ey52WMUFk6r77OIux+F9M6lg6Hv1ryRWARfWP+tDWJn1znYsDQQb0EhMH5NKA7P0UP1Q6K9BtyiBrQaG2rAzQ6JKjXX/hwS0NCPFChaYB7GEhBm9tANYxIPpD+a8F8zH6Wz+78jCg39cGGvCt8N6x+UhXVhhGH98QcPnu/Ph/Nhw7rHdVMD1cU+5jJPEB/xRbTafF3dsD6gu1d/+k78vBtJgZMY2f3h0U6EQ7NV4elSawlT7I2EQ6vc3Cd+umTqh50aRbHvHMqH0pKKFIUhGa+Gsrjtq0kxJT8aIyD2MaEJOzEdxWkoR9s1WYGdwqPxVzkhs1UepKaqzzFFgjwXH6S/gf+FTIxvUM1uFUOE7ImPsaqV4akFSg8c00DNb3aJHzCXXSxWx6o3i7Gs0pEom0xCXAixNXrp51k3p2Cf+sHTqw8scxomSjqvLkNypamSJ1NhEymSLqQ5N2Jh6VRirVwVJes4jxpm9VXNfG07nL4Monpby79vUYnAB1shsGG2U56pyPWWpF4j92l+AH+mRyFueYPLfnCGu6NGZ/hs3Sx5VaNadspRCPDgi58SRxgwZf5Ksw8Y/XnBWiTWnIhcNbB+JRHhOqskjaTO0hRUPXfFueEN9qjhiOf9Su2kUye3AC1b7hLfOymUbpST/VOntIxWzoGlt0LS1zZWJMBtsU8/zPtj7Hsnk1YyxN4lQbSTFWNTghysYNrGBAEze8ktLp69KWgd/Qs=&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://www.draw.io/js/viewer.min.js"></script>