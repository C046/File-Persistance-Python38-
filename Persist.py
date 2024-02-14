import threading
import time
import psutil
import os
import numpy as np
from File_Persistance_Python38.System import Create

class Persistance(Create):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assign the sleeper function to a thread to be able to run in the background.
        self.sleeper_thread = threading.Thread(target=self.sleeper())
        self.sleeper_thread.start()

    def sleeper(self):
        while True:
            if self.file_exists():
                # If file does exist, do nothing.
                pass
            else:
                # Generate the file and directory
                self.generate_filepath(drives=self.drives)
                print(self.filepath)
                self.create_file()
            
            
            
            # Sleep for 60 seconds
            time.sleep(60)
            # Remove the file
            self._delete()
            # Set the filepath to none
            self.filepath = None


if __name__ == "__main__":
    Persistance()