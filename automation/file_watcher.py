import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from automation.auto_push import push_to_github
from automation.screenshot import take_screenshot
from automation.linkedin_post import post_to_linkedin
from automation.caption import generate_caption


class ChangeHandler(FileSystemEventHandler):

    ddef on_modified(self, event):

    if event.is_directory:
        return

    # Only trigger if README.md changed
    if "README.md" not in event.src_path:
        return

    print("README modified. Running automation...")

    push_to_github()

    image_path = take_screenshot()

    caption = generate_caption()

    post_to_linkedin(caption, image_path)