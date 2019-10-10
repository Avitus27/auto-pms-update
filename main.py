#!/usr/bin/python3

import os
import requests

import settings

from packaging import version

system_type = os.getenv("OS")
build = os.getenv("BUILD")
plex = os.getenv("PLEX_LOCATION")
download_location = os.getenv("DOWNLOAD_LOCATION")


result = requests.get('https://plex.tv/pms/downloads/5.json')
result = result.json()

result = result['computer'][system_type]
current_version = version.parse(result['version'])
system_version = version.parse(str(os.system(plex + " --version")))

if current_version > system_version:
    print("Update Found!")
else:
    print("No Update")
    exit(0)

for item in result['releases']:
    if item['build'] == build:
        update_url = item['url']
        break

file_download = requests.get(update_url)
file_location = "{}update.deb".format(download_location)

with open(file_location, 'wb') as f:
    f.write(file_download.content)

os.system("dpkg -i {}".format(file_location))
