# Python code to search for the auto-created folders from the Renesas HEW IDE.
# Once detected, choose the 'delete option' to delete all these folders.

import os, fnmatch

#dir_path = os.path.dirname(os.path.realpath(__file__))

#for root, dirs, files in os.walk(dir_path):
#	for file in files:
#		if file.endswith('dir'):
			#print root+'/'+str(file)

def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below supplied root directory.'''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)