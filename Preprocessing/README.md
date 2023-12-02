Here first run **dir.sh** in the termninal by the commands


chmod +x dir.sh  - Giving necessary permissions


./dir.sh - running bash script


it willl create the appropriate directories required for the preprocessing:


cache_dir - used while running the script for storing the file temporarily, 
initially and finally it will be empty 


data_final - final processed images will be stored in this folder ,initially empty


defect_images - images with NULL type size(<5 bytes) will be stored here, initially empty


diff_images - images that are not from same artist or extra images on the site will be stored here ,initially empty


long_images - raw long images will be stored here  same as initial images(so that we don't lose the data), initially empty


raw_data - will contain the raw data chapter wise like given below , extract the given zip here , initially it will not be empty and each chapter folder will contain raw images

raw_data<br>
|<br>
|_chapter1<br>
|<br>
|_chapter2<br>
..<br>
..<br>
..<br>


small_cropped_images - after processing some very small dimension images will be here, these are to be ignored (inititally this will be empty)



white_images - images with more than 50% white space will be here  these are to be ignored( initially empty)


If the images data is small we can furthur manually go through images in small_cropped_images
and white_images folder and find the few useful ones 



then run **run.sh**


chmod +x run.sh  - Giving necessary permissions


./run.sh - running bash script



run correcting_size_ratio.py for resizing the images  to 400x400
This process can also be done using transforms from pytorch but here we are also taking care of the rectangular images by cropping them.

