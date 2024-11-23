from multiprocessing.managers import State

import requests
import json

def lat_long_input():
    print("Lat and Long can be found by inputting location here: https://www.latlong.net/")
    lat = input("Enter your latitude: ")
    long = input("Enter your longitude: ")
    return lat, long

def main():
    lat, long = lat_long_input()

    url = f'https://api.weather.gov/points/{lat},{long}'

    # Make the GET request
    locationRequest = requests.get(url)

    # Check the status code
    if locationRequest.status_code == 200:
        # Parse the JSON data
        locationData = locationRequest.json()

        json_string = json.dumps(locationData)

        locationResults = json.loads(json_string)

        # Navigate to the city and state
        city = locationResults['properties']['relativeLocation']['properties']['city']
        state = locationResults['properties']['relativeLocation']['properties']['state']

        # Print and verify the locationResults

        print("\nIs the following location correct?")
        print(f'State: {state}')
        print(f'City: {city}')

        locationCheck = input("\n(Y/N): ")

        if locationCheck == "Y" or "y" or "yes" or "Yes":
            print("Awesome, this thing works!")
        else:
            print("Damn, I can't program for shit 💀")



    else:
        print(f'Error: {locationRequest.status_code}')



if __name__ == "__main__":
    main()