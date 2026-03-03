import random
from datetime import datetime

def generate_caption():

    captions = [

        "Just pushed a small update to my Dev Workflow Automation project. Slowly improving the system that syncs coding work with GitHub and prepares LinkedIn updates automatically.",

        "Another small improvement pushed today. This automation tool helps streamline my development workflow from VS Code to GitHub.",

        "Working on a developer workflow automation project. Just pushed a new update improving the automation pipeline.",

        "Continuing to build my Dev Workflow Automation tool. Today's update focuses on improving the GitHub integration."
    ]

    caption = random.choice(captions)

    hashtags = "\n\n#Python #Automation #GitHub #Developer"

    return f"{caption}\n\nUpdated: {datetime.now().strftime('%Y-%m-%d %H:%M')}{hashtags}"