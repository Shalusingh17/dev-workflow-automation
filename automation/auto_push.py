import os

def push_to_github():

    print("Pushing code to GitHub...")

    os.system("git add .")
    os.system('git commit -m "Auto update from VS Code work"')
    os.system("git push")

    print("GitHub push completed")