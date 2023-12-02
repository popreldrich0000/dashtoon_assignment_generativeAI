# dashtoon_assignment_generativeAI
In this assignmnet we will be using the following research paper:
https://arxiv.org/pdf/1602.07188.pdf
This was the original Paper that Introduced Neural Style Learning
I did not entirely copy the paper but introduced some new changes according to the subtleties required by the assignment. 


**Summary**
I first started the assignment by Web scraping and then processing it further for our use.
I Scraped the data from  https://www.mangageko.com/manga/her-summon/
where all the images are made by only 1 artist. And hence I will make an encoder-decoder type CNN for extracting the *style* of the images drawn by the given artist. 





**(!Disclamer- All the data used in this project is only for acadmic purposes and I DO NOT own any of the data!!)**

Data scraping  ⮕  Preprocessing and data cleaning ⮕ Training the style images to extract the Features from them


**Data scraping**

I implemented **scraping.py** script for scraping the data from the site (https://www.mangageko.com/manga/her-summon/). The script automatically Navigates form one Chapter to the next and downloads next 117 chapers and saves them in their respective folders(i.e. chapter1, chapter2 etc)  according to their chapters. 

And this is the structure of the data directory:

Data_raw<br>
|<br>
|_chapter1<br>
|<br>
|_chapter2<br>
..<br>
..<br>
..<br>

**Preprocessing and data cleaning**

Discussed in preprocessing README.md file in Preprocessing folder

In this assignmnet we will be using Autoencoders type of neural network for traing the style images where the input image size will be 400x400 pixels. 

We will have an encoder and then decoder in our design, and we will train our images by the given artist on this model so that it learns the basic structure, layout , Color distribution and texture of the image by the artist.


