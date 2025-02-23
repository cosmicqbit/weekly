import os
from datetime import datetime
import shutil

# Directory paths
docs_dir = "docs"
posts_dir = "site/content/posts"

# Function to generate front matter
def generate_front_matter(file_name):
    # Generate title by converting the file name to a human-readable format
    title = file_name.replace("-", " ").replace(".md", "").title()

    # Generate current date in Hugo-compatible format (YYYY-MM-DD)
    date = datetime.now().strftime("%Y-%m-%d")

    # Define other metadata
    author = "Li"
    description = f"This is the content for {title}"
    tags = ["weekly", "issue"]

    # Create front matter in TOML format
    front_matter = (
        f"+++\n"
        f"title = \"{title}\"\n"
        f"date = \"{date}\"\n"
        f"author = \"{author}\"\n"
        f"description = \"{description}\"\n"
        f"tags = {tags}\n"
        f"+++\n"
    )
    return front_matter

# Ensure the posts directory exists
os.makedirs(posts_dir, exist_ok=True)

# Process all Markdown files in the docs directory
for file_name in os.listdir(docs_dir):
    if file_name.endswith(".md"):
        docs_file_path = os.path.join(docs_dir, file_name)
        posts_file_path = os.path.join(posts_dir, file_name)

        # Read the file content
        with open(docs_file_path, "r") as file:
            content = file.read()

        # Check if front matter already exists
        if content.strip().startswith("+++"):
            print(f"Front matter already exists for {file_name}. Skipping.")
            continue

        # Generate front matter and prepend it to the content
        front_matter = generate_front_matter(file_name)
        updated_content = front_matter + "\n" + content

        # Write the updated content to the posts directory
        with open(posts_file_path, "w") as file:
            file.write(updated_content)

        print(f"Processed and copied {file_name} to {posts_dir}.")
