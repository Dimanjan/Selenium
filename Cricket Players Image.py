from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib
import argparse
import urllib3, shutil
c = urllib3.PoolManager()

#below is the search term you want to search on google images (first try out manually, which term fetches you more relevant images)
browser = webdriver.Chrome()

folder="batsmenPhotos1"
if not os.path.exists(folder):
    os.mkdir(folder)    
playerList=['J.H. Edrich', 'I.M. Chappell', 'G.S. Chappell', 'K.W.R. Fletcher', 'K.R. Stackpole', 'D.L. Amiss', ' Zaheer Abbas', 'G.M. Turner', 'I.V.A. Richards', 'C.G. Greenidge', ' Javed Miandad', 'D.L. Haynes', 'D.M. Jones', 'S.R. Tendulkar', 'B.C. Lara', 'M.E. Waugh', 'W.J. Cronje', 'G. Kirsten', 'M.G. Bevan', 'S.T. Jayasuriya', 'R.T. Ponting', 'J.H. Kallis', 'A.C. Gilchrist', ' Mohammad Yousuf', 'M.E. Trescothick', 'C.H. Gayle', 'M.L. Hayden', 'R.R. Sarwan', 'G.C. Smith', 'K.P. Pietersen', 'M.E.K. Hussey', 'M.S. Dhoni', 'A.B. de Villiers', 'H.M. Amla', 'V. Kohli', 'D.A. Warner']

counter = 0
succounter = 0 

for player in playerList:
    searchterm= player+" cricket profile photo"

    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    browser.get(url)
    header={'User-Agent':"Chrome/76.0.3809.36"}
     

    
    #for _ in range(5):
        #browser.execute_script("window.scrollBy(0,10)")
    
    a=browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
    print(a[0])
    for x in [a[0]]:
        counter = counter + 1
        print("Total Count:", counter)
        print("Succsessful Count:", succounter)
        print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
        img = json.loads(x.get_attribute('innerHTML'))["ou"]
        imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
        try:
            #path = os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype)
            #urllib.request.urlretrieve(img, path)
            
            
            url=img
                

            filename=folder+"/"+player+".jpg"
            with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
     
                shutil.copyfileobj(res, out_file)   
    

            succounter = succounter + 1
        except:
            print("can't get img")

print(succounter, "pictures succesfully downloaded")
browser.close()
