# Python code to search for the auto-created folders from the Renesas HEW IDE.
# Once detected, choose the 'delete option' to delete all these folders.

import os
for root, dirs, files in os.walk("C:/Users/Schwizgebel/Programmieren"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))