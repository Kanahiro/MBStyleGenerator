from .types import MapboxTypes, QgsTypes
from .qgsMapboxPaint import QgsMapboxPaint
from .qgsMapboxLayout import QgsMapboxLayout

class QmlTranslator:
    def __init__(self, qml_str):
        self.qml_str = qml_str

    def mbpaint(self) -> dict:
        qgs_style = self._parse()
        mbtype = self.mbtype()
        return QgsMapboxPaint(qgs_style, mbtype).export()

    def mblayout(self) -> dict:
        qgs_style = self._parse()
        mbtype = self.mbtype()
        return QgsMapboxLayout(qgs_style, mbtype).export()

    def mbtype(self) -> str:
        qgs_style = self._parse()
        qgs_type = self._qgs_type(qgs_style)

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

    def _qgs_type(self, qgs_style) -> str:
        qgs_type = ''
        if 'rasterrenderer' in qgs_style:
            qgs_type = 'raster'
        else:
            qgs_type = qgs_style['symbol']['type']
        return qgs_type

    def _parse(self) -> dict:
        import xml.etree.ElementTree as ET
        root = ET.fromstring(self.qml_str)
        qgs_style = {}

        rasterrenderer = {}
        for child in root.getiterator():
            if child.tag == 'rasterrenderer': 
                rasterrenderer = child.attrib

        #when raster
        if rasterrenderer:
            qgs_style = {'rasterrenderer':rasterrenderer}
        #when vector
        else:
            symbol = {}
            layer = {}
            props = {}
            for child in root.getiterator():
                if child.tag == 'symbol': 
                    symbol = child.attrib
                if child.tag == 'layer':
                    layer = child.attrib
                if child.tag == 'prop':
                    props[child.attrib['k']] = child.attrib['v']
            qgs_style = {'symbol':symbol, 'layer':layer, 'props':props}

        return qgs_style