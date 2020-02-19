from .qgsTypes import QgsTypes
from .mapboxTypes import MapboxTypes

class QmlTranslator:
    def __init__(self, qml_str):
        self.qml_str = qml_str

    def mbpaint(self):
        qgs_style = self._parse()
        mbpaint = self.qgsstyle_to_mbpaint(qgs_style)
        return mbpaint

    def mbtype(self):
        qgs_type = self._qgs_type()

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

    def _qgs_type(self):
        qgs_style = self._parse()
        if 'rasterrenderer' in qgs_style:
            return 'raster'
        else:
            return qgs_style['symbol']['type']

    def _parse(self):
        import xml.etree.ElementTree as ET
        root = ET.fromstring(self.qml_str)
        qgs_style = {}

        #RASTER
        rasterrenderer = {}
        for child in root.getiterator():
            if child.tag == 'rasterrenderer': 
                rasterrenderer = child.attrib
        if rasterrenderer:
            qgs_style = {'rasterrenderer':rasterrenderer}
        else:
            #VECTOR
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

    def qgsstyle_to_mbpaint(self, qgs_style):
        mbtype = self.mbtype()
        mbpaint = {}
        if mbtype == MapboxTypes.CIRCLE.value:
            mbpaint = self.mbpaint_circle(qgs_style)
        elif mbtype == MapboxTypes.LINE.value:
            mbpaint = self.mbpaint_line(qgs_style)
        elif mbtype == MapboxTypes.FILL.value:
            mbpaint = self.mbpaint_fill(qgs_style)
        elif mbtype == MapboxTypes.RASTER.value:
            mbpaint = self.mbpaint_raster(qgs_style)
        return mbpaint

    def mbpaint_circle(self, qgs_style):
        style = {
            'circle-color': self._qgscolor_to_mbcolor(qgs_style['props']['color']),
            'circle-radius':self._qgssize_to_mbsize(qgs_style['props']['size'], qgs_style['props']['size_unit']),
            'circle-opacity':float(qgs_style['symbol']['alpha']),
            'circle-stroke-color':self._qgscolor_to_mbcolor(qgs_style['props']['outline_color'])
        }
        return style

    def mbpaint_line(self, qgs_style):
        style = {
            'line-color' : self._qgscolor_to_mbcolor(qgs_style['props']['line_color']),
            'line-width' : self._qgssize_to_mbsize(qgs_style['props']['line_width'], qgs_style['props']['line_width_unit']),
            'line-opacity' : float(qgs_style['symbol']['alpha'])
        }
        return style

    def mbpaint_fill(self, qgs_style):
        style = {
            'fill-color' : self._qgscolor_to_mbcolor(qgs_style['props']['color']),
            'fill-outline-color' : self._qgscolor_to_mbcolor(qgs_style['props']['outline_color']),
            'fill-opacity' : float(qgs_style['symbol']['alpha'])
        }
        return style

    def mbpaint_raster(self, qgs_style):
        style = {
            'raster-opacity':float(qgs_style['rasterrenderer']['opacity'])
        }
        return style

    def _qgscolor_to_mbcolor(self, qgscolor):
        #qgscolor: rrr,ggg,bbb,aaa
        #mbcolor: #RRGGBB 0x
        rgba = qgscolor.split(',') #[rrr,ggg,bbb] aaa
        mbcolor = "#"
        for c in rgba[:3]:
            hexed_color = hex(int(c))[2:]
            mbcolor = mbcolor + str(hexed_color).zfill(2)
        return mbcolor

    def _qgscolor_to_opacity(self, qgscolor):
        rgba = qgscolor.split(',') #[rrr,ggg,bbb] aaa
        opacity = float(rgba[-1] / 255)
        return opacity

    def _qgssize_to_mbsize(self, qgssize, qgsunit):
        mbsize = 0
        if qgsunit == 'MM':
            mbsize = int(float(qgssize) * 2.83465)
        if mbsize < 1:
            mbsize = 1
        return mbsize
