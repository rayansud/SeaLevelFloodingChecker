# coding=utf-8
import urllib2
import json


def get_elevation_for_latlng():


    elevation_key = 'AIzaSyDlBuyhQP3dZkoRYPekfL7lB_X5jNljEmU'

    lat = raw_input("Enter your latitude: ")
    long = raw_input("Enter your longitude: ")
    elevation_request = 'https://maps.googleapis.com/maps/api/elevation/json?locations='+str(lat)+','+str(long)+'&key='+elevation_key

    response = urllib2.urlopen(elevation_request)
    json_response = response.read().decode('utf-8')

    data= json.loads(json_response)
    elevation = data['results'][0]['elevation']

    return elevation

def get_elevation_for_city():

    nearest_city = raw_input("Nearest City: ")
    geocode_key = 'AIzaSyAf0Sb8bMbFmYYsWw7Kf-lIVPY0pKHyiy4'
    elevation_key = 'AIzaSyDlBuyhQP3dZkoRYPekfL7lB_X5jNljEmU'

    geocode_request = 'https://maps.googleapis.com/maps/api/geocode/json?address='+nearest_city+'&key='+geocode_key

    response = urllib2.urlopen(geocode_request)
    json_response = response.read().decode('utf-8')

    data= json.loads(json_response)
    location = data['results'][0]['geometry']['location']
    lat =  location['lat']
    long  = location['lng']

    elevation_request = 'https://maps.googleapis.com/maps/api/elevation/json?locations='+str(lat)+','+str(long)+'&key='+elevation_key

    response = urllib2.urlopen(elevation_request)
    json_response = response.read().decode('utf-8')

    data= json.loads(json_response)
    elevation = data['results'][0]['elevation']

    return elevation


def get_years_before_underwater_for_elevation(ele):
    years = ele/(9.0/(2100.0-2017))
    current_age = 2017.0-int(birth_year)
    age_at_flooding = current_age+years
    number_generations = years/27.0

    print "Your home will be underwater in "+str(int(round(years)))+" years, within "+str(int(round(number_generations)))+" generations. You would be "+str(int(round(age_at_flooding)))+" years old (if you survive)"

birth_year = raw_input("Birth year: ")
##el = get_elevation_for_latlng()
el = get_elevation_for_city()
print "\n---The following projection is based on unchecked pollution, causing a 4ºC rise in temperatures by 2100. It assumes a constant rate of temperature increase, of ~12 cm/year. Elevation data from Google Maps.---\n"
print "Your elevation is "+ str(int(round(el)))+" meters"
get_years_before_underwater_for_elevation(el)
