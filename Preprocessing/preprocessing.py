from PIL import Image
import argparse
import os
import shutil
from crop_img import crp,cut_paste
import cv2
import numpy as np
def get_image_dimensions(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return True,width, height
    except Exception as e:
        print(f"Error: {e}")
        return False,None,None

def get_images_name_list(directory):
    return [f for f in os.listdir(directory)]

def get_image_size(file_path):
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        print(f"Error: {e}")
        return None

    

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('Folder_name', help='Path to the input file.')
    args = parser.parse_args()
    Folder_name = args.Folder_name
    curr_dir = os.getcwd()
    folder_path =  curr_dir +  "/raw_data/" + Folder_name
    images_names = get_images_name_list(folder_path)
    defect_folder_path = curr_dir + "/" + "defect_images" + "/"
    white_images_path = curr_dir + "/" + "white_images" + "/"
    diff_images = curr_dir + "/" + "diff_images" + "/"
    data_folder_path = curr_dir + "/" + "data_final" + "/"
    long_img_folder_path = curr_dir + "/" + "long_images" + "/"
    small_cropped_imgs = curr_dir + "/" + "small_cropped_images" + "/"
    cache_dir_path = curr_dir + "/" + "cache_dir" + "/"

    defect_folder_max = [0]
    white_images_max = [0]
    diff_images_max = [0]
    data_folder_path_max = [0]
    long_img_folder_path_max = [0]
    # print(images_names)

    for img in images_names:
        # print(img)
        image_path = folder_path+img
        try:
            image_size = get_image_size(image_path)
            dimensions = get_image_dimensions(image_path)
        except :
            os.remove(image_path)
            continue

        if (image_size == None or image_size<5):
            cut_paste(image_path,defect_folder_path,defect_folder_max,cache_dir_path)
            continue
        
        
        if dimensions[1]<700:
            cut_paste(image_path,diff_images,diff_images_max,cache_dir_path)
            continue
            
        if(dimensions[2]<1000):
            white_threshold = 250
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            wt = np.sum(gray > white_threshold) > (gray.shape[0]*gray.shape[1])/2

            if wt:
                cut_paste(image_path,white_images_path,white_images_max,cache_dir_path)
            else:
                cut_paste(image_path,data_folder_path,data_folder_path_max,cache_dir_path)
        else:
            # print("here")
            crp(image_path,data_folder_path,white_images_path,long_img_folder_path,Folder_name,img,small_cropped_imgs,long_img_folder_path_max,cache_dir_path)
if __name__ == '__main__':
    main()
