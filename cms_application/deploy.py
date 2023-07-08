```python
import os
import subprocess

def deploy_website(website):
    # Ensure the website directory exists
    if not os.path.exists(website.directory):
        raise Exception(f"Website directory {website.directory} does not exist")

    # Change to the website directory
    os.chdir(website.directory)

    # Initialize git if it hasn't been already
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])

    # Add all files to git
    subprocess.run(["git", "add", "-A"])

    # Commit the changes
    subprocess.run(["git", "commit", "-m", f"Deploying {website.name}"])

    # Push the changes to Cloudflare Pages
    subprocess.run(["git", "push", "origin", "main"])

    print(f"Website {website.name} has been deployed to Cloudflare Pages")
```