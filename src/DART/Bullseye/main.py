#!/usr/bin/python3

#DART 10/14/17
#Bullseye Pi Code
#Main entry class

import sys
from threading import Thread
from queue import Queue
sys.path.insert(0, '../../')
from DART.Bullseye.Utils.AsciiArt import AsciiArt
from DART.Bullseye.Networking.MailMan import MailMan
from DART.Bullseye.Mr_Manager import Mr_Manager

asciiArt = AsciiArt()
version = "1.0.0"
networkQueue = Queue()
mailMan = MailMan(networkQueue)
mrManager = Mr_Manager(networkQueue)


def run() :
    #=====Show start screen======
    print(asciiArt.getBullseye(), asciiArt.getBy(), asciiArt.getDart())
    print("\n\t    -----v" + version + "-----\n")

    #=====Start Threads=====
    mrManagerThread = Thread(target = mrManager.run) 
    mailManThread = Thread(target = mailMan.run) 
    
    mrManagerThread.start()
    mailManThread.start()


if __name__ == "__main__":
    run()