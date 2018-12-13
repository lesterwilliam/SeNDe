# Python code designed to search for the auto-created folders from the Renesas HEW IDE.
# Once detected, choose the 'delete option' to delete all these folders.

import sys
import os
import csv
from datetime import datetime

folderlist = []
dirlist = []
os.path.start_path = 0

def welcome_msg():
	print("\nThis is -> SEARCH AND DESTROY <-\n")

def get_time():
	t = datetime.now()
	return t.strftime('%d-%m-%y %H%M')

def search_files():
	print("\nThe following directories have been found:\n")
	for root, dirs, files in os.walk(os.path.start_path):
		for dir in dirs:
			if dir.endswith("dir"):
				folderlist.append(dir)
				dirlist.append(str(os.path.join(root, dir)))
				print("\t" + str(os.path.join(root, dir)))
	print("\n\t" + str(folderlist))

def get_start_path():
	os.path.start_path = input("\tEnter the start path. Leave empty for test structure.\n\t")
	if os.path.start_path == "":
		os.path.start_path = "C:/Users/Schwizgebel/Programmieren"
		print("\tUsing test path: " + str(os.path.start_path))

def check_target():
	print(".")

def export_csv():
	with open(str("logs/targets-" + str(get_time()) + ".csv"), 'w', newline='\n') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow("Directory: " + str(os.path.start_path))
		csvwriter.writerow(folderlist)
	
def export_txt():
	with open(str("logs/targets-" + str(get_time()) + ".txt"), "w") as dir_file:
		for item in dirlist:
			dir_file.write("%s\n" % item)

def main():
	welcome_msg()
	get_start_path()
	search_files()
	export_csv()
	export_txt()

main()