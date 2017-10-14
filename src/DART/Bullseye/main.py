#!/usr/bin/python3

#DART 10/14/17
#Bullseye Pi Code
#Main entry class

import sys
sys.path.insert(0, '../../')
from DART.Bullseye.Utils.AsciiArt import AsciiArt



asciiArt = AsciiArt()
version = "1.0.0"


def run() :
    #=====Show start screen======
    print(asciiArt.getBullseye(), asciiArt.getBy(), asciiArt.getDart())
    print("\n\t    -----v" + version + "-----\n")



if __name__ == "__main__":
    run()