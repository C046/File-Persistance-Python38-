# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:31:31 2024

@author: hadaw
"""

import os
import secrets
import string

class Create:
    def __init__(self):
        """
        Constructor for the Create class.
        Initializes an instance with a default filepath set to None.
        """
        self.filepath = None

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

    def generate_filepath(self, directory=None, ext=".txt"):
        """
        Generate a random filepath for a new file.

        Args:
            directory (str): The directory where the file will be created. If None, uses the user's home directory.
            ext (str): The file extension. Defaults to ".txt".

        Returns:
            str: The generated filepath.
        """
        if directory is None:
            directory = os.path.expanduser("~")

        # Construct the directory, folder name, filename, and full filepath
        self.directory = os.path.join(directory, "")
        self.folder_name = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(12))
        self.filename = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(12)) + ext

        self.filepath = os.path.abspath(os.path.join(self.directory, self.folder_name, self.filename))
        return self.filepath

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
        
    def persistance(self):
        pass