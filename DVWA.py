import subprocess
import time

# Vars
singlehash = '''
#############################################################################
'''
doublehash = '''
#############################################################################
#############################################################################
'''


installation_list = [
'sudo aptitude purge `dpkg -l | grep php| awk \'{print $2}\' |tr "\n" " "`',
'sudo add-apt-repository ppa:ondrej/php',
'sudo apt-get update',
'sudo apt-get upgrade',
'sudo apt-get install php5.6',
'sudo apt-get install php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-xml',
'sudo service apache2 start',
'sudo a2dismod php7.0',
'sudo a2enmod php5.6',
'sudo service apache2 restart',
'sudo apt-get install unzip',
'sudo apt-get install php5.6-gd',
'sudo service apache2 restart',
'sudo wget /var/www https://github.com/ethicalhack3r/DVWA/archive/master.zip',
'sudo mv master.zip /var/www/',
'sudo unzip /var/www/master.zip -d /var/www/html/'
]

def text():
	print(doublehash)
	print('''
 ______     _      __        __    ______     ______ 
|  ____|   | |     \ \      / /   |  ____|   |  ____|
| |____    | |      \ \    / /    | |____    | |____ 
|  ____|   | |       \ \  / /     |  ____|   |  ____|
| |____    | |___     \ \/ /      | |____    | |____
|______|   |_____|     \__/       |______|   |______|


This script will setup your DVWA server. After the
script is run, please read the instuctions and follow
them precisely. After this your DVWA server will run.
Just type in the [webserver ip]/DVWA-master
''')
	print(doublehash)

def installation():
	for module in installation_list:
		subprocess.call(module, shell=True)
		time.sleep(5)
		print("Done with: "+module)
		print("Continuing to the next module..")
		print(singlehash)

text()
question = input("Do you want to continue? (y/n): ")
if question == "y":
		installation()
		question2 = input("You need to continue manually from here. Do you want to continue? (y/n): ")
		if question2 == "y":
			print(singlehash)
			print("Now we need to create a file with the config.inc.php settings so we can launch the DVWA-master server")
			print("You will need to cd to following dir and then open the following file:")
			print("")
			print("cd /var/www/html/DVWA-master/config/")
			print("sudo nano config.inc.php.dist")
			print("Save it as a new file named: config.php.inc")
			print("")
			print(singlehash)
			exit()

		if question2 == "n":
			exit()

		else:
			print("Wrong input! Please answer with y/n..")
			print("Please run the script again.")

if question == "n":
	exit()

else:
	print("Wrong input! Please answer with y/n..")
