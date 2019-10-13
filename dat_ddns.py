from requests import get
import time
import sys
import logging
import os
from threading import Thread
import subprocess

def updateIP():
    ip = get('https://api.ipify.org').text
    open('ip/ip', 'w').close()
    file = open('ip/ip','w')
    file.write(ip)

def startDat():
    if(os.path.isdir('./ip/.dat')):
        os.system('dat share ip')
    else:
        os.system('dat create ip --title "ddns" --description "ddns"')
        os.system('dat share ip')

def resetDat():
    os.system('rm -r ip && mkdir ip')

def main():
    #if ip folder don't exist create it
    newpath = 'ip'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    #dat thread
    t = Thread(target=startDat, args=())
    t.start()
    #Update IP
    exit = 0
    print('To exit press Ctrl+C')
    while(exit == 0):
        try:
            updateIP()
            time.sleep(240)
        except KeyboardInterrupt:
            #kill thread for dat sync
            sys.exit(0)
main()
