from .qgsTypes import QgsTypes
from .mapboxTypes import MapboxTypes
class QgsMapboxPaint:
    def __init__(self, qgs_style:dict, mbtype:str):
        self.qgs_style = qgs_style
        self.mbtype = mbtype

    def export(self):
        if self.mbtype == MapboxTypes.CIRCLE.value:
            return self._circle(self.qgs_style)
        elif self.mbtype == MapboxTypes.LINE.value:
            return self._line(self.qgs_style)
        elif self.mbtype == MapboxTypes.FILL.value:
            return self._fill(self.qgs_style)
        elif self.mbtype == MapboxTypes.RASTER.value:
            return self._raster(self.qgs_style)

    def _circle(self, qgs_style):
        import math
        paint = {
            'circle-color': self._qgscolor_to_mbcolor(qgs_style['props']['color']),
            'circle-radius':math.ceil(0.5 * self._qgssize_to_mbsize(qgs_style['props']['size'], qgs_style['props']['size_unit'])),
            'circle-opacity':float(qgs_style['symbol']['alpha'])
        }
        #when outline enable
        if qgs_style['props']['outline_style'] == 'yes':
            paint['circle-stroke-color'] = self._qgscolor_to_mbcolor(qgs_style['props']['outline_color'])
            paint['circle-stroke-width'] = self._qgssize_to_mbsize(qgs_style['props']['outline_width'], qgs_style['props']['outline_width_unit'])
        return paint

    def _line(self, qgs_style):
        paint = {
            'line-color' : self._qgscolor_to_mbcolor(qgs_style['props']['line_color']),
            'line-width' : self._qgssize_to_mbsize(qgs_style['props']['line_width'], qgs_style['props']['line_width_unit']),
            'line-opacity' : float(qgs_style['symbol']['alpha'])
        }
        #line style
        if qgs_style['props']['line_style'] == 'dash':
            paint['line-dasharray'] = [3,1]
        if qgs_style['props']['line_style'] == 'dot':
            paint['line-dasharray'] = [1,1]

        return paint

    def _fill(self, qgs_style):
        paint = {
            'fill-color' : self._qgscolor_to_mbcolor(qgs_style['props']['color']),
            'fill-outline-color' : self._qgscolor_to_mbcolor(qgs_style['props']['outline_color']),
            'fill-opacity' : float(qgs_style['symbol']['alpha'])
        }
        return paint

    def _raster(self, qgs_style):
        paint = {
            'raster-opacity':float(qgs_style['rasterrenderer']['opacity'])
        }
        return paint

    def _qgscolor_to_mbcolor(self, qgscolor):
        #qgscolor: rrr,ggg,bbb,aaa 000-255
        #mbcolor: #RRGGBB 00-FF
        rgba = qgscolor.split(',') #[rrr,ggg,bbb,aaa]
        mbcolor = "#"
        for c in rgba[:3]: #[rrr,ggg,bbb]aaa
            hexed_color = hex(int(c))[2:]
            mbcolor = mbcolor + str(hexed_color).zfill(2)
        return mbcolor

    def _qgscolor_to_opacity(self, qgscolor):
        rgba = qgscolor.split(',') #[rrr,ggg,bbb,aaa]
        opacity = float(rgba[3] / 255)
        return opacity

    #qgssize: size * unit
    #mbsize: point
    def _qgssize_to_mbsize(self, qgssize, qgsunit):
        import math
        mbsize = 1
        if qgsunit == 'MM':
            mbsize = mbsize + math.floor(float(qgssize) * 2.83465)
        return mbsize
