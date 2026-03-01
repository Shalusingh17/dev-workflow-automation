from automation.auto_push import push_to_github
from automation.update_readme import update_readme
from automation.linkedin_post import post_to_linkedin


def run_automation():

    print("Starting automation...")

    update_readme()
    push_to_github()
    post_to_linkedin()

    print("Automation completed")


if __name__ == "__main__":
    run_automation()