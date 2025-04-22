import os

def convert_to_gitbook_readme(base_path):
    for root, dirs, files in os.walk(base_path):
        for d in dirs:
            folder_path = os.path.join(root, d)
            md_path = os.path.join(root, f"{d}.md")
            readme_path = os.path.join(folder_path, "README.md")

            if os.path.isfile(md_path):
                print(f"Moving {md_path} → {readme_path}")
                os.rename(md_path, readme_path)

if __name__ == "__main__":
    convert_to_gitbook_readme("_build")

