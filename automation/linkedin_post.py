import webbrowser
import urllib.parse

def post_to_linkedin(caption, image_path):

    text = caption
    encoded = urllib.parse.quote(text)

    linkedin_url = f"https://www.linkedin.com/feed/?shareActive=true&text={encoded}"

    webbrowser.open(linkedin_url)

    print("LinkedIn opened. Attach this image manually:", image_path)