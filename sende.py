# Python code to search for the auto-created folders from the Renesas HEW IDE.
# Once detected, choose the 'delete option' to delete all these folders.

import os

filelist = []

def search_files():
	print("The following directories have been found.:")
	for root, dirs, files in os.walk("C:/Users/Schwizgebel/Programmieren/SeNDe"):
		for file in files:
			if file.endswith(".txt"):
				filelist.append(file)
				print(os.path.join(root, file))

def main():
	search_files()
	#print(filelist)

main()