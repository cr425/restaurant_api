#!/usr/bin/python
# encoding: utf-8
 
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
    mealType = "pizza"
    location = "Tokoyo, Japan"
    
    lat, lng = getGeocodeLocation(location)

    #assemble url for foursquare API call    
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s4&query=%s'
    % (foursquare_client_id, foursquare_client_secret, lat, lng, mealType))
    
    #make http request object and use it to GET data from API
    http_request = httplib2.Http()
    result = json.loads(http_request.request(url, 'GET')[1])
    
    #use the result from the API call and parse dictionary object for the restaurant name, address
    restaurant = result['response']['venues'][0]['name']
    restaurant_address = result['response']['venues'][0]['location']['formattedAddress'][0] + ", "+ result['response']['venues'][0]['location']['formattedAddress'][1] 
    #use result to get the photo for the restaurant. First get the venue ID, and make another API call to get the photos for that API
    venue_id = result['response']['venues'][0]['id']
    #assemble photourl with venue_id
    photo_url = ('https://api.foursquare.com/v2/venues/%s/photos?oauth_token=GL3NCZ3LYWDYJEC51BYJMRTMBUDICLVKY4TQJGODVK2IQOOM&v=20170227' % venue_id)
    #make call to API and get image for restaurant
    photo = json.loads(http_request.request(photo_url, 'GET')[1])
    image = photo['response']['photos']['items'][0]['user']['photo']['prefix'] + photo['response']['photos']['items'][0]['user']['photo']['suffix'][1:]

    #print results when definition is called as final call to action
    sys.getdefaultencoding()
    print "Restaurant Name: "
    sys.stdout.write(restaurant)
#    print "Restaurant Address: " 
#    sys.stdout.write(restaurant_address)
#    print "Image: " + sys.stdout.write(image)

    return     


	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id 
    #(you can change this by altering the 300x300 value in the URL or
    # replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url	
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
#	findARestaurant("Tacos", "Jakarta, Indonesia")
#	findARestaurant("Tapas", "Maputo, Mozambique")
#	findARestaurant("Falafel", "Cairo, Egypt")
#	findARestaurant("Spaghetti", "New Delhi, India")
#	findARestaurant("Cappuccino", "Geneva, Switzerland")
#	findARestaurant("Sushi", "Los Angeles, California")
#	findARestaurant("Steak", "La Paz, Bolivia")
#	findARestaurant("Gyros", "Sydney Australia")