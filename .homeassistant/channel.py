#!/home/homeassistant/.homeassistant/bin/python
from pylgtv import WebOsClient
import sys

webos_client = WebOsClient('192.168.1.12')
webos_client.set_channel(str(sys.argv[-1]))
print(webos_client.get_current_channel())
#webos_client.launch_app('netflix')
#webos_client.launch_app('home theater')

#for app in webos_client.get_apps():
#    print(app)
