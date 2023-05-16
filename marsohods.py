import requests
import os
from urllib.request import urlretrieve
from PIL import Image

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
params = {"api_key": "efnxfBSPzK6ZFfvXHmOmwnRWWvhhHs5M1GjgpNvQ", "earth_date": "2022-07-21"}

response = requests.get(url, params=params)
data = response.json()

try:
    os.mkdir("Mars")
except: None

count = 0  # счетчик загруженных и сохраненных фотографий
for photo in data["photos"]:
    if count == 5:
        break  # если загружено и сохранено 5 фотографий, выходим из цикла
    urlretrieve(photo["img_src"], f"Mars/mars_photo_{count+1}.jpg")
    #img = Image.open(f"Mars/mars_photo_{count+1}.jpg")
    #img.show()
    count += 1