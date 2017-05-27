#!/bin/bash

echo "Starting the installation"
echo "Installing php package.."
sudo apt-get purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "` &
wait
echo "Adding php5 repository to apt"
sudo add-apt-repository ppa:ondrej/php &
wait
echo "Updating the system"
sudo apt-get update &
wait
echo "Upgrading the system"
sudo apt-get upgrade &
wait
echo "Installing php5.6"
echo "This is the only working versions for DVWA"
sudo apt-get install php5.6 &
wait
echo "Installing mbstring, mcrypt mysql and xml for php5.6"
sudo apt-get install php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-xml &
wait
echo "I can start the apache server now so you can check in your browser if everything is working"
read -p "Do you want me to continue? Press any key"
sudo service apache2 start
echo "You can check if the server is running now"
read -p "Is it working? Press any key to continue."
echo "Check if the php7.0 mod is disabled"
sudo a2dismod php7.0 &
wait
echo "Checking if the php5.6 mod is enabled"
sudo a2enmod php5.6 &
wait
echo "Restarting the apache2 server."
sudo service apache2 restart &
wait
echo "Installing unzip"
sudo apt-get install unzip &
wait
echo "Installing php5.6-gd"
sudo apt-get install php5.6-gd
wait
echo "Downloading the DVWA zipfile"
sudo wget /var/www https://github.com/ethicalhack3r/DVWA/archive/master.zip &
wait
echo "Moving the file to the /var/www/ folder"
sudo mv master.zip /var/www/ &
wait
echo "Unzipping the file and moving it to /var/www/html."
echo "The file will be named: DVWA-master"
sudo unzip /var/www/master.zip -d /var/www/html/ &
wait
echo "Now we need to create a file with the config.inc.php settings so we can launch the DVWA-master server"
echo "You will need to cd to following dir and then open the following file:"
echo ""
echo "cd /var/www/html/DVWA-server/config/"
echo "sudo nano config.inc.php.dist"
echo "Save it as a new file named: config.php.inc"
read -p "Please do this manually from here. Press any key to continue."
exit











