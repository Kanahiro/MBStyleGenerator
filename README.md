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
<img src='https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R7VptU%2BI6FP41zNz7gR3aQsGPAurq4h3xdffTTqChRNOmplHAX39P2vQ1KAVx8V5hGKbnNDkheZ6cPElbs3re%2FISjYHrOHExrZsOZ16x%2BzTTtdgd%2BpWMRO6zmQexwOXFil5E5rsgLVs6G8j4RB4eFgoIxKkhQdI6Z7%2BOxKPgQ52xWLDZhtNhqgFysOa7GiOreO%2BKIaeztmO3M%2Fx0Td5q0bNiqfx5KCquehFPksFnOZR3VrB5nTMRX3ryHqRy7ZFzuThd3dPBgn5wNw0d00%2F1x%2Fc9tPQ52vE6VtAsc%2B2Lj0C8Pk%2BPvt837n8HF8XDWODkcndVVlcYzok9qvK7EguJz5MO4cNVv6YlvhjPiUeSD1Z0wX1ypOzAUXUSJ68P1GP4j1LS6z5gLAjgcqhuCBeAdTwl1BmjBnmRPQoHGD4nVnTJOXiAsonDLAAfc5kJRyrQLJa5kTXA3wMtxCGUukuExUtcAhUKVGTNKURCSUfSHZREPcZf4XSYE85JA7Ml3sKOsFO%2FIEJw9pAyS9SuCosCTo4HnOUoqkE4w87DgCyii7qZ8UxPOSOxZRl%2FDVr5pjroHyofUjHHT0GlrlzDDkO%2FCGGTNWaXmmhWbA0AKzSEKuPtI4K4cxTDPRbjI9TRzRQxdg62GxtaAs%2FsoaxyCf%2BiGF8ouExfGXuRISvFEvErRMEBj4ruDqEy%2FmXkuVeeli0HdCY3oMSWOg%2F2IPgIJFDNMciZgxBfR6LS68IUx7DW%2BtWot%2BEM9sI3Mhq8szkWP%2BcA0RCJKYaDvDEsKLyHbm9N5NdkWRRDXBTvPrQLK60La1CDVsKMkSjhT4WV5oTwZVwDrAUQyXILktQS6Xzc0tC0dbWsJshSNML1gIRGEyfg8LltCfFegtsxqoHY%2BCNOWhumME4F%2Fe6MI1b%2F%2B3k%2FPikjaG%2BbirUFpa1AOPXrNkR9SJFhlgdDYC4TtCQSjtGKb7YosMQxzE4VQbs%2FqfF6F0Nb4%2BujR34BNrBDkxRfNPXZlmn0WaXCwlwZbB3XX0sDQN5zeKJD9%2Fx%2BqgvwK2Ey52WMUFk6r77OIux%2BF9M6lg6Hv1ryRWARfWP%2BtDWJn1znYsDQQb0EhMH5NKA7P0UP1Q6K9BtyiBrQaG2rAzQ6JKjXX%2FhwS0NCPFChaYB7GEhBm9tANYxIPpD%2Ba8F8zH6Wz%2B78jCg39cGGvCt8N6x%2BUhXVhhGH98QcPnu%2FPh%2FNhw7rHdVMD1cU%2B5jJPEB%2FxRbTafF3dsD6gu1d%2F%2Bk78vBtJgZMY2f3h0U6EQ7NV4elSawlT7I2EQ6vc3Cd%2BumTqh50aRbHvHMqH0pKKFIUhGa%2BGsrjtq0kxJT8aIyD2MaEJOzEdxWkoR9s1WYGdwqPxVzkhs1UepKaqzzFFgjwXH6S%2Fgf%2BFTIxvUM1uFUOE7ImPsaqV4akFSg8c00DNb3aJHzCXXSxWx6o3i7Gs0pEom0xCXAixNXrp51k3p2Cf%2BsHTqw8scxomSjqvLkNypamSJ1NhEymSLqQ5N2Jh6VRirVwVJes4jxpm9VXNfG07nL4Monpby79vUYnAB1shsGG2U56pyPWWpF4j92l%2BAH%2BmRyFueYPLfnCGu6NGZ%2Fhs3Sx5VaNadspRCPDgi58SRxgwZf5Ksw8Y%2FXnBWiTWnIhcNbB%2BJRHhOqskjaTO0hRUPXfFueEN9qjhiOf9Su2kUye3AC1b7hLfOymUbpST%2FVOntIxWzoGlt0LS1zZWJMBtsU8%2FzPtj7Hsnk1YyxN4lQbSTFWNTghysYNrGBAEze8ktLp69KWgd%2FQs%3D'>