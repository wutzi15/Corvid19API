from pyproj import Proj, transform

class Projection:
    @staticmethod
    def wgsToXy(lon,lat):
        return transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), lon,lat)
    
    @staticmethod
    def pointToXy(point):
        xy=point.split(",")
        return Projection.wgsToXy(float(xy[0]),float(xy[1]))
        