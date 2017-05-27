import subprocess

# Vars
singlehash = '''
#############################################################################
'''

print "Starting the installation"
print "Installing php package.."
subprocess.call('sudo apt-get purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "`', shell=True)
print(singlehash)

print "Adding php5 repository to apt"
subprocess.call('sudo add-apt-repository ppa:ondrej/php', shell=True)
print(singlehash)

print "Updating the system"
subprocess.call('sudo apt-get update', shell=True)
print(singlehash)

print "Upgrading the system"
subprocess.call('sudo apt-get upgrade', shell=True)
print(singlehash)

print "Installing php5.6"
print "This is the only working versions for DVWA"
subprocess.call('sudo apt-get install php5.6', shell=True)
print(singlehash)

print "Installing mbstring, mcrypt mysql and xml for php5.6"
subprocess.call('sudo apt-get install php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-xml', shell=True)
print(singlehash)

print "I can start the apache server now so you can check in your browser if everything is working"
subprocess.call('sudo service apache2 start', shell=True)

print "You can check if the server is running now"
question = raw_input("Do you want to continue? (y/n): ")
if question == "y":
	print "Check if the php7.0 mod is disabled"
	subprocess.call('sudo a2dismod php7.0', shell=True)
	print(singlehash)

	print "Checking if the php5.6 mod is enabled"
	subprocess.call('sudo a2enmod php5.6', shell=True)
	print(singlehash)

	print "Restarting the apache2 server."
	subprocess.call('sudo service apache2 restart', shell=True)
	print(singlehash)

	print "Installing unzip"
	subprocess.call('sudo apt-get install unzip', shell=True)
	print(singlehash)

	print "Installing php5.6-gd"
	subprocess.call('sudo apt-get install php5.6-gd', shell=True)
	print(singlehash)

	print "Downloading the DVWA zipfile"
	subprocess.call('sudo wget /var/www https://github.com/ethicalhack3r/DVWA/archive/master.zip', shell=True)
	print(singlehash)

	print "Moving the file to the /var/www/ folder"
	subprocess.call('sudo mv master.zip /var/www/', shell=True)
	print(singlehash)

	print "Unzipping the file and moving it to /var/www/html."
	print "The file will be named: DVWA-master"
	subprocess.call('sudo unzip /var/www/master.zip -d /var/www/html/', shell=True)
	print(singlehash)

	question2 = raw_input("You need to continue manually from here. Do you want to continue? (y/n): ")
	if question2 == "y";
		print "Now we need to create a file with the config.inc.php settings so we can launch the DVWA-master server"
		print "You will need to cd to following dir and then open the following file:"
		print ""
		print "cd /var/www/html/DVWA-master/config/"
		print "sudo nano config.inc.php.dist"
		print "Save it as a new file named: config.php.inc"
		print ""

	elif question2 == "n":
		exit()
	else:
		print "Wrong input! Please answer with y/n.."
		
elif question == "n":
	exit()
else:
	print "Wrong input! Please answer with y/n.."
