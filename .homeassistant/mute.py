#!/home/homeassistant/.homeassistant/bin/python
from pylgtv import WebOsClient
import sys

webos_client = WebOsClient('192.168.1.12')
webos_client.set_volume(0)
#webos_client.launch_app('netflix')
#webos_client.launch_app('home theater')

#for app in webos_client.get_apps():
#    print(app)
