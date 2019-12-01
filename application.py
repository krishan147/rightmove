from packages.rightmove_webscraper_master.rightmove_webscraper import RightmoveData
import time
import pandas as pd

def getData(location, url):
    list_frames = []
    for x in range(0, 1000):
        if x % 24 == 0:
            time.sleep(8)
            list_url = url.split('index=')
            url = list_url[0] + 'index=' + str(x) + list_url[1]
            try:
                data = RightmoveData(url)
                df = data.get_results
                df['searchterm'] = location

                print (df)

                list_frames.append(df)
            except IndexError as er:
                print (list_frames)
                return list_frames

with open("locations.txt", "r") as f:
    list_locations = f.read().splitlines()
    for url_data in list_locations:
        list_url_data = url_data.split(',')
        list_frames = getData(list_url_data[0], list_url_data[1])
        df = pd.concat(list_frames)
        df.to_csv("results/"+list_url_data[0]+".csv")