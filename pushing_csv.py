import subprocess
import os
import time

# path to csv file
repo_path = r"C:\Users\Rise Networks\Desktop\Grant_Tracking_System"

# path to the file to be pushed
file_to_add = "data/grant_data.csv"

# check script's path
os.chdir(repo_path)

# using subprocess to automate the git add and git push
try:
    subprocess.run(["git", "add", file_to_add], check=True)

    # Creating commit message
    commit_message = "Updated the csv file"

    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push to github
    subprocess.run(["git", "push"])
    print("Changes made and updated successfully!")
except subprocess.CalledProcessError as e:
    print("Error adding file: {e}")




