#Integrate frame images into video
import os
import cv2
from PIL import Image


def image_to_video(image_path, media_path):
    # get all image names from image_path
    image_names = os.listdir(image_path)
    # sort the image names
    image_names.sort(key=lambda n: int(n[:-4]))
    # set format
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # set fps
    fps = 60
    # get image size(all images have the same size)
    image = Image.open(image_path + image_names[0])
    # init writer
    media_writer = cv2.VideoWriter(media_path, fourcc, fps, image.size)
    # add image to vedio
    for image_name in image_names:
        im = cv2.imread(os.path.join(image_path, image_name))
        media_writer.write(im)
        print(image_name, 'Merge Completed!')
    # Release and write vedio
    media_writer.release()
    print('Silent video writing completed!')

# image_path
image_path =  "C:/tmp/"
# save_path
media_path = "res_01.mp4"
# call function
image_to_video(image_path, media_path)
