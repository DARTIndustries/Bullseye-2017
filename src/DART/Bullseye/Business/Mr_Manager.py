#!/usr/bin/python3

# DART 10/14/17
# Namespace = DART.Bullseye

import sys
import threading
import time

sys.path.insert(0, '../../../')
from DART.Bullseye.Business.DeliveryBoy import DeliveryBoy


class Mr_Manager:
    def __init__(self):
        self.longList = []
        self.longListLock = threading.Lock()

    def processor(self):
        """Processes new messages as they come in and executes non-long running commands"""
        print("MrManager:  waiting for commands")
        while (True):
            try:
                command = DeliveryBoy.inQueue.get()  # blocking
                if (command == "exit"):
                    sys.exit(0)

                # --Acquire Long List Lock--
                self.longListLock.acquire()  # Blocking
                self.filterConflicting(command)

                # ---Execute Command---
                if command.isLongRunning:
                    self.longList.append(command)
                else:
                    command.execute()
            except Exception as e:
                print(" Mr Manager: Top level exception in run. Exception: ", e)

            finally:
                # --Release Long List Lock--
                self.longListLock.release()

    def filterConflicting(self, newCommand):
        """Removes any old long running commands that conflict with the new command"""
        if len(self.longList) > 0:
            newList = []
            for longCommand in self.longList:
                if not newCommand.isConflicting(longCommand):
                    newList.append(newCommand)
            self.longList = newList

    def executer(self):
        """Executes Long running Commands. Runs in its own thread"""
        while True:
            if len(self.longList) > 0:
                try:
                    # --Acquire Long List Lock--
                    self.longListLock.acquire()  # Blocking

                    newList = []
                    for command in self.longList:
                        isDone = command.execute()
                        if not isDone:
                            newList.append(command)
                    self.longList = newList
                except Exception as e:
                    print(" Mr Manager Long running: Top level exception in run. Exception: ", e)
                finally:
                    # --Release Long List Lock--
                    self.longListLock.release()

            time.sleep(0.005)
