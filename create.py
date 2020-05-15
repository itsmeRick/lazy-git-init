import os
import sys
from selenium import webdriver
from github import Github
from dotenv import load_dotenv

load_dotenv()

def startProject():
    folderName = sys.argv[1]
    g = Github(os.getenv('user'), os.getenv('pass'))
    user = g.get_user()
    user.create_repo(str(folderName))
    print("Created repo {}".format(str(folderName)))

if __name__ == "__main__":
    startProject()


