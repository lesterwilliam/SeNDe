# Python code to search for the auto-created folders from the Renesas HEW IDE.
# Once detected, choose the 'delete option' to delete all these folders.

import sys
import os

filelist = []


def search_files():
	print("\nThe following directories have been found:\n")
	for root, dirs, files in os.walk("C:/Users/Schwizgebel/Programmieren"):
		for file in files:
			if file.endswith(".txt"):
				filelist.append(file)
				print(os.path.join(root, file))
	print("\n" + str(filelist))

#def get_start_path():
	

def main():
	search_files()

	
main()