import webbrowser
import time
import pyperclip


def post_to_linkedin(caption, image_path):

    print("\nPreparing LinkedIn post...\n")

    # Copy caption to clipboard automatically
    pyperclip.copy(caption)

    print("Caption copied to clipboard ✅")

    # Open LinkedIn feed
    webbrowser.open("https://www.linkedin.com/feed/")

    time.sleep(5)

    print("\n================ ACTION REQUIRED ================\n")
    print("1️⃣ Click 'Start a post'")
    print("2️⃣ Press CTRL + V (caption already copied)")
    print("3️⃣ Attach this image:", image_path)
    print("4️⃣ Click Post 🚀")
    print("\n=================================================\n")