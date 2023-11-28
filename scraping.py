import requests
from bs4 import BeautifulSoup
import os

def data_download_site(url , folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass    
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_links = soup.find_all('a')

    # print(next_link)
    for item in all_links:
        try:
            if(item["title"][:9]=="Chapter 2"):
                next_link = "https://www.mangageko.com/"+item["href"]
        except:
            pass    
    images = soup.find_all('img')
    i = 0

    for image in images:
        link = image['src']
        with open(str(i)+ '.jpg' , 'wb') as f:
            try:
                img = requests.get(link)    
                f.write(img.content)
            except Exception as err:
                print(link , " error for this link " , err)
            
        i = i + 1      
    os.chdir("/media/eldrich-rikaze/New Volume/Style_transfer_assignment/Scratch__NN")
    

def main():
    url_s = 'https://www.mangageko.com/reader/en/her-summon-chapter-'  
    url_e = '-eng-li/'
    for i in range(95,118,1):
        print("downloading Chapter :" , i)  
        url = url_s + str(i) + url_e
        data_download_site(url , "chapter"+str(i))
        
if __name__=="__main__":
    main()
# def data_download_google(url , folder, num_images ):
