import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from automation.auto_push import push_to_github
from automation.screenshot import take_screenshot
from automation.caption import generate_caption
from automation.linkedin_post import post_to_linkedin


class ChangeHandler(FileSystemEventHandler):

    def __init__(self):
        self.is_running = False

    def on_modified(self, event):

        # Ignore folders
        if event.is_directory:
            return

        # Only trigger for README.md
        if not event.src_path.endswith("README.md"):
            return

        # Prevent multiple triggers
        if self.is_running:
            return

        self.is_running = True

        print("\nREADME modified. Starting automation...\n")

        try:
            # Step 1: Push to GitHub
            push_to_github()

            # Step 2: Take Screenshot
            image_path = take_screenshot()

            # Step 3: Generate Caption
            caption = generate_caption()

            # Step 4: Open LinkedIn
            post_to_linkedin(caption, image_path)

        except Exception as e:
            print("Error during automation:", e)

        # Small delay to avoid loop trigger
        time.sleep(5)

        self.is_running = False


def start_watching():

    path = os.getcwd()

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)

    observer.start()
    print("Watching project for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()