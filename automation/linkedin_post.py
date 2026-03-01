import webbrowser

def post_to_linkedin():

    repo_link = "https://github.com/shalusingh17/dev-workflow-automation"

    linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={repo_link}"

    print("Opening LinkedIn post window...")

    webbrowser.open(linkedin_url)