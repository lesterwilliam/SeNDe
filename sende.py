# Python code designed to search for the auto-created folders from the Renesas HEW IDE.
# Once detected, choose the 'delete option' to delete all these folders.

import sys
import os
import csv

dirlist = []
os.path.start_path = 0

def welcome_msg():
	print("\nThis is -> SEARCH AND DESTROY <-\n")

def search_files():
	print("\nThe following directories have been found:\n")
	#for root, dirs, files in os.walk("C:/Users/Schwizgebel/Programmieren"):
	for root, dirs, files in os.walk(os.path.start_path):
		for dir in dirs:
			if dir.endswith("dir"):
				dirlist.append(dir)
				print("\t" + str(os.path.join(root, dir)))
	print("\n\t" + str(dirlist))

def get_start_path():
	os.path.start_path = input("\tEnter the start path. Leave empty for test structure.\n\t")
	if os.path.start_path == "":
		os.path.start_path = "C:/Users/Schwizgebel/Programmieren"
		print("\tUsing test path: " + str(os.path.start_path))

def check_target():
	print(".")

def export_csv():
	with open('targets.csv', 'w', newline='\n') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(dirlist)
	
def main():
	welcome_msg()
	get_start_path()
	search_files()
	export_csv()

main()