#-*- coding: UTF-8 -*-
import pyfoursquare as foursquare


class fsq(object):
    """docstring for fsq"""
    def __init__(self,):
        super(fsq, self).__init__()
        client_id = "1IRVQJDPFTEO04AE3EIYH020ITCYIL0YJBQEQKNS4B2LGA3Y"
        client_secret = "YLPWKV2KNQ3FK4LW531G3IZAOUJSVO3JSPZD1XGFG3XNSB2N"
        callback = 'http://localhost:8000/'
        ACCESS_TOKEN = 'KDUW5LVPWAWI42ZDQGTWMTFGFCRFF5XLICLGTFD2U2LC4SJT'

        self.auth = foursquare.OAuthHandler(client_id, client_secret, callback)
        self.auth.set_access_token(ACCESS_TOKEN)
        self.api = foursquare.API(self.auth)

    def local(self,lugar,comuna):
        return self.api.venues_search(query=lugar,near=comuna)

    def buscar(self,latitud,longitud,radio,limite=50):
        return self.api.venues_search(ll=str(latitud)+','+str(longitud),radius=radio,limit=limite)

    def print_venues(self,venues):
        print '--------------'
        for venue in venues:
            print venue.name
            #print venue.location.address #solo si existe
            print venue.location.lat
            print venue.location.lng
            print venue.id
            print venue.categories

def main():
    fsq_obj = fsq()
    
    latitud=-33.439049
    longitud=-70.630352
    radio=500
    limite=10
    venues = fsq_obj.buscar(latitud,longitud,radio,limite)
    fsq_obj.print_venues(venues)

    lugares = fsq_obj.local('Parque Arauco', 'Las Condes')
    fsq_obj.print_venues(lugares)



if __name__ == '__main__':
   main() 


