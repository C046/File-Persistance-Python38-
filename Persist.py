# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:46:56 2024

@author: hadaw
"""
import threading
import time
from SystemFunctions import Create


class Persistance(Create):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # And something to work on at work
        
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
        
            
if __name__ == "__main__":
    Persistance.sleeper()