from packages.rightmove_webscraper_master.rightmove_webscraper import RightmoveData
import time
import pandas as pd

def getData(location, url):
    list_frames = []
    for x in range(0, 1000):
        if x % 24 == 0:
            list_url = url.split('index=')
            url = list_url[0] + 'index=' + str(x) + list_url[1]
            try:
                data = RightmoveData(url)
                df = data.get_results
                df['searchterm'] = location
                list_frames.append(df)
            except IndexError as er:
                return list_frames



            # url = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E87490&radius=40.0&propertyTypes=bungalow%2Cdetached%2Csemi-detached%2Cterraced&includeSSTC=true&mustHave=newHome&dontShow=&furnishTypes=&keywords="
# end_url = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E87490&radius=40.0&index=1008&propertyTypes=bungalow%2Cdetached%2Csemi-detached%2Cterraced&includeSSTC=true&mustHave=newHome&dontShow=&furnishTypes=&keywords="
#
# try:
#     rm = RightmoveData(end_url)
# except IndexError as er:
#     pass
#
# print (rm)
#
# data = rm.get_results
#
# print (data)

# data.to_csv("results.csv")

with open("locations.txt", "r") as f:
    list_locations = f.read().splitlines()
    for url_data in list_locations:
        list_url_data = url_data.split(',')
        df = getData(list_url_data[0], list_url_data[1])