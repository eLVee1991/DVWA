# DVWA (Damn Vulnerable Web Application)
Codes help setting up DVWA on Ubuntu webserver. These scripts and .txt help with the installation. They follow the instructions of JackkTuturial:

You can watch it here!
https://www.youtube.com/watch?v=5BG6iq_AUvM


## How to use DVWA.py
You need to have unzip! If you do not have unzip please do:
- sudo apt-get install unzip

then do:
- cd /tmp
- wget https://github.com/eLVee1991/DVWA/archive/master.zip
- sudo unzip master.zip
- cd DVWA-master
- python3 DVWA.py

## If it doens't work
You can use the DVWA server.txt for manual copy and paste installation. It might be handy to SSH into the server and set-up LAMP, System Essentials and SSH Service. Once installed do:
- sudo service ssh start
- login on your other computer via ssh, so you can copy and paste code.

##### Enjoy!

