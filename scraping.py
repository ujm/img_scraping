import urllib3
from bs4 import BeautifulSoup
import certifi
import urllib.request
import os
from progressbar import ProgressBar
import sys

url = input("url : ")
path = input("path : ")

def file_download(url, img_type):
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', url)
    
    soup = BeautifulSoup(r.data, 'html.parser')
    
    images = []
    
    for link in soup.find_all('img'):
        src = link.get('src')
        if img_type in src:
            images.append(src)
    
    return images

def load_config(config):
    print(config)

img_type = 'jpg'

file_url = file_download(url, img_type)

def save_file(path, file_url):
    if path not in os.listdir('./'):
        os.mkdir(path)

    for image in file_url:
        filename = image.split('/')[-1]
        urllib.request.urlretrieve(image, os.path.join(path, filename))

save_file(path, file_url)
