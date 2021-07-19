# Import Libraries
import os
from pathlib import Path

# Get current working directory
pwd = os.getcwd()

# Make root README.md file and gitignore file
Path(pwd+'/README.md').touch(mode=0o666, exist_ok=True)
Path(pwd+'/.gitignore').touch(mode=0o666, exist_ok=True)

# loop 100 times
for dayNum in range(1, 101):
    # make a new folder for each loop
    Path(pwd+'/Day_'+str(dayNum)).mkdir(parents=True, exist_ok=True)

    # get the new folder path
    done = pwd+'/Day_'+str(dayNum)

    # Make required files and folder
    Path(done+'/Twitter_Upload').mkdir(mode=0o777, parents=False, exist_ok=False)
    Path(done+'/main.py').touch(mode=0o666, exist_ok=True)
    Path(done+'/README.md').touch(mode=0o666, exist_ok=True)

# Ignore all the folders from git history
f = open('.gitignore', 'w')

for _ in range(1, 101):
    f.write('Day_'+str(_)+'/\n')

f.close()
