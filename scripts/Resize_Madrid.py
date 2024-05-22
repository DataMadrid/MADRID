import os
from PIL import Image

def resize_images(image_directory):
    for filename in os.listdir(image_directory):
        img_path = os.path.join(image_directory, filename)
        with Image.open(img_path) as img:
            width, height = img.size
            if width != 224 or height != 224:
                new_img = img.resize((224, 224))
                new_img.save(img_path)
                print(f"Resized image {filename} to 224x224 pixels.")
            else:
                print(f"Image {filename} is already 224x224 pixels.")

# Replace 'path_to_your_images' with the path to your images
resize_images('../')