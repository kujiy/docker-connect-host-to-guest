__author__ = 'Jason Vanzin forked by kujiy'
import sys #used to get commandline arguments
import subprocess
import os

def update(ipaddress, hostname):
        cmd = 'hostile set ' + ipaddress + ' ' + hostname
	print(cmd)
        os.system(cmd)

def validIP(ipaddress):
    """ str -> bool
    Found this on http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
    The function takes the IP address as a string and splits it by ".". It then checks to see if there are 4 items
    in the list. If not, it's not valid. Next, it makes sure the last two characters are not ".0", which would signify an
    invalid address. Third it checks the last character to make sure it's not a ".", which would be invalid. Lastly, it
    checks each item to make sure it's greater than 0 or equal to zero but less than or equal to 255.
    :param ipaddress:
    :return:
    """
    parts = ipaddress.split(".")
    if len(parts) != 4:
        return False
    if ipaddress[-2:] == '.0': return False
    if ipaddress[-1] == '.': return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

def getContainerIP(hostname):
        cmd = 'docker inspect --format "{{ .NetworkSettings.IPAddress }}" ' + hostname
        res = subprocess.check_output(cmd, shell=True)
	return res.rstrip() #remove linebreak

def getAllContainerNames():
	cmd = 'docker ps --format "{{.Names}}"'
        res = subprocess.check_output(cmd, shell=True)
	aContainers = res.split('\n')
	del aContainers[-1] #remove last empty element
	return aContainers

def main():
	aContainers = getAllContainerNames()
	for container_name in aContainers:
		#print(container_name)
		changeHosts(container_name)


def changeHosts(hostname):

    ipaddress = getContainerIP(hostname)

    if not validIP(ipaddress): #checks the IP address to see if it's valid.
        print(ipaddress, "is not a valid IP address. Usage: hostfileupdate.py [ipadddress] [hostmame]")
        sys.exit(2)

    update(ipaddress, hostname) #Calls the update function.

if __name__ == '__main__':
    main()
