from .mapboxTypes import MapboxTypes
class QgsMapboxLayout:
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
        return

    def _line(self, qgs_style):
        return

    def _fill(self, qgs_style):
        return

    def _raster(self, qgs_style):
        return