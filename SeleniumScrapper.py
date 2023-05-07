from os import system
from selenium import webdriver
import undetected_chromedriver as uc 
from selenium_stealth import stealth
import random
import re
import codecs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class Scrapper:
    def Setup(Headless=True):
        options = uc.ChromeOptions()
        if(Headless):
            options.add_argument("--headless")
        #options.add_extension(r'C:\Users\Woda\Desktop\Python_Projects\1.48.4_0.crx')
        options.add_argument(r"--load-extension=C:\Users\Woda\Desktop\Python_Projects\1.48.4_0")
        driver = uc.Chrome(options = options)
        #driver = uc.Chrome()
        #driver = webdriver.Chrome(options=options)
        print("Driver ready")
        return driver

    def RemoveAds(AdsFile,ContentString):
        pattern=re.compile(r"\.(?=\S)")
        patterns=[]
        patterns.append(pattern)
        with open(AdsFile,'r') as ADS:
            data = ADS.read().replace('\n','')
            data = data.split(";")
        for Ads in data:
            AdPattern=re.compile(Ads)
            patterns.append(AdPattern)
        for line in patterns:
            content=re.sub(line,'',ContentString)
        return content

    def Scrap(driver,url,XPathButton,XpathContent,
                chapter=1, endchapter=9999, title="Title.txt",
                AdFilePath="AdSnippets.txt"):
        codecs.open(title,'w',"utf-8").close()
        elem_old=0
        driver.get(url)
        driver.implicitly_wait(random.random()+1)
        for i in range(chapter,endchapter):        
            driver.implicitly_wait(random.random()+2)
            try:
                WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,XPathButton))
        )
            except:

                print("Retry clicking link")
                try:
                    WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,XPathButton))
        )
                except:
                    break
            
            
            elem= driver.find_element(By.XPATH,XpathContent).text
            j=0
            while ( elem == elem_old):
                print("Doubling error")
                time.sleep(1)
                elem= driver.find_element(By.XPATH,XpathContent).text
                if(j==5):
                    break
                time.sleep(4)
                j+=1                
            elem_old=elem
            print("chapter"+str(i))
            content = Scrapper.RemoveAds(AdFilePath,elem)
            with codecs.open(title,'a',"utf-8") as book:
                book.writelines(content)
            old_url=driver.current_url
            while(old_url==driver.current_url):
                try:
                    driver.find_element(By.XPATH,XPathButton).click()
                except:
                    print("Trying again")
                    pass
            #driver.get(url)        
        print('Finished on {}'.format(i))
        driver.quit()




