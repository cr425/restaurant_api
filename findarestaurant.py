from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "NTBCYEW33YPVNZ25LX3HDZC0FJNTZOM5KGCGUMHU4ZHXBFUW"
foursquare_client_secret = "S10D2D2UGLSID1PLQCLRPKX2ERBO5N35VGAAPIH0BEX050ER"


def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    lat, lng = getGeocodeLocation(location)
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like
   #https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

    mealType = "pizza"
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=40.7,-74&query=%s'
    % (foursquare_client_id, foursquare_client_secret, mealType))

    http_request = httplib2.Http()
    result = json.loads(http_request.request(url, 'GET')[1])

    first_restaurant = result['response']['venues'][0]['name']
    venue_id = result['response']['venues'][0]['id']
    photo_url = ('https://api.foursquare.com/v2/venues/%s/photos?oauth_token=GL3NCZ3LYWDYJEC51BYJMRTMBUDICLVKY4TQJGODVK2IQOOM&v=20170227' % venue_id)
    photo = json.loads(http_request.request(photo_url, 'GET')[1])
    
    photo_url_final = photo['response']['photos']['items'][0]['user']['photo']['prefix'] + photo['response']['photos']['items'][0]['user']['photo']['suffix'][1:]
    
	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id 
    #(you can change this by altering the 300x300 value in the URL or
    # replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url	
if __name__ == '__main__':
	res = findARestaurant("Pizza", "Tokyo, Japan")
#	findARestaurant("Tacos", "Jakarta, Indonesia")
#	findARestaurant("Tapas", "Maputo, Mozambique")
#	findARestaurant("Falafel", "Cairo, Egypt")
#	findARestaurant("Spaghetti", "New Delhi, India")
#	findARestaurant("Cappuccino", "Geneva, Switzerland")
#	findARestaurant("Sushi", "Los Angeles, California")
#	findARestaurant("Steak", "La Paz, Bolivia")
#	findARestaurant("Gyros", "Sydney Australia")