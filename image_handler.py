import os
import shutil

TO_POST = "images/to_post"
POSTED = "images/posted"

def get_next_image():
    files = [f for f in os.listdir(TO_POST) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return os.path.join(TO_POST, files[0]) if files else None

def move_to_posted(image_path):
    filename = os.path.basename(image_path)
    shutil.move(image_path, os.path.join(POSTED, filename))
