from datetime import datetime

def update_readme():

    content = f"""
# Dev Workflow Automation

This project automatically pushes code to GitHub and posts updates to LinkedIn.

## Last Update
{datetime.now()}

## Features
- Auto GitHub Push
- Auto README Update
- LinkedIn Update Automation

## Tech Stack
Python
Git
Automation
"""

    with open("README.md", "w") as file:
        file.write(content)

    print("README updated")