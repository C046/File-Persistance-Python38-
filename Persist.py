# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:46:56 2024

@author: hadaw
"""
import threading
import time
from File_Persistance_Python38.SystemFunctions import Create
import numpy as np

class Persistance(Create):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Assign the sleeper function to a thread to be able to run in the background.
        self.sleeper_thread = threading.Thread(target=self.sleeper)
        
    def sleeper(self):
        if self.file_exists():
            # If file does exist
            # do nothing.
            pass 
        else:
            # Generate the file and directory
            self.generate_filepath()
            self.create_file()
            
        # Sleep for 30 seconds
        time.sleep(60)
        # Remove the file
        self._delete()
        
        # Perform shuffling below
        drives = np.asanyarray(self.get_drives())
        drives = np.random.shuffle(drives)
        print(drives)
            
if __name__ == "__main__":
    Persistance().sleeper()