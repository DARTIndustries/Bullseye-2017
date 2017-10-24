#!/usr/bin/python3

#DART 10/14/17
#Bullseye Pi Code
#Main entry class

import sys
sys.path.insert(0, '../../')
from DART.Bullseye.Utils.AsciiArt import AsciiArt
import threading


asciiArt = AsciiArt()
version = "1.0.0"


def run() :
    #=====Show start screen======
    print(asciiArt.getBullseye(), asciiArt.getBy(), asciiArt.getDart())
    print("\n\t    -----v" + version + "-----\n")

#https://docs.python.org/3/library/threading.html
#    mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
#    mythread.start()             


if __name__ == "__main__":
    run()