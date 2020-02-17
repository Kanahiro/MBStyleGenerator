class QmlTranslator:
    def __init__(self, qml_str):
        self.qml_str = qml_str

    def to_mbstyle_paint(self):
        qgs_style = self.parse(self.qml_str)
        mbstyle = self.qgsstyle_to_mbstyle(qgs_style)
        return mbstyle

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

    def qgsstyle_to_mbstyle(self, qgs_style):
        layerType = qgs_style['symbol']['type']
        mbstyle = {}
        if layerType == 'marker':
            mbstyle = self.mbstyle_circle(qgs_style)
        if layerType == 'line':
            mbstyle = self.mbstyle_line(qgs_style)
        return mbstyle

    def mbstyle_circle(self, qgs_style):
        style = {
            'circle-color':qgs_style['props']['color'],
            'circle-radius':qgs_style['props']['size'],
            'circle-opacity':qgs_style['symbol']['alpha']
        }
        return style

    def mbstyle_line(self, qgs_style):
        style = {
            'line-color' : qgs_style['props']['line_color'],
            'line-width' : qgs_style['props']['line_width'],
            'line-opacity' : qgs_style['symbol']['alpha']
        }
        return style

    def mbstyle_fill(self, qgs_style):
        style = {
            'fill-color' : qgs_style['props']['fill_color'],
            'fill-opacity' : qgs_style['symbol']['alpha']
        }
        return style