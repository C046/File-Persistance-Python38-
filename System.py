import os
import secrets
import string
import psutil
import numpy as np

class Create:
    def __init__(self):
        """
        Constructor for the Create class.
        Initializes an instance with a default filepath set to None.
        """
        self.filepath = None
        self.drives = self.get_drives()
        self.maxxy = self.drives.size

    def _delete(self):
        """
        Delete the previously created file and its parent directory.

        Raises:
            FileNotFoundError: If the file or directory is not found.
        """
        if self.filepath:
            try:
                os.remove(self.filepath)
                print(f"Successfully deleted file: {self.filepath}")

                os.rmdir(os.path.dirname(self.filepath))
                print(f"Successfully deleted directory: {os.path.dirname(self.filepath)}")

            except FileNotFoundError:
                print("File or directory not found.")

    def shuffle_drives(self):
        np.random.shuffle(self.get_drives())
        self.drives = self.drives[np.random.randint(0,self.maxxy)]
        
    def generate_filepath(self, ext=".txt", drives=None):
        """
        Generate a random filepath for a new file.

        Args:
            directory (str): The directory where the file will be created. If None, uses the user's home directory.
            ext (str): The file extension. Defaults to ".txt".

        Returns:
            str: The generated filepath.
        """
        # Perform shuffling
        if drives is None:
            self.shuffle_drives()
        else:
            self.shuffle_drives()

        # Construct the directory, folder name, filename, and full filepath
        self.drives = os.path.join(self.drives, "")
        self.folder_name = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(12))
        self.filename = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(12)) + ext

        self.filepath = os.path.abspath(os.path.join(self.drives, self.folder_name, self.filename))
        #return self.filepath

    def create_file(self):
        """
        Create a new file at the previously generated filepath.

        Prints a success message or a message if the file already exists.
        """
        try:
            # Create the necessary directories and the file
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

            with open(self.filepath, "x", encoding="utf-8"):
                pass

            print(f"Successful file creation at: {self.filepath}")

        except FileExistsError:
            print(f"File already exists: {self.filepath}")

    def file_exists(self):
        """
        Check if the file at the generated filepath exists.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        if self.filepath:
            abspath_exists = os.path.exists(self.filepath)
            return abspath_exists
        else:
            return False
        
    def get_drives(self):
        if os.name == 'posix':
            return np.asanyarray([part.device for part in psutil.disk_partitions()]) if 'psutil' in globals() else np.asanyarray([])
        elif os.name == 'nt':
            return np.asanyarray([os.path.abspath(f"{chr(d)}:\\") for d in range(ord('A'), ord('Z') + 1) if os.path.exists(f"{chr(d)}:")])
        else:
            return np.asanyarray([])