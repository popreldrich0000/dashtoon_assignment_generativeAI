from PIL import Image
import cv2
from preprocessing import get_images_name_list,get_image_dimensions
import numpy as np




def check_white(image):
        image = np.array(image)
        white_threshold = 250
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        wt = np.sum(gray > white_threshold) > (gray.shape[0]*gray.shape[1])/2
        return wt
        
image_dir_path = "/media/eldrich-rikaze/New Volume/Style_transfer_assignment/Scratch__NN/data_final/"
img_name_list = get_images_name_list(image_dir_path)
final_dir = "/media/eldrich-rikaze/New Volume/Style_transfer_assignment/Scratch__NN/resized_images"

for name in img_name_list:
    img_path = image_dir_path + name
    dimensions = get_image_dimensions(img_path)
    image = Image.open(img_path)
    
    if(dimensions[1]<dimensions[2]/2):
        mid_ver = dimensions[2]//2
        upper_half = image.crop((0, 0, dimensions[1], mid_ver))
        lower_half = image.crop((0,mid_ver , dimensions[1], dimensions[2]))
        if check_white(upper_half):
            resized_image = image.resize((400, 400))
            resized_image.save(f"{final_dir}/{name[:-4]}_up.jpg")

        if check_white(lower_half):
            resized_image = image.resize((400, 400))
            resized_image.save(f"{final_dir}/{name[:-4]}_down.jpg")
        
        continue
    if(dimensions[2]<dimensions[1]/2):
        mid_across = dimensions[1]//2
        left_half = image.crop((0, 0, mid_across, dimensions[2]))
        right_half = image.crop((mid_across, 0, dimensions[1], dimensions[2]))
        if check_white(left_half):
            resized_image = image.resize((400, 400))
            resized_image.save(f"{final_dir}/{name[:-4]}_left.jpg")

        if check_white(right_half):
            resized_image = image.resize((400, 400))
            resized_image.save(f"{final_dir}/{name[:-4]}_right.jpg")
        continue
    resized_image = image.resize((400, 400))
    resized_image.save(f"{final_dir}/{name[:-4]}.jpg")   


