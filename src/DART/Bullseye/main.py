#!/usr/bin/python3

#DART 10/14/17
#Bullseye Pi Code
#Main entry class
#Namespace = DART.Bullseye

import sys
import os
import signal
from threading import Thread
sys.path.insert(0, '../../')
from DART.Bullseye.Utils.AsciiArt import AsciiArt
from DART.Bullseye.Networking.MailMan import MailMan
from DART.Bullseye.Business.Mr_Manager import Mr_Manager

asciiArt = AsciiArt()
version = "1.0.0"
mailMan = MailMan()
mrManager = Mr_Manager()


def run() :
    #=====Show start screen======
    print(asciiArt.getBullseye(), asciiArt.getBy(), asciiArt.getDart())
    print("\n\t    -----v" + version + "-----\n")

    #=====Start Threads=====
    mailManThread = Thread(target = mailMan.run) 
    mrManagerThread = Thread(target = mrManager.run) 

    
    mailManThread.start()
    mrManagerThread.start()

    mailManThread.join()
    mrManagerThread.join()


if __name__ == "__main__":
    run()