from django.shortcuts import render
from django.shortcuts import render
import pandas as pd
from math import radians, sin, cos, sqrt, atan2
import geocoder
from geopy.geocoders import Nominatim

df = pd.read_csv('Data/data.csv')
columns_to_drop = ['cleartrip_seller_rating', 'country', 'crawl_date', 'image_count', 'landmark', 'locality', 'property_id', 'property_type', 'province', 'qts', 'room_area', 'room_count', 'room_type', 'sitename', 'state', 'tad_review_count', 'tad_review_rating', 'tad_stay_review_rating', 'tripadvisor_seller_rating', 'uniq_id']
df.drop(columns=columns_to_drop, inplace=True)
df = df.dropna(subset=['latitude', 'longitude'])
df['first_image_url'] = df['image_urls'].str.split('|').str[0]
df.drop('image_urls', axis=1, inplace=True)
df['hotel_star_rating'] = df['hotel_star_rating'].fillna(2)
df['hotel_star_rating'] = df['hotel_star_rating'].str[0].astype(float)


def algo(df,lat,long):
    input_lat = lat
    input_lon = long

    # Define radius in kilometers
    radius = 100

    # Function to calculate distance using haversine formula
    def calc_distance(lat1, lon1, lat2, lon2):
        R = 6371  # radius of Earth in kilometers
        dLat = radians(lat2 - lat1)
        dLon = radians(lon2 - lon1)
        a = sin(dLat/2) * sin(dLat/2) + cos(radians(lat1)) \
            * cos(radians(lat2)) * sin(dLon/2) * sin(dLon/2)
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        distance = round(distance, 2)
        return distance

    # Calculate distance between input and DataFrame values
    df['distance'] = df.apply(lambda row: calc_distance(input_lat, input_lon, row['latitude'], row['longitude']), axis=1)
    

    # Filter DataFrame to include only rows within radius
    nearby_df = df[df['distance'] <= radius]
    df = nearby_df.sort_values(by='distance')

    # Print the resulting DataFrame
    return df


def recm(request):
    if(request.method=="POST"):
        city = request.POST['city']
        

        geolocator = Nominatim(user_agent="my-app-name")
        location = geolocator.geocode(city)

        latitude = location.latitude
        longitude = location.longitude
        
        result = dict(algo(df,latitude,longitude))
        data = {}
        for key,value in result.items():
            data[key] = list(value)
        frm = zip(data['city'], data['room_facilities'], data['hotel_star_rating'], data['pageurl'], data['distance'], data['address'], data['first_image_url'], data['property_name'])

        dd = {
            'frm':frm,
            'user':1
        }
        if 'username' in request.session:
                dd['user'] = 0
        return render(request,'recommend.html',dd)
        


    
    else:  
        g = geocoder.ip('me')
        print(g)
        result = dict(algo(df,g.latlng[0],g.latlng[1]))
        data = {}
        for key,value in result.items():
            data[key] = list(value)
        frm = zip(data['city'], data['room_facilities'], data['hotel_star_rating'], data['pageurl'], data['distance'], data['address'], data['first_image_url'], data['property_name'])


    
        dd = {
            'frm':frm,
            'user':1
        }
        if 'username' in request.session:
                dd['user'] = 0
        
        return render(request,'recommend.html',dd)
