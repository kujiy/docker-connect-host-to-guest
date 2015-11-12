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

def main():
    global aContainerInfo

    # set container name and container hostname to ip
    for target in aContainerInfo:
        changeHosts(target)

def getAllContainerInfo():
    # get each Docker Container's info
    # 1. container name
    # 2. container ip-address
    # 3. container hostname
    # 4. containter domain name
    cmd = 'docker inspect --format "{{ .Name }},{{ .NetworkSettings.IPAddress }},{{ .Config.Hostname }},{{ .Config.Domainname }}"  $(docker ps --format={{.Names}})'
    # get comma separated string
    # eg:
    # /gitlab,  gitlab01 , 172.17.0.147 , gitlab01.feast.css.fujitsu.com
    # /redmine,  dee36d9bf409 , 172.17.0.135 ,
    res_comma = subprocess.check_output(cmd, shell=True)

    #convert to array

    #last result dict
    # 1. container name : ip
    # 2. container hostname : ip
    # 3. container domainname : ip
    return convertToContainerArray(res_comma)

def convertToContainerArray(res_comma):
    #last result dict
    aAllContainerInfo = {}

    aEachContainer = res_comma.split('\n')
    del aEachContainer[-1] #remove last empty element
    for aOneCont in aEachContainer:
        one = aOneCont.split(',')
        # remove / from container_name
        # before : /gitlab
        # after  : gitlab
        one[0] = one[0][1:]
        #print one

        #cont_name : ip
        aAllContainerInfo[one[0]] = one[1]
        #hostname:ip
        # Don't allow to exist duplicated hostname(s) with other containers
        if one[2] <> "" and aAllContainerInfo.get(one[2],"empty"):
            aAllContainerInfo[one[2]] = one[1]
        else:
            print "***************** CAUTION ********************"
            print "\n"
            print " Your containers have duplicated hostname(s)!!!"
            print "\n"
            print "**********************************************"
        #domainnname:ip
        if one[3] <> "":
            aAllContainerInfo[one[3]] = one[1]

    #print aAllContainerInfo
    return aAllContainerInfo


def changeHosts(target):
    global aContainerInfo

    # container name to ip
    ipaddress = aContainerInfo[target]

    if not validIP(ipaddress): #checks the IP address to see if it's valid.
        print(ipaddress, "is not a valid IP address. Usage: hostfileupdate.py [ipadddress] [hostmame]")
        sys.exit(2)

    update(ipaddress, target) #Calls the update function.

if __name__ == '__main__':
    # get all talbe
    aContainerInfo = getAllContainerInfo()
    main()
