import cv2
import numpy as np
import os
import shutil

def cut_paste(source, final_dir,max_num,cache_dir_path):
    
    file_name = os.path.basename(source)
    file_no_ext, _ = os.path.splitext(source)
    destination_path = os.path.join(final_dir, file_name)
    count = max_num[0]
    new_name = file_name
    # if there is a file with same name in the folder then rename it again and again till there is no
    # other file with same name
    while os.path.exists(destination_path):
        new_name = f"new_{count}.jpg"
        destination_path = os.path.join(final_dir, new_name)
        count += 1
    if(max_num[0]<count):
        max_num[0] = count

    cache_dir_filepath = os.path.join(cache_dir_path,file_name)    
    new_name_source = os.path.join(cache_dir_filepath[:-len(file_name)],new_name)
    # print("newname")
    # print(new_name_source , source)
    # print("end")
    shutil.move(source, cache_dir_path)
    os.rename(cache_dir_filepath, new_name_source)
    shutil.move(new_name_source, final_dir)
def crp(image_path,data_folder_path,white_images_path,long_img_folder_path,chapter_name,img_name,small_cropped_imgs_path,long_img_folder_path_max,cache_dir_path):
    # print("here too")
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    path = "/media/eldrich-rikaze/New Volume/Style_transfer_assignment/Scratch__NN/data_final/"
    for i, contour in enumerate(contours):
        
        x, y, w, h = cv2.boundingRect(contour)
        roi = image[y:y+h, x:x+w]
        gray_roi = gray[y:y+h, x:x+w]
        # total_pixels = gray_roi.size
        # white_threshold = 200
        # white_pixels = cv2.countNonZero(gray_roi > white_threshold)
        # percentage_white = (white_pixels / total_pixels) * 100
        white_threshold = 250
        wt = np.sum(gray_roi > white_threshold) > (gray_roi.shape[0]*gray_roi.shape[1])/2

        if wt:
            # print("white Image found")
            # print(os.path.join(white_images_path, img_name+chapter_name+f"_{i}.jpg"))
            cv2.imwrite(os.path.join(white_images_path, img_name+chapter_name[:-1]+f"_{i}.jpg"), roi)
            continue
        mp = h // 2
        trp1 = h // 3
        trp2 = 2*h // 3
        no_ext_name,_ = os.path.splitext(img_name)
        

        if w >= 700 and h >= 300: 
            name =  no_ext_name[0]+chapter_name[:-1]+f"_{i}.jpg"
            if h < 1200:
                cv2.imwrite(os.path.join("a"+data_folder_path,name), roi)            
            elif h <2000:
                image[:mp, :, :]
                cv2.imwrite(os.path.join(data_folder_path,"a"+name), roi[:mp, :, :])
                cv2.imwrite(os.path.join(data_folder_path,"b"+name), roi[mp:, :, :])

            else:
                cv2.imwrite(os.path.join(data_folder_path,"a"+name), roi[:trp1, :, :])
                cv2.imwrite(os.path.join(data_folder_path,"b"+name), roi[trp1:trp2, :, :])
                cv2.imwrite(os.path.join(data_folder_path,"c"+name), roi[trp2:, :, :])
            # print(str(os.path.join(data_folder_path, no_ext_name+chapter_name[:-1]+f"_{i}.jpg")))
            # print(roi.shape)
            # name =  no_ext_name[0]+chapter_name[:-1]+f"_{i}.jpg"
            # print(no_ext_name[0]+chapter_name+f"_{i}.jpg")
            # name = f"qwertyuiopasdf_{i}.jpg"
            # print(name)
            # print(type(roi))
            # os.path.join(data_folder_path+name)
            # string = f"output_{i}.jpg"
            # string = os.path.join(data_folder_path+name)
            # cv2.imwrite(string,roi)      
            # cv2.imwrite(os.path.join(data_folder_path,name), roi) 
            # cv2.imwrite(os.path.join(path+f"_{i}.jpg"), roi)
        elif w >= 100 and h >= 100:
            cv2.imwrite(os.path.join(small_cropped_imgs_path, no_ext_name[0]+chapter_name[:-1]+f"_{i}.jpg"), roi)
            
    cut_paste(image_path,long_img_folder_path,long_img_folder_path_max,cache_dir_path)

# curr_dir = os.getcwd()
# image_path="/media/eldrich-rikaze/New Volume/Style_transfer_assignment/Scratch__NN/raw_data/chapter1/3.jpg"
# data_folder_path= curr_dir + "/" + "data_final" + "/"
# white_images_path=curr_dir + "/" + "white_images" + "/"
# long_img_folder_path=curr_dir + "/" + "long_images" + "/"
# Folder_name = "chapter1/"
# img = "3.jpg"
# small_cropped_imgs=curr_dir + "/" + "small_cropped_images" + "/"
# long_img_folder_path_max=[0]
# cache_dir_path=curr_dir + "/" + "cache_dir" + "/"
# print(data_folder_path)
# crp(image_path,data_folder_path,white_images_path,long_img_folder_path,Folder_name,img,small_cropped_imgs,long_img_folder_path_max,cache_dir_path)
