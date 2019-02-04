import os
import shutil
import re

JUPYTER_IMAGES_DIR = 'content/downloads/notebooks/jupyter_images'


def copy_jupyter_images_to_output(dir):
    jupyter_image_dir = re.split('\\\\|\\/|\\/\\/', dir)[-1]

    if not os.path.exists(os.path.join('output', jupyter_image_dir)):
        os.makedirs(os.path.join('output', jupyter_image_dir))

    for file in os.listdir(dir):
        shutil.copy2(os.path.join(dir, file), os.path.join('output', jupyter_image_dir))

copy_jupyter_images_to_output(JUPYTER_IMAGES_DIR)