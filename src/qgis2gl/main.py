from .types import MapboxTypes, QgsTypes
from .qgsMapboxPaint import QgsMapboxPaint
from .qgsMapboxLayout import QgsMapboxLayout


class Qgis2Gl:
    def __init__(self, qml_str):
        self.qml_str = qml_str
        self.qgs_style = self._parse_qml()

    def category_is_visible(self, idx):
        categories = self.qgs_style.get('categories')
        if categories is None:
            return False

        category = categories[idx]
        return category.get('render') == 'true'

    def mbpaint(self, idx=0) -> dict:
        symbol = self.qgs_style['symbols'][idx]
        return QgsMapboxPaint(symbol, self.mbtype(idx)).export()

    def mblayout(self, idx=0) -> dict:
        symbol = self.qgs_style['symbols'][idx]
        return QgsMapboxLayout(symbol, self.mbtype(idx)).export()

    def mbtype(self, idx=0) -> str:
        qgs_type = self.qgs_type(idx)
        if qgs_type == QgsTypes.MARKER.value:
            return MapboxTypes.CIRCLE.value
        elif qgs_type == QgsTypes.LINE.value:
            return MapboxTypes.LINE.value
        elif qgs_type == QgsTypes.FILL.value:
            return MapboxTypes.FILL.value
        elif qgs_type == QgsTypes.RASTER.value:
            return MapboxTypes.RASTER.value
        else:
            return qgs_type

    def qgs_type(self, idx=0) -> str:
        qgs_type = ''
        if self.qgs_style.get('rasterrenderer'):
            qgs_type = 'raster'
        else:
            qgs_type = self.qgs_style.get('symbols')[idx]['symbol']['type']
        return qgs_type

    def _parse_qml(self) -> dict:
        import xml.etree.ElementTree as ET
        root = ET.fromstring(self.qml_str)
        qgs_style = {}

        rasterrenderer = {}
        for child in root.getiterator():
            if child.tag == 'rasterrenderer':
                rasterrenderer = child.attrib

        # when raster
        if rasterrenderer:
            qgs_style = {'rasterrenderer': rasterrenderer}
        # when vector
        else:
            categories = []
            symbols = []
            symbol = {}
            for child in root.getiterator():
                if child.tag == 'categories':
                    iter = list(child)
                    for i in iter:
                        # some category
                        categories.append(i.attrib)
                if child.tag == 'symbols':
                    symbols_iter = list(child)
                    for s in symbols_iter:
                        symbol = {
                            'symbol': s.attrib,
                            'props': {}
                        }
                        layer_iter = list(s)
                        for l in layer_iter:
                            prop_iter = list(l)
                            for p in prop_iter:
                                if p.tag == 'prop':
                                    symbol['props'][p.attrib['k']
                                                    ] = p.attrib['v']
                        symbols.append(symbol)

            qgs_style = {
                'categories': categories,
                'symbols': symbols,
            }

        return qgs_style
