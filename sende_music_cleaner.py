# Python code designed to search for the auto-created folders from the Renesas HEW IDE.
# Once detected, choose the 'delete option' to delete all these folders.

import sys
import os
import csv
from datetime import datetime
import shutil
import glob

folderlist = []
dirlist = []
os.path.start_path = 0

def welcome_msg():
	print("\nThis is -> SEARCH AND DESTROY <-\n")

def get_time():
	t = datetime.now()
	return t.strftime('%d-%m-%y %H-%M')

def get_size(start_path = '.'):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
	return total_size

def search_files():
	saved_space = 0
	print("\nThe following directories have been found:\n")
	for root, dirs, files in os.walk(os.path.start_path):
		for dir in dirs:
			if dir.endswith("Artwork"):
				folderlist.append(dir)
				dirlist.append(str(os.path.join(root, dir)))
				saved_space += get_size(str(os.path.join(root, dir)))
				print("\t" + str(os.path.join(root, dir)))
	print("\n\t" + str(folderlist))
	return saved_space

def search_and_destroy_file():
	print("Start")
	
	for root, dirs, files in os.walk("s:/New music/"):
		for file in files:
			if file.endswith(".m3u") or file.endswith(".DS_Store") or file.endswith(".pls") or file.endswith(".dat") or file.endswith(".mp4") or file.endswith(".bmp") or file.endswith(".cue") or file.endswith(".accurip") or file.endswith(".wma") or file.endswith(".jpeg") or file.endswith(".m3u8") or file.endswith(".JPG") or file.endswith(".CUE") or file.endswith(".LOG") or file.endswith("Thumbs.db"):
				print(os.path.join(root, file))
				os.remove(os.path.join(root, file))

def get_start_path():
	os.path.start_path = input("\tEnter the start path. Leave empty for test structure.\n\t")
	if os.path.start_path == "":
		os.path.start_path = "C:/Users/Schwizgebel/Programmieren"
		print("\tUsing test path: " + str(os.path.start_path))

def check_target():
	print(".")

def export_csv(input):
	with open(str("logs/targets-" + str(get_time()) + ".csv"), 'w', newline='\n') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow("Directory: " + str(os.path.start_path))
		csvwriter.writerow(folderlist)
	
def export_txt(input):
	with open(str("logs/targets-" + str(get_time()) + ".txt"), "w") as dir_file:
		dir_file.write("Freeable space: " + str(input) + " byte\n")
		for item in dirlist:
			dir_file.write("%s\n" % item)

def delete():
	if input("Do you want to delete all directories? (y/n):\n") == "y":
		for item in dirlist:
			shutil.rmtree(item, ignore_errors=True)

def main():
	#welcome_msg()
	#get_start_path()
	#availabel_space = search_files()
	#export_csv(availabel_space)
	#export_txt(availabel_space)
	#delete()
	search_and_destroy_file()

main()