import webbrowser
import urllib.parse

def post_to_linkedin(caption, image_path):

    repo_link = "https://github.com/shalusingh17/dev-workflow-automation"

    text = caption + "\n\n" + repo_link

    encoded = urllib.parse.quote(text)

    linkedin_url = f"https://www.linkedin.com/feed/?shareActive=true&text={encoded}"

    print("Opening LinkedIn post window")

    webbrowser.open(linkedin_url)