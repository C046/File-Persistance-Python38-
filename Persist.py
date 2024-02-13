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
        super(Create, self).__init__(*args, **kwargs)
        # Assign the sleeper function to a thread to be able to run in the background.
        self.sleeper_thread = threading.Thread(target=self.sleeper)
        self.drives = self.get_drives
        
    def sleeper(self):
        
        # Perform shuffling below
        if self.drives:
            self.drives = np.random.shuffle(self.drives)[np.random.randint(0,len(self.drives))]
        else:
            self.drives = np.asanyarray(self.get_drives())
            self.drives = np.random.shuffle(self.drives)[np.random.randint(0,len(self.drives))] 
            
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
        

        
        
        print(self.drives)
            
if __name__ == "__main__":
    Persistance().sleeper()