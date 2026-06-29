import os

def load_captions (captions_folder, image_folder):
    captions = {}
    image_files = os.listdir(image_folder)

    for image_file in image_files:
        image_name = image_file.split(".")[0]
        caption_file = os.path.join(captions_folder, image_name + ".txt")

        with open(caption_file, "r") as f:
            caption = f.readlines()[0].strip()

        if image_name not in captions:
            captions[image_name] = caption

    return captions