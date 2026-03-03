import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from automation.auto_push import push_to_github
from automation.screenshot import take_screenshot
from automation.linkedin_post import post_to_linkedin
from automation.caption import generate_caption


class ChangeHandler(FileSystemEventHandler):

    def on_modified(self, event):

        if event.is_directory:
            return

        print("File saved — running automation")

        push_to_github()

        screenshot = take_screenshot()

        caption = generate_caption()

        post_to_linkedin(caption, screenshot)


def start_watching():

    path = "."
    event_handler = ChangeHandler()
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Watching project for changes...")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()