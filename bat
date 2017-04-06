sudo su -s /bin/bash homeassistant
sudo /srv/homeassistant/bin/hass --script check_config
sudo systemctl start home-assistant@homeassistant
cd /srv/homeassistant
sudo systemctl restart
git push origin master
git clone  address.git
hass --script check_config
