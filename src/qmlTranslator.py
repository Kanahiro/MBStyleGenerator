class QmlTranslator:
    def __init__(self, qml_str):
        self.qml_str = qml_str

    def mbpaint(self):
        qgs_style = self.parse(self.qml_str)
        mbpaint = self.qgsstyle_to_mbpaint(qgs_style)
        return mbpaint

    def mbtype(self):
        qgs_style = self.parse(self.qml_str)
        qgs_type = qgs_style['symbol']['type']
        if qgs_type == 'marker':
            return 'circle'
        elif qgs_type == 'line':
            return 'line'
        elif qgs_type == 'polygon':
            return 'fill'
        elif qgs_type == 'raster':
            return 'raster'
        else:
            return qgs_type

    def parse(self, qml_str):
        import xml.etree.ElementTree as ET
        root = ET.fromstring(qml_str)
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
        return {'symbol':symbol, 'layer':layer, 'props':props}

    def qgsstyle_to_mbpaint(self, qgs_style):
        mbtype = self.mbtype()
        mbpaint = {}
        if mbtype == 'circle':
            mbpaint = self.mbpaint_circle(qgs_style)
        elif mbtype == 'line':
            mbpaint = self.mbpaint_line(qgs_style)
        elif mbtype == 'fill':
            mbpaint = self.mbpaint_fill(qgs_style)
        elif mbtype == 'raster':
            mbpaint = self.mbpaint_raster(qgs_style)
        return mbpaint

    def mbpaint_circle(self, qgs_style):
        style = {
            'circle-color':qgs_style['props']['color'],
            'circle-radius':qgs_style['props']['size'],
            'circle-opacity':qgs_style['symbol']['alpha']
        }
        return style

    def mbpaint_line(self, qgs_style):
        style = {
            'line-color' : qgs_style['props']['line_color'],
            'line-width' : qgs_style['props']['line_width'],
            'line-opacity' : qgs_style['symbol']['alpha']
        }
        return style

    def mbpaint_fill(self, qgs_style):
        style = {
            'fill-color' : qgs_style['props']['fill_color'],
            'fill-opacity' : qgs_style['symbol']['alpha']
        }
        return style

    def mbpaint_raster(self, qgs_style):
        return {}