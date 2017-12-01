sudo su -s /bin/bash homeassistant
/srv/homeassistant/bin/hass --script check_config
sudo systemctl start home-assistant@homeassistant
cd /srv/homeassistant
sudo systemctl restart
git push origin master
git clone  address.git
