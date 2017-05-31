#!/home/homeassistant/.homeassistant/bin/python
from pylgtv import WebOsClient
from os import system
from time import sleep
import sys

webos_client = WebOsClient('192.168.1.12')
#channel="7-1"
#for letter in channel:
#  print(letter)
#  if letter=="-":
#      system("/home/homeassistant/.homeassistant/tivoscript/ADVANCE")
#  else:
#      system("/home/homeassistant/.homeassistant/tivoscript/NUM"+letter)
#      sleep(1) 
#system("/home/homeassistant/.homeassistant/tivoscript/ENTER")
#sleep(2)
#system("/home/homeassistant/.homeassistant/tivoscript/RECORD")
#sleep(1)
#system("/home/homeassistant/.homeassistant/tivoscript/RIGHT")
#exit(0)
#webos_client.set_channel(str(sys.argv[-1]))
print(webos_client.get_input())
#webos_client.set_input("com.webos.app.hdmi2")
if "hdmi1" in webos_client.get_input():
   system("/home/homeassistant/.homeassistant/tivoscript/RECORD")
   sleep(1)
   system("/home/homeassistant/.homeassistant/tivoscript/RIGHT")
   exit(0)

if "livetv" in webos_client.get_input():
   result=(webos_client.get_current_channel())
#   print(result)
   channel=result["channelNumber"]
   print(result["channelNumber"])
   for letter in channel:
     print(letter)
     if letter=="-":
       system("/home/homeassistant/.homeassistant/tivoscript/ADVANCE")
     else:
       system("/home/homeassistant/.homeassistant/tivoscript/NUM"+letter)
       sleep(1)
   system("/home/homeassistant/.homeassistant/tivoscript/ENTER")
   sleep(2)
   system("/home/homeassistant/.homeassistant/tivoscript/RECORD")
   sleep(1)
   system("/home/homeassistant/.homeassistant/tivoscript/RIGHT")
#print(inputname)
#exit(0)
#print(result)
#data=json.loads(result)
#if result["returnValue"]==False:
#   print("not on channel")
#   exit(0)

#system("/home/homeassistant/.homeassistant/tivoscript/RECORD")

#webos_client.launch_app('netflix')
#webos_client.launch_app('home theater')

#for app in webos_client.get_apps():
#    print(app)
