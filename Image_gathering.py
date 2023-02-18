from inspect import _void
from multiprocessing.sharedctypes import Value
from tkinter.ttk import Style
from traceback import print_tb
from xml.etree.ElementInclude import include
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from urllib.error import HTTPError
from flask import Flask, render_template, request
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict
from selenium import webdriver  # you need to download chrome.exe and the chromedriver.exe , otherwise you have to modify the code
from bs4 import BeautifulSoup
from PIL import Image
from time import time, ctime
from bs4 import BeautifulSoup,Comment
from threading import Thread
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from ecosia_images import crawler
from random import seed
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as BSHTML
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bing_image_downloader import downloader
from urllib.request import urlopen
from bs4 import BeautifulSoup
from google_images_download import google_images_download   #importing the library
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL.Image import core as image
from selenium.webdriver.common.keys import Keys
from icrawler.builtin import BaiduImageCrawler
from PIL import Image
from icrawler.builtin import GoogleImageCrawler
from urllib import error
from urllib import parse #Parsing, merging, encoding, decoding for URLs
from icrawler.builtin import BaiduImageCrawler
from BaiduImagesDownload import Crawler
from lxml import html
import glob, os
from selenium.webdriver.common.keys import Keys
from os import environ, wait
from urllib.parse import quote
from multiprocessing import Pool
from user_agent import generate_user_agent
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from google_images_download import google_images_download   #importing the library
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
from icrawler.builtin import GreedyImageCrawler
from sys import exit
from io import StringIO
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
import datetime
from imgdl import download
import cgi, time, csv, requests, os, sys, json, re, shutil
import flickr_api
import urllib, urllib.error, urllib.request
import urllib.request as r
import os, flickrapi, sys, subprocess, shutil, six, twitter, numpy, wget, requests, pickle

app = Flask(__name__)


#0-Index✅
@app.route('/')
def index():
    return render_template('index.html')
    
#Selenium Download funktion ✅
def download_url(file_url, output_dir, key_, current_numb, source):
    try:
    #Get url ine
        file_name_start_pos = file_url.rfind("/") + 1
        file_name = file_url[file_name_start_pos:]
        ts = time.time()
        today = date.today()
        err_count = 0



        #Navigate to output_dir
        file_path = os.path.realpath(__file__)
        output_files = file_path.replace('Image_gathering.py',str(output_dir))
        os.chdir(output_files)

        #Create new folder
        new_folder = str(key_)+"_"+str(today)
        path = os.path.join(output_files, new_folder)
        r = requests.get(file_url, stream=True)

        #Navigate to folder
        if not os.path.exists(path):
            os.makedirs(path)
        elif os.path.exists(path):
            os.chdir(path)

        #Write image to folder
        if r.status_code == requests.codes.ok:
            with open(file_name, 'wb') as f:
                for data in r:
                    f.write(data)
            os.rename(file_name,"ImageSearch="+str(key_)+"_Nr="+str(current_numb-1)+"_From="+str(source)+"_"+str(today)+".png")

    except Exception as e:
        s = str(e)
        print("\n"+str(s)+"\n")




    #End
    return "success"

#1-Baidu✅
@app.route('/Baidu', methods=['GET', 'POST'])
def Baidu():

    #Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/10: Resetting Baidu_urls.txt"+"\n")
    f = open("URLS/Baidu_urls.txt", "w")
    f.write("")
    f.close()
    
    #Variables
    print("2/10: Get search requirements"+"\n")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    output_dir = 'Images/Baidu_pics'
    
    #Driver
    print("3/10: Start driver"+"\n")
    url = "https://image.baidu.com"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(1)
    
    #Search
    print("4/10: Create search"+"\n")
    driver.find_element(By.CSS_SELECTOR, '#kw').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(str(key_))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.RETURN)
    time.sleep(1)
    
    #Scroll down
    print("5/10: Scrolling down to load image urls"+"\n")
    SCROLL_PAUSE_TIME = 10
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(SCROLL_PAUSE_TIME)
        total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#imgid > div > ul > li'))
        print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")
        if new_height == last_height:
            print("--- No more room to scroll ---")
            break
        last_height = new_height
        #Test
        #if total_pictures > 25:
        #    break
        
    #Total image count
    print("6/10: Get total image count"+"\n")
    total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#imgid > div > ul > li'))
    print("- There are "+str(total_pictures)+" pictures available"+"\n")
    time.sleep(1)
    
    #Get Image urls
    print("7/10: Write image url to Baidu_urls.txt"+"\n")
    find_href = driver.find_elements(By.CSS_SELECTOR, '#imgid > div > ul > li > div > div.imgbox-border > a > img')
    with open("URLS/Baidu_urls.txt", "a+") as textFile:
        for my_href in find_href:
            textFile.write(str(my_href.get_attribute("src"))+".png" + "\n")

    # Insert into List with image urls
    print("8/10: Write image url to Every_url.txt"+"\n")
    with open("URLS/Every_url.txt", "a+") as textFile:
        for my_href in find_href:
            textFile.write(str(my_href.get_attribute("src"))+".png" + "\n")
    
    #Download function 
    print("9/10: Downloading image from Baidu_urls.txt"+"\n")
    with open("URLS/Baidu_urls.txt", "r") as urls:
        for idx, url in enumerate(urls.readlines()):
            url = url.rstrip("\n")
            print("- Downoading image #"+str(idx+1)+" out of "+str(total_pictures)+" images")
            download_url(url, output_dir, key_)

    #End
    print("\n"+"10/10: Finish downloading "+str(total_pictures)+" images from Baidu to "+str(output_dir)+"\n")
    print("--- If you did not get all the images, try adjusting SCROLL_PAUSE_TIME ---"+"\n")
    return str("Success")

#2-Becovi ✅✅✅✅✅✅✅✅✅✅
@app.route('/Becovi', methods=['GET', 'POST']) 
def Becovi():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting Becovi_urls.txt"+"\n")
    f = open("URLS/Becovi_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Becovi_pics'
    SCROLL_PAUSE_TIME = 10
    source = "search.becovi.com"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    url = "https://search.becovi.com/serp.php?q="+str(key_)+"&i=NYCZV1CQ1T&atr=&s="
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)
    print("- Insert search requirements into brwoser"+"\n")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div.header > div:nth-child(2) > div > div > ul > li:nth-child(2) > a").click()
    #Scroll down and click show more
    print("4/7: Scrolling down to load image urls"+"\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'img'))

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("--- No more room to scroll ---"+"\n")
                break
            last_height = new_height
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")
            time.sleep(SCROLL_PAUSE_TIME)
  
    print("5/7: Writing metadata")
    page_length = 1
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        find_href = driver.find_elements(By.CSS_SELECTOR, '#images > div > a > img')
        time.sleep(2)

        with open("URLS/Becovi_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Becovi_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 2:
            break


    print("6/7: Downloading image from Becovi_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Becovi_urls.txt', 'r') as urls:       
        file = open("URLS/Becovi_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Becovi_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from Becovi to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")

#3-Bing✅
@app.route('/Bing', methods=['GET', 'POST'])
def Bing():

    #Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/11: Resetting Bing_urls.txt"+"\n")
    f = open("URLS/Bing_urls.txt", "w")
    f.write("")
    f.close()

    #Variables
    print("2/11: Get search requirements"+"\n")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    output_dir = 'Images/Bing_pics'
    
    #Driver
    print("3/11: Start driver"+"\n")
    url = "https://www.bing.com/?scope=images&nr=1&FORM=NOFORM"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)

    #Accept coockies
    print("4/11: Accept cookies"+"\n")
    element = driver.find_element(By.CSS_SELECTOR, '#bnp_btn_accept')
    if element.is_displayed():
        driver.find_element(By.CSS_SELECTOR, '#bnp_btn_accept').click()
        print("- Cookies found"+"\n")
    else:
        print("- Cookies not found"+"\n")
    time.sleep(2)

    #Create search
    print("5/11: Create search"+"\n")
    driver.find_element(By.CSS_SELECTOR, '#sb_form_q').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#sb_form_q').send_keys(str(key_))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#sb_form_q').send_keys(Keys.RETURN)
    time.sleep(1)

    #Scroll down
    print("6/11: Scrolling down to load image urls"+"\n")
    SCROLL_PAUSE_TIME = 6
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(SCROLL_PAUSE_TIME)
        total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '.mimg'))
        print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

        if new_height == last_height:
            print("--- No more room to scroll ---")
            break
        last_height = new_height
        #Test
        #if total_pictures > 25:
        #    break
    
    #Total image count
    print("7/11: Get total image count"+"\n")
    total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '.mimg'))
    print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")
    time.sleep(1)
    
    #Get Image urls
    print("8/11: Write image url to Bing_urls.txt"+"\n")
    find_href = driver.find_elements(By.CSS_SELECTOR, '.iusc')
    with open("URLS/Bing_urls.txt", "a+") as textFile:
        for idx, my_href in enumerate(find_href):
            print(my_href)
            attb = str(my_href.get_attribute("m"))
            x = int(attb.find("murl"))+7
            y = int(attb.find('","turl"'))
            sliced = attb[x:y]
            start = 0
            stop = len(sliced)
            print(str(idx)+" ___ "+str(sliced))

            if ".jpg" or ".png" or ".JPG" or ".PNG" in sliced:
                textFile.write(str(sliced)+"\n")
            elif ".jpg" or ".png" or ".JPG" or ".PNG" not in sliced:
                print("pass - elif 1"+str(idx))
            elif not ".jpg" or ".png" or ".JPG" or ".PNG" in sliced:
                print("pass - elif 2 "+str(idx))
            else:
                print("pass - else "+str(idx))



    # Insert into List with image urls
    print("9/11: Write image url to Every_url.txt"+"\n")
    with open("URLS/Every_url.txt", "a+") as textFile:
        for my_href in find_href:
            textFile.write(str(my_href.get_attribute("src"))+".png" + "\n")
    
    #Download function 
    print("10/11: Downloading image from Bing_urls.txt"+"\n")
    with open("URLS/Bing_urls.txt", "r") as urls:
        for idx, url in enumerate(urls.readlines()):
            url = url.rstrip("\n")
            print("- Downoading image #"+str(idx+1)+" out of "+str(total_pictures)+" images")
            download_url(url, output_dir, key_)

    #End
    print("\n"+"11/11: Finish downloading "+str(total_pictures)+" images from Bing to "+str(output_dir)+"\n")
    print("--- If you did not get all the images, try adjusting SCROLL_PAUSE_TIME ---"+"\n")
    return str("Success")

#4-Brave✅
@app.route('/Brave', methods=['GET', 'POST'])
def Brave():

    #Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/9: Resetting Brave_urls.txt"+"\n")
    f = open("URLS/Brave_urls.txt", "w")
    f.write("")
    f.close()

    #Variables
    print("2/9: Get search requirements"+"\n")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    output_dir = 'Images/Brave_pics'

        #Driver
    print("3/9: Start driver"+"\n")
    url = "https://search.brave.com/images?q="+str(key_)
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)

    #Scroll down and click show more
    print("4/9: Scrolling down to load image urls"+"\n")
    SCROLL_PAUSE_TIME = 6
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        driver.find_element(By.CSS_SELECTOR, '#show-more-btn').click()
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'div > div > img'))
        print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")
        if new_height == last_height:
            print("--- No more room to scroll ---")
            break
        last_height = new_height
        #Test
        #if total_pictures > 25:
        #    break
    
    #Total image count
    print("5/9: Get total image count"+"\n")
    total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'div > div > img'))
    print("- There are "+str(total_pictures)+" pictures available"+"\n")
    time.sleep(1)
    
    #Get Image urls
    print("6/9: Write image url to Brave_urls.txt"+"\n")
    find_href = driver.find_elements(By.CSS_SELECTOR, 'div > div > img')
    with open("URLS/Brave_urls.txt", "a+") as textFile:
        for idx, my_href in enumerate(find_href):
            sliced = str(my_href.get_attribute("src"))
            textFile.write(str(sliced)+"\n")

    # Insert into List with image urls
    print("7/9: Write image url to Every_url.txt"+"\n")
    with open("URLS/Every_url.txt", "a+") as textFile:
        for my_href in find_href:
            textFile.write(str(my_href.get_attribute("src"))+"\n")

    #Download function 
    print("8/9 Downloading image from Brave_urls.txt"+"\n")
    with open("URLS/Brave_urls.txt", "r") as urls:
        for idx, url in enumerate(urls.readlines()):
            url = url.rstrip("\n")
            print("- Downoading image #"+str(idx+1)+" out of "+str(total_pictures)+" images")
            download_url(url, output_dir, key_)

    #End
    print("\n"+"9/9: Finish downloading "+str(total_pictures)+" images from Brave to "+str(output_dir)+"\n")
    print("--- If you did not get all the images, try adjusting SCROLL_PAUSE_TIME ---"+"\n")
    return str("Success")
    
#5*-DreamsTime 
@app.route('/DreamsTime', methods=['GET', 'POST']) 
def DreamsTime():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting DreamsTime_urls.txt"+"\n")
    f = open("URLS/DreamsTime_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/DreamsTime_pics'
    SCROLL_PAUSE_TIME = 10
    source = "dreamstime.com"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    #tip 1
    url = "https://www.dreamstime.com/"
    chrome_path = 'chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(10)
    
    #Boot check
    try:
        element_a = driver.find_element((By.XPATH, "//*[contains(text(),'Hold nede')]"))
        print(str(element_a))
        if element_a.is_displayed():
            action = ActionChains(driver)
            action.click_and_hold(element_a)
            action.perform()
            time.sleep(10)
            action.release(element_a)
            action.perform()
            time.sleep(0.2)
            action.release(element_a)
            print("- Human verification approved")
        else:
            time.sleep(2)
    except:
        time.sleep(0.2)
        print("- No human verification needed")



    #Cookie check
    try:
        element = driver.find_element(By.CSS_SELECTOR, '#popup-freetrial > a')
        if element.is_displayed():
            driver.find_element(By.CSS_SELECTOR, '#popup-freetrial > a').click()
            print("- Reject cookies"+"\n")
    except:
        print("- No cookie-box found"+"\n")
        time.sleep(2)


     
    print("- Insert search requirements into brwoser"+"\n")
    #tip 2
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#srh_field').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#srh_field').send_keys(str(key_))    
    driver.find_element(By.CSS_SELECTOR, '#srh_field').send_keys(Keys.ENTER)  


    print("4/7: Writing metadata")
       #Boot check
    try:
        element_a = driver.find_element((By.CSS_SELECTOR, "p[style='text-align: center; text-transform: none; cursor: pointer; -webkit-tap-highlight-color: transparent; user-select: none; outline: 0!important; vertical-align: middle; font-family: Roboto, sans-serif; font-size: 20px; color: #21b5ea; font-weight: normal; display: table-cell; padding: 0; margin: 0;']"))
        if element_a.is_displayed():
            action = ActionChains(driver)
            action.click_and_hold(element_a)
            action.perform()
            time.sleep(10)
            action.release(element_a)
            action.perform()
            time.sleep(0.2)
            action.release(element_a)
            print("- Human verification approved")
        else:
            time.sleep(2)
    except:
        time.sleep(0.2)
        print("- No human verification needed")
    #tip 3
    total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'img'))
    print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")


    #tip 4
    page_length = driver.find_element(By.CSS_SELECTOR, 'body > main > div:nth-child(1) > div.row.item-list-tools > div.col-md-3.hidden-sm-down > div > ul > li.dt-label > span:nth-child(2)')
    stx = str(page_length).replace("of ","")
    stx2 = str(page_length).replace(" pages","")
    page_array_number = ['x'] * int(stx2)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
           #Boot check
        try:
            element_a = driver.find_element((By.CSS_SELECTOR, "p[style='text-align: center; text-transform: none; cursor: pointer; -webkit-tap-highlight-color: transparent; user-select: none; outline: 0!important; vertical-align: middle; font-family: Roboto, sans-serif; font-size: 20px; color: #21b5ea; font-weight: normal; display: table-cell; padding: 0; margin: 0;']"))
            if element_a.is_displayed():
                action = ActionChains(driver)
                action.click_and_hold(element_a)
                action.perform()
                time.sleep(10)
                action.release(element_a)
                action.perform()
                time.sleep(0.2)
                action.release(element_a)
                print("- Human verification approved")
            else:
                time.sleep(2)
        except:
            time.sleep(0.2)
            print("- No human verification needed")
            index = index+1 
            print("-- Working on page : "+str(index)+" out of "+str(numb_))
            time.sleep(10)
            #tip 5
            find_href = driver.find_elements(By.CSS_SELECTOR, 'a > img')
            time.sleep(2)

        with open("URLS/DreamsTime_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into DreamsTime_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == numb_:
            break
        else:
            #tip 6
            print("--- Next page #"+str(index+1))
            driver.find_element(By.CSS_SELECTOR, '#srh_field').send_keys(Keys.RIGHT)  


    print("6/7: Downloading image from DreamsTime_urls.txt"+"\n")
    cnt = 1
    with open('URLS/DreamsTime_urls.txt', 'r') as urls:       
        file = open("URLS/DreamsTime_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from DreamsTime_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from DreamsTime to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")


#6-DuckDuckGo✅
@app.route('/DuckDuckGo', methods=['GET', 'POST'])
def DuckDuckGo():

    #Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/8: Resetting DuckDuckGo_urls.txt"+"\n")
    f = open("URLS/DuckDuckGo_urls.txt", "w")
    f.write("")
    f.close()

    #Variables
    print("2/8: Get search requirements"+"\n")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    output_dir = 'Images/DuckDuckGo_pics'
    print("- Search = "+str(id)+"\n")

    #Driver
    print("3/8: Start driver"+"\n")
    url = "https://duckduckgo.com/?q="+str(key_)+"&t=h_&iar=images&iax=images&ia=images"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)

    #Scroll down and click show more
    print("4/8: Scrolling down to load image urls"+"\n")
    SCROLL_PAUSE_TIME = 10
    last_height = driver.execute_script("return document.body.scrollHeight")
    try:
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#zci-images > div > div.tile-wrap > div > div > div.tile--img__media > span > img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            if new_height == last_height:
                print("--- No more room to scroll ---"+"\n")
                break
            last_height = new_height
            #Test
            #if total_pictures > 25:
            #    break
    except:
        print("- No more pages")
        
    
  #Get Image urls
    print("5/8: Write image url to DuckDuckGo_urls.txt"+"\n")
    find_href = driver.find_elements(By.CSS_SELECTOR, '#zci-images > div > div.tile-wrap > div > div > div.tile--img__media > span > img')
    with open("URLS/DuckDuckGo_urls.txt", "a+") as textFile:
        for idx, my_href in enumerate(find_href):
            sliced = str(my_href.get_attribute("src"))
            textFile.write(str(sliced)+".png"+"\n")

    # Insert into List with image urls
    print("6/8: Write image url to Every_url.txt"+"\n")
    with open("URLS/Every_url.txt", "a+") as textFile:
        for my_href in find_href:
            textFile.write(str(my_href.get_attribute("src"))+".png"+"\n")

    #Download function 
    print("7/8: Downloading image from DuckDuckGo_urls.txt"+"\n")
    with open("URLS/DuckDuckGo_urls.txt", "r") as urls:
        for idx, url in enumerate(urls.readlines()):
            url = url.rstrip("\n")
            print("- Downoading image #"+str(idx+1)+" out of "+str(total_pictures)+" images")
            download_url(url, output_dir, key_)

    #End
    print("\n"+"8/8: Finish downloading "+str(total_pictures)+" images from DuckDuckGo to "+str(output_dir)+"\n")
    print("--- If you did not get all the images, try adjusting SCROLL_PAUSE_TIME ---"+"\n")
    return str("Success")

#7-Ecosia✅
@app.route('/Ecosia', methods=['GET', 'POST'])
def Ecosia():

    #Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/8: Resetting Ecosia_urls.txt"+"\n")
    f = open("URLS/Ecosia_urls.txt", "w")
    f.write("")
    f.close()

    #Variables
    print("2/8: Get search requirements"+"\n")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    output_dir = 'Images/Ecosia_pics'

    #Driver
    print("3/8: Start driver"+"\n")
    url = "https://www.ecosia.org/images?q="+str(key_)
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)

    #Scroll down and click show more
    print("4/8: Scrolling down to load image urls"+"\n")
    SCROLL_PAUSE_TIME = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    try:
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#main > div > section > div > article > div.image-result__link-wrapper > a > img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")
            if new_height == last_height:
                print("--- No more room to scroll ---")
                break
            last_height = new_height

    except:
        print("- No more pages")
        
    
  #Get Image urls
    print("5/8: Write image url to Ecosia_urls.txt"+"\n")
    find_href = driver.find_elements(By.CSS_SELECTOR, '#main > div > section > div > article > div.image-result__link-wrapper > a > img')
    with open("URLS/Ecosia_urls.txt", "a+") as textFile:
        for idx, my_href in enumerate(find_href):
            sliced = str(my_href.get_attribute("src"))
            textFile.write(str(sliced)+".png"+"\n")

    # Insert into List with image urls
    print("6/8: Write image url to Every_url.txt"+"\n")
    with open("URLS/Every_url.txt", "a+") as textFile:
        for my_href in find_href:
            textFile.write(str(my_href.get_attribute("src"))+".png"+"\n")

    #Download function 
    print("7/8: Downloading image from Ecosia_urls.txt"+"\n")
    with open("URLS/Ecosia_urls.txt", "r") as urls:
        for idx, url in enumerate(urls.readlines()):
            url = url.rstrip("\n")
            print("- Downoading image #"+str(idx+1)+" out of "+str(total_pictures)+" images")
            download_url(url, output_dir, key_)

    #End
    print("\n"+"8/8: Finish downloading "+str(total_pictures)+" images from Ecosia to "+str(output_dir)+"\n")
    print("--- If you did not get all the images, try adjusting SCROLL_PAUSE_TIME ---"+"\n")
    return str("Success")

#18-EveryPixel ✅✅✅✅✅✅✅✅✅✅
@app.route('/EveryPixel', methods=['GET', 'POST']) 
def EveryPixel():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting EveryPixel_urls.txt"+"\n")
    f = open("URLS/EveryPixel_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/EveryPixel_pics'
    SCROLL_PAUSE_TIME = 10
    source = "EveryPixel.com"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    #tip 1
    url = "https://www.everypixel.com"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(10)
    print("- Insert search requirements into brwoser"+"\n")
    #tip 2
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'body > div.wrap.wrap-index > div > div > div > div > form > span > input').send_keys(str(key_))    
    driver.find_element(By.CSS_SELECTOR, 'body > div.wrap.wrap-index > div > div > div > div > form > span > input').send_keys(Keys.ENTER)    
    time.sleep(5)

    #element = driver.find_element(By.CSS_SELECTOR, '#bnp_btn_accept')
    #if element.is_displayed():
     #   driver.find_element(By.CSS_SELECTOR, '#bnp_btn_accept').click()
      #  print("- Reload page"+"\n")
    #else:
     #   time.sleep(2)
     




    print("5/7: Writing metadata")
    #tip 3
    total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '.thumb__img'))
    print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

    #tip 4
    page_length = len(driver.find_element(By.XPATH, "//*[@id='root-pagination']/nav/ul/li"))
    print(page_length)
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        #tip 5
        find_href = driver.find_elements(By.CSS_SELECTOR, '.thumb__img')
        time.sleep(2)

        with open("URLS/EveryPixel_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into EveryPixel_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == numb_:
            break
        else:
            try: 
                element = driver.find_element(By.CSS_SELECTOR, "/html/body/div[2]/div[4]/div[2]/nav/ul/li["+str(index+1)+"]")
                if element.is_displayed():
                    element.click()
                    print("--- Next page #"+str(index+1)+"\n")
                else:
                    time.sleep(2)
            except:
                time.sleep(2)


     

    print("6/7: Downloading image from EveryPixel_urls.txt"+"\n")
    cnt = 1
    with open('URLS/EveryPixel_urls.txt', 'r') as urls:       
        file = open("URLS/EveryPixel_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from EveryPixel_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from EveryPixel to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")



#7-Flickr
@app.route('/Flickr', methods=['GET', 'POST'])
def Flickr():

    #Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/9: Resetting Flickr_urls.txt"+"\n")
    f = open("URLS/Flickr_urls.txt", "w")
    f.write("")
    f.close()

    #Variables
    print("2/9: Get search requirements"+"\n")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    output_dir = 'Images/Flickr_pics'
    SCROLL_PAUSE_TIME = 10

    #Driver
    print("3/9: Start driver"+"\n")
    url = "https://www.flickr.com/search/?text="+str(key_)+"&view_all=1"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    wait = WebDriverWait(driver, 20)

    print("- Wait for cookie button")
    time.sleep(30)

    #Accept coockies
    print("4/11: Accept cookies"+"\n")
    #driver.find_elements_by_xpath("//*[contains(text(), 'Reject All')]")

    element = driver.find_element(By.XPATH, '/a[2]')
    if element.is_displayed():
        element.click()
        print("- Cookies found"+"\n")
    else:
        print("- Cookies not found"+"\n")
    time.sleep(2)


    #Scroll down and click show more
    print("5/9: Scrolling down to load image urls"+"\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("--- No more room to scroll ---")
                break
            last_height = new_height

            time.sleep(SCROLL_PAUSE_TIME)
            print("- Load button check"+"\n")
            for button in driver.find_elements(By.CSS_SELECTOR, 'button#yui_3_16_0_1_1665507030055_34330.alt'):
                button.click()
                print("- Load button clicked!"+"\n")

 

            #Test
            #if total_pictures > 25:
            #    break

    
  #Get Image urls
    print("6/9: Write image url to Flickr_urls.txt"+"\n")
    find_href = driver.find_elements(By.CSS_SELECTOR, 'img')
    with open("URLS/Flickr_urls.txt", "a+") as textFile:
        for idx, my_href in enumerate(find_href):
            sliced = str(my_href.get_attribute("src"))
            textFile.write(str(sliced)+"\n")

    # Insert into List with image urls
    print("7/9: Write image url to Every_url.txt"+"\n")
    with open("URLS/Every_url.txt", "a+") as textFile:
        for my_href in find_href:
            textFile.write(str(my_href.get_attribute("src"))+"\n")

    #Download function 
    print("8/9: Downloading image from Flickr_urls.txt"+"\n")
    with open("URLS/Flickr_urls.txt", "r") as urls:
        for idx, url in enumerate(urls.readlines()):
            url = url.rstrip("\n")
            print("- Downoading image #"+str(idx+1)+" out of "+str(total_pictures)+" images")
            download_url(url, output_dir, key_)

    #End
    print("\n"+"9/9: Finish downloading "+str(total_pictures)+" images from Flickr to "+str(output_dir)+"\n")
    print("--- If you did not get all the images, try adjusting SCROLL_PAUSE_TIME ---"+"\n")
    return str("Success")

#8-Getty  ✅✅✅✅✅✅✅✅✅✅
@app.route('/Getty', methods=['GET', 'POST']) 
def Getty():
    
      #Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting Getty_urls.txt"+"\n")
    f = open("URLS/Getty_urls.txt", "w")
    f.write("")
    f.close()

    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Getty_pics'


    #Driver
    print("3/7: Start driver")
    print("- Wainting for cookie-box"+"\n")
    url = "https://www.gettyimages.dk/photos/sd?assettype=image&phrase="+str(key_)+"&sort=mostpopular&license=rf,rm&page=1"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)

    print("4/7: Accept cookies"+"\n")
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(5)

    print("5/7: Download image urls")
    total_pictures = driver.find_element(By.CSS_SELECTOR, "body > div.content_wrapper > section > div > main > div > div > div:nth-child(4) > div.Gallery-module__columnContainer___LqU0P > div.GallerySummary-module__container___evoqD > div.HeadlineToggleRow-module__container___qzPv_ > div > h1").text
    page_length = driver.find_element(By.CSS_SELECTOR, "section.PaginationRow-module__container___LxZJN span.PaginationRow-module__lastPage___k9Pq7").text
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 
    print("- There are "+str(page_length)+" pages available with "+str(total_pictures)+"\n")
    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        find_href = driver.find_elements(By.CSS_SELECTOR, 'img.MosaicAsset-module__thumb___yvFP5')
        time.sleep(2)


        with open("URLS/Getty_urls.txt", "a+") as textFile:
            for my_href in find_href:
                i = str(my_href.get_attribute("src")).index("?")
                Url_wanted = str(my_href.get_attribute("src"))[:i+1]
                textFile.write(str(Url_wanted)+".png"+"\n")

        print("-- Image-Urls inserted into Getty_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted)+".png"+"\n")
            
        print("-- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)
        if index == 1:
            break

        if index == numb_:
            break

        url = "https://www.gettyimages.dk/photos/sd?assettype=image&phrase="+str(key_)+"&sort=mostpopular&license=rf,rm&page="+str(index+1)
        driver.get(url)
       


    print("6/7: Downloading image from Getty_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Getty_urls.txt', 'r') as urls:       
        file = open("URLS/Getty_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Getty_urls.txt:', Counter)

        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from Getty to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                cnt+=1
                download_url(url, output_dir, key_)
  

    #End
    return str("Success")

#9-Gibiru ✅✅✅✅✅✅✅✅✅✅
@app.route('/Gibiru', methods=['GET', 'POST']) 
def Gibiru():
	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/6: Resetting Gibiru_urls.txt"+"\n")
    f = open("URLS/Gibiru_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/6: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Gibiru_pics'


    #Driver
    print("3/6: Start driver")
    print("- Wainting for cookie-box"+"\n")
    url = "https://gibiru.com/results.html?q="+str(key_)+"&cx=partner-pub-5956360965567042%3A8627692578&cof=FORID%3A11&ie=UTF-8"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)
    
    print("4/6: Writing metadata")
    driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[2]").click()
    time.sleep(2)
    page_length = len(driver.find_elements(By.CSS_SELECTOR, "div.gsc-resultsRoot.gsc-tabData.gsc-tabdActive div.gsc-cursor-box.gs-bidi-start-align div.gsc-cursor div.gsc-cursor-page"))
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 
    print("- There are "+str(page_length)+" pages available")

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        find_href = driver.find_elements(By.CSS_SELECTOR, 'img.gs-image.gs-image-scalable')
        time.sleep(2)

        with open("URLS/Gibiru_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted)+".png"+"\n")

        print("--- Image-Urls inserted into Gibiru_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted)+".png"+"\n")

            
        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 2:
            break

        driver.find_element(By.CSS_SELECTOR, "#___gcse_0 > div > div > div > div.gsc-wrapper > div.gsc-resultsbox-visible > div.gsc-resultsRoot.gsc-tabData.gsc-tabdActive > div > div.gsc-cursor-box.gs-bidi-start-align > div > div:nth-child("+str(index+1)+")").click()
    

    print("5/6: Downloading image from Gibiru_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Gibiru_urls.txt', 'r') as urls:       
        file = open("URLS/Gibiru_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Gibiru_urls.txt:', Counter)

        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"6/6: Finish downloading "+str(Counter)+" images from Gibiru to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                cnt+=1
                download_url(url, output_dir, key_)
  

    #End
    return str("Success")

#10-Google ---- need login
@app.route('/Google', methods=['GET', 'POST']) 
def Google():
	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/6: Resetting Google_urls.txt"+"\n")
    f = open("URLS/Google_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/6: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Google_pics'
    SCROLL_PAUSE_TIME = 10
    email = "email"
    password = "fff"


    #Driver
    print("3/6: Start driver")
    print("- Wainting for cookie-box"+"\n")
    url = "https://www.google.com/search?q="+str(key_)+"&sxsrf=ALiCzsbWa-4yvuJugGI2atST3Sh3wxNYIw:1665957580084&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjz7ZXO3-X6AhWOjYsKHS61BlMQ_AUoAXoECAIQAw&biw=1440&bih=789&dpr=1"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=C:/Users/mention user name/AppData/Local/Google/Chrome/User Data/Default");
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)


    #Accept coockies
    print("4/11: Accept cookies"+"\n")
    #driver.find_elements_by_xpath("//*[contains(text(), 'Reject All')]")

    element = driver.find_element(By.CSS_SELECTOR, '.VfPpkd-RLmnJb')
    if element.is_displayed():
        element.click()
        print("- Cookies found"+"\n")
        print("- Login detected"+"\n")
        driver.find_element(By.CSS_SELECTOR, '#identifierId').send_keys(str(email))
        driver.find_element(By.CSS_SELECTOR, '#identifierId').send_keys(Keys.RETURN)
    else:
        print("- Cookies not found"+"\n")
    time.sleep(2)


    #Scroll down and click show more
    print("5/9: Scrolling down to load image urls"+"\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("--- No more room to scroll ---")
                break
            last_height = new_height

            time.sleep(SCROLL_PAUSE_TIME)
            print("- Load button check"+"\n")
            for button in driver.find_elements(By.CSS_SELECTOR, 'button#yui_3_16_0_1_1665507030055_34330.alt'):
                button.click()
                print("- Load button clicked!"+"\n")

 

            #Test
            #if total_pictures > 25:
            #    break

    
  #Get Image urls
    print("6/9: Write image url to Flickr_urls.txt"+"\n")
    find_href = driver.find_elements(By.CSS_SELECTOR, 'img')
    with open("URLS/Flickr_urls.txt", "a+") as textFile:
        for idx, my_href in enumerate(find_href):
            sliced = str(my_href.get_attribute("src"))
            textFile.write(str(sliced)+"\n")

    # Insert into List with image urls
    print("7/9: Write image url to Every_url.txt"+"\n")
    with open("URLS/Every_url.txt", "a+") as textFile:
        for my_href in find_href:
            textFile.write(str(my_href.get_attribute("src"))+"\n")

    #Download function 
    print("8/9: Downloading image from Flickr_urls.txt"+"\n")
    with open("URLS/Flickr_urls.txt", "r") as urls:
        for idx, url in enumerate(urls.readlines()):
            url = url.rstrip("\n")
            print("- Downoading image #"+str(idx+1)+" out of "+str(total_pictures)+" images")
            download_url(url, output_dir, key_)

    #End
    print("\n"+"9/9: Finish downloading "+str(total_pictures)+" images from Flickr to "+str(output_dir)+"\n")
    print("--- If you did not get all the images, try adjusting SCROLL_PAUSE_TIME ---"+"\n")
    return str("Success")

#11-Metacrawler ✅✅✅✅✅✅✅✅✅✅
@app.route('/Metacrawler', methods=['GET', 'POST']) 
def Metacrawler():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/6: Resetting Metacrawler_urls.txt"+"\n")
    f = open("URLS/Metacrawler_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/6: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Metacrawler_pics'
    SCROLL_PAUSE_TIME = 10


    #Driver
    print("3/6: Start driver")
    print("- Wainting for cookie-box"+"\n")
    url = "https://www.metacrawler.com/serp?q="+str(key_)+"&page=1&sc=XzkkJtEkHlRQ20"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)


    print("4/6: Writing metadata")
    page_length = 29
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 
    print("- There are "+str(page_length)+" pages available")

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        find_href = driver.find_elements(By.CSS_SELECTOR, 'body > div.layout > div.layout__body > div.layout__mainline > div.mainline-results.mainline-results__images > div.images-bing > div > div > a > img')
        time.sleep(2)

        with open("URLS/Metacrawler_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted)+".png"+"\n")

        print("--- Image-Urls inserted into Metacrawler_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted)+".png"+"\n")

            
        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 2:
            break

        url2 = "https://www.metacrawler.com/serp?q="+str(key_)+"&page="+str(index+1)+"&sc=XzkkJtEkHlRQ20"
        driver.get(url2)    

    print("5/6: Downloading image from Metacrawler_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Metacrawler_urls.txt', 'r') as urls:       
        file = open("URLS/Metacrawler_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Metacrawler_urls.txt:', Counter)

        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"6/6: Finish downloading "+str(Counter)+" images from Metacrawler to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                cnt+=1
                download_url(url, output_dir, key_)
  

    #End
    return str("Success")

#12-Naver ✅✅✅✅✅✅✅✅✅✅
@app.route('/Naver', methods=['GET', 'POST']) 
def Naver():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting Naver_urls.txt"+"\n")
    f = open("URLS/Naver_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Naver_pics'
    SCROLL_PAUSE_TIME = 10
    source = "search.naver.com"

    #Driver
    print("3/7: Start driver")
    print("- Wainting for cookie-box"+"\n")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="+str(key_)+"&oquery=&tqi=h0y7Awp0YihssgS3Iisssssstgh-059602"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)

    #Scroll down and click show more
    print("4/7: Scrolling down to load image urls"+"\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("--- No more room to scroll ---"+"\n")
                break
            last_height = new_height

            time.sleep(SCROLL_PAUSE_TIME)
  
    print("5/7: Writing metadata")
    page_length = 1
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        find_href = driver.find_elements(By.CSS_SELECTOR, '#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div > div > div.thumb > a > img')
        time.sleep(2)

        with open("URLS/Naver_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted = str(my_href.get_attribute("data-lazy-src"))
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")
                textFile.write(str(Url_wanted)+"\n")

        print("--- Image-Urls inserted into Naver_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 2:
            break


    print("6/7: Downloading image from Naver_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Naver_urls.txt', 'r') as urls:       
        file = open("URLS/Naver_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Naver_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from Naver to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")

#13-Pexels ✅✅✅✅✅✅✅✅✅✅
@app.route('/Pexels', methods=['GET', 'POST']) 
def Pexels():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting Pexels_urls.txt"+"\n")
    f = open("URLS/Pexels_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Pexels_pics'
    SCROLL_PAUSE_TIME = 10
    source = "pexels.com"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    url = "https://www.pexels.com/da-dk/sog/"+str(key_)+"/"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)
    print("- Insert search requirements into brwoser"+"\n")
    #Scroll down and click show more
    print("4/7: Scrolling down to load image urls"+"\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("--- No more room to scroll ---"+"\n")
                break
            last_height = new_height
            time.sleep(SCROLL_PAUSE_TIME)
  
    print("5/7: Writing metadata")
    page_length = 1
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        find_href = driver.find_elements(By.CSS_SELECTOR, '#\- > div.Grid_gridWrapper__jJO3V.BreakpointGrid_grid-spacing-mobile-15__pAUo3.BreakpointGrid_grid-spacing-tablet-15__r9ing.BreakpointGrid_grid-spacing-desktop-30__75rr9.BreakpointGrid_grid-spacing-oversized-30__31ge3 > div > div > div > article > a > img')
        time.sleep(2)

        with open("URLS/Pexels_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Pexels_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 2:
            break


    print("6/7: Downloading image from Pexels_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Pexels_urls.txt', 'r') as urls:       
        file = open("URLS/Pexels_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Pexels_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from Pexels to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")

#14-Pinterest ✅✅✅✅✅✅✅✅✅✅
@app.route('/Pinterest', methods=['GET', 'POST']) 
def Pinterest():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting Pinterest_urls.txt"+"\n")
    f = open("URLS/Pinterest_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Pinterest_pics'
    SCROLL_PAUSE_TIME = 10
    source = "pinterest.dk"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    url = "https://www.pinterest.dk/search/pins/?q=test&rs=typed"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)
    print("- Insert search requirements into brwoser"+"\n")
    driver.find_element(By.CSS_SELECTOR, "#__PWS_ROOT__ > div.zI7.iyn.Hsu > div > div:nth-child(2) > div.QLY._he.zI7.iyn.Hsu > div > div.ESm.PrF.ujU.wYR.zI7.iyn.Hsu > div > div > form > div > div.Jea.LJB.Pw5.XgI.XiG.fev.gjz.urM.zI7.iyn.Hsu > div.gjz.hs0.sLG.ujU.un8.C9i.TB_ > div.ujU.zI7.iyn.Hsu > input[type=text]").clear()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#__PWS_ROOT__ > div.zI7.iyn.Hsu > div > div:nth-child(2) > div.QLY._he.zI7.iyn.Hsu > div > div.ESm.PrF.ujU.wYR.zI7.iyn.Hsu > div > div > form > div > div.Jea.LJB.Pw5.XgI.XiG.fev.gjz.urM.zI7.iyn.Hsu > div.gjz.hs0.sLG.ujU.un8.C9i.TB_ > div.ujU.zI7.iyn.Hsu > input[type=text]").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#__PWS_ROOT__ > div.zI7.iyn.Hsu > div > div:nth-child(2) > div.QLY._he.zI7.iyn.Hsu > div > div.ESm.PrF.ujU.wYR.zI7.iyn.Hsu > div > div > form > div > div.Jea.LJB.Pw5.XgI.XiG.fev.gjz.urM.zI7.iyn.Hsu > div.gjz.hs0.sLG.ujU.un8.C9i.TB_ > div.ujU.zI7.iyn.Hsu > input[type=text]").send_keys(str(key_))
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#__PWS_ROOT__ > div.zI7.iyn.Hsu > div > div:nth-child(2) > div.QLY._he.zI7.iyn.Hsu > div > div.ESm.PrF.ujU.wYR.zI7.iyn.Hsu > div > div > form > div > div.Jea.LJB.Pw5.XgI.XiG.fev.gjz.urM.zI7.iyn.Hsu > div.gjz.hs0.sLG.ujU.un8.C9i.TB_ > div.ujU.zI7.iyn.Hsu > input[type=text]").send_keys(Keys.RETURN)



    #Scroll down and click show more
    print("4/7: Scrolling down to load image urls"+"\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, 'div.XiG.zI7.iyn.Hsu > img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")
# full xp = /html/body/div[1]/div[1]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/img
# normal xp = //*[@id="mweb-unauth-container"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/img
# css selector = #mweb-unauth-container > div > div.zI7.iyn.Hsu > div.F6l.ZZS.k1A.zI7.iyn.Hsu > div > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > div > div:nth-child(1) > a > div > div > div > div > div.XiG.zI7.iyn.Hsu > img
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("--- No more room to scroll ---"+"\n")
                break
            last_height = new_height
            time.sleep(SCROLL_PAUSE_TIME)
  
    print("5/7: Writing metadata")
    page_length = 1
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        find_href = driver.find_elements(By.CSS_SELECTOR, 'div.XiG.zI7.iyn.Hsu > img')
        time.sleep(2)

        with open("URLS/Pexels_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Pexels_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 2:
            break


    print("6/7: Downloading image from Pexels_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Pexels_urls.txt', 'r') as urls:       
        file = open("URLS/Pexels_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Pexels_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from Pexels to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")

#15-Pixabay ✅✅✅✅✅✅✅✅✅✅
@app.route('/Pixabay', methods=['GET', 'POST']) 
def Pixabay():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting Pixabay_urls.txt"+"\n")
    f = open("URLS/Pixabay_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Pixabay_pics'
    SCROLL_PAUSE_TIME = 10
    source = "pixabay.com"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    url = "https://pixabay.com/"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)
    print("- Insert search requirements into brwoser"+"\n")
    driver.find_element(By.CSS_SELECTOR, '#hero > div.search_form > form > div > span > input').click()
    driver.find_element(By.CSS_SELECTOR, '#hero > div.search_form > form > div > span > input').send_keys(str(key_))    
    driver.find_element(By.CSS_SELECTOR, '#hero > div.search_form > form > div > span > input').send_keys(Keys.ENTER)    
    time.sleep(5)



    print("4/7: Scrolling down to load image urls"+"\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#content > div > div > div > div.row-masonry.search-results > div > div > div > div > a > img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("--- No more room to scroll ---"+"\n")
                break
            last_height = new_height
            time.sleep(SCROLL_PAUSE_TIME)
  
    print("5/7: Writing metadata")
    page_length = 1
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        find_href = driver.find_elements(By.CSS_SELECTOR, '#content > div > div > div > div.row-masonry.search-results > div > div > div > div > a > img')
        time.sleep(2)

        with open("URLS/Pixabay_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Pixabay_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 2:
            break


    print("6/7: Downloading image from Pixabay_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Pixabay_urls.txt', 'r') as urls:       
        file = open("URLS/Pixabay_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Pixabay_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from Pixabay to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")

#16-Qmamu ✅✅✅✅✅✅✅✅✅✅
@app.route('/Qmamu', methods=['GET', 'POST']) 
def Qmamu():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting Qmamu_urls.txt"+"\n")
    f = open("URLS/Qmamu_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Pixabay_pics'
    SCROLL_PAUSE_TIME = 10
    source = "qmamu.com"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    url = "https://qmamu.com/"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)
    print("- Insert search requirements into brwoser"+"\n")
    driver.find_element(By.CSS_SELECTOR, '#root > div > div.sc-dlnjwi.dJXsSm > div.sc-eCApnc.iylGhi > ul > a:nth-child(2)').click()
    driver.find_element(By.CSS_SELECTOR, '#search_key').click()
    driver.find_element(By.CSS_SELECTOR, '#search_key').send_keys(str(key_))    
    driver.find_element(By.CSS_SELECTOR, '#search_key').send_keys(Keys.ENTER)    
    time.sleep(12)

    print("4/7: Writing metadata")
    total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#___gcse_1 > div > div > div > div.gsc-wrapper > div.gsc-resultsbox-visible > div > div > div.gsc-expansionArea > div > div.gs-result.gs-imageResult.gs-imageResult-popup > div.gs-image-popup-box > div.gs-image-box > a > img'))
    print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

  
    page_length = 10
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        #tip 3
        find_href = driver.find_elements(By.CSS_SELECTOR, '#___gcse_1 > div > div > div > div.gsc-wrapper > div.gsc-resultsbox-visible > div > div > div.gsc-expansionArea > div > div.gs-result.gs-imageResult.gs-imageResult-popup > div.gs-image-popup-box > div.gs-image-box > a > img')
        time.sleep(2)

        with open("URLS/Qmamu_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Qmamu_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 10:
            break
        else:
            driver.find_element(By.CSS_SELECTOR, '.gsc-cursor-container-next').click()


    print("6/7: Downloading image from Qmamu_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Qmamu_urls.txt', 'r') as urls:       
        file = open("URLS/Qmamu_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Qmamu_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from Qmamu to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")

#17-Qwant ✅✅✅✅✅✅✅✅✅✅
@app.route('/Qwant', methods=['GET', 'POST']) 
def Qwant():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting Qwant_urls.txt"+"\n")
    f = open("URLS/Qwant_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/Qwant_pics'
    SCROLL_PAUSE_TIME = 10
    source = "qwant.com"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    #tip 1
    url = "https://www.qwant.com/?q=&t=images"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)
    print("- Insert search requirements into brwoser"+"\n")
    #tip 2
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div > input[type=search]').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div > input[type=search]').send_keys(str(key_))    
    driver.find_element(By.CSS_SELECTOR, 'div > input[type=search]').send_keys(Keys.ENTER)    
    time.sleep(12)

    #element = driver.find_element(By.CSS_SELECTOR, '#bnp_btn_accept')
    #if element.is_displayed():
     #   driver.find_element(By.CSS_SELECTOR, '#bnp_btn_accept').click()
      #  print("- Reload page"+"\n")
    #else:
     #   time.sleep(2)
     

    print("4/7: Scrolling down to load image urls"+"\n")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#root > div.SearchLayout-module__container___2GMK3.Flex-module__flex___35zId.Flex-module__column___1m4v1 > div.SearchLayout-module__content___25Tnc > div > div > div > div.Images-module__ImagesGrid___KhooK > a > div.Card-module__Card___d7OS7.Card-module__CardWithRipple___2shJX.Images-module__ImagesGridItemImage___1vafn.Ripple-module__RippleContainer___2zD03.Box-module__relative___1cR1n > img'))
            print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("--- No more room to scroll ---"+"\n")
                break
            last_height = new_height
            time.sleep(SCROLL_PAUSE_TIME)


    print("5/7: Writing metadata")
    #tip 3
    total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#root > div.SearchLayout-module__container___2GMK3.Flex-module__flex___35zId.Flex-module__column___1m4v1 > div.SearchLayout-module__content___25Tnc > div > div > div > div.Images-module__ImagesGrid___KhooK > a > div.Card-module__Card___d7OS7.Card-module__CardWithRipple___2shJX.Images-module__ImagesGridItemImage___1vafn.Ripple-module__RippleContainer___2zD03.Box-module__relative___1cR1n > img'))
    print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")


    #tip 4
    page_length = 1
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        #tip 5
        find_href = driver.find_elements(By.CSS_SELECTOR, '#root > div.SearchLayout-module__container___2GMK3.Flex-module__flex___35zId.Flex-module__column___1m4v1 > div.SearchLayout-module__content___25Tnc > div > div > div > div.Images-module__ImagesGrid___KhooK > a > div.Card-module__Card___d7OS7.Card-module__CardWithRipple___2shJX.Images-module__ImagesGridItemImage___1vafn.Ripple-module__RippleContainer___2zD03.Box-module__relative___1cR1n > img')
        time.sleep(2)

        with open("URLS/Qwant_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Qwant_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 10:
            break
        else:
            #tip 6
            print("--- Restart scroll #"+str(index))

    print("6/7: Downloading image from Qwant_urls.txt"+"\n")
    cnt = 1
    with open('URLS/Qwant_urls.txt', 'r') as urls:       
        file = open("URLS/Qwant_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from Qwant_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from Qwant to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")

#18-SearchEncrypt ✅✅✅✅✅✅✅✅✅✅
@app.route('/SearchEncrypt', methods=['GET', 'POST']) 
def SearchEncrypt():

	#Prepare terminal
    os.system("clear")

    #Reset url txt file
    print("1/7: Resetting SearchEncrypt_urls.txt"+"\n")
    f = open("URLS/SearchEncrypt_urls.txt", "w")
    f.write("")
    f.close()


    #Variables
    print("2/7: Get search requirements")
    id = request.args.get('ID')
    key_ = id.split('*')[0]
    print("- Search requirements = "+str(key_)+"\n")
    output_dir = 'Images/SearchEncrypt_pics'
    SCROLL_PAUSE_TIME = 10
    source = "searchencrypt.com"

    #Driver
    print("3/7: Start driver and navigate to imagesearch")
    #tip 1
    url = "https://www.searchencrypt.com/home"
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.set_window_size(1000,700)
    driver.get(url)
    time.sleep(5)
    print("- Insert search requirements into brwoser"+"\n")
    #tip 2
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#autosuggest > input').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#autosuggest > input').send_keys(str(key_))    
    driver.find_element(By.CSS_SELECTOR, '#autosuggest > input').send_keys(Keys.ENTER)    
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#app > section > section.search-header.serp__header.--sticky > div.search-header__bottom.site-wrapper.--transition > nav > ul > li.serp-nav__item.serp-nav__image > a').click()

    #element = driver.find_element(By.CSS_SELECTOR, '#bnp_btn_accept')
    #if element.is_displayed():
     #   driver.find_element(By.CSS_SELECTOR, '#bnp_btn_accept').click()
      #  print("- Reload page"+"\n")
    #else:
     #   time.sleep(2)
     




    print("5/7: Writing metadata")
    #tip 3
    total_pictures = len(driver.find_elements(By.CSS_SELECTOR, '#app > section > section.serp__body.site-wrapper.container-wrapper > section.image-gallery.xserp__results.container > div.image-gallery__entries > div > img'))
    print("- There are "+str(total_pictures)+" pictures available and still loading......"+"\n")


    #tip 4
    page_length = 1
    page_array_number = ['x'] * int(page_length)
    numb_ = len(page_array_number) 

    for index, item in enumerate(page_array_number):
        index = index+1 
        print("-- Working on page : "+str(index)+" out of "+str(numb_))
        time.sleep(10)
        #tip 5
        find_href = driver.find_elements(By.CSS_SELECTOR, '#app > section > section.serp__body.site-wrapper.container-wrapper > section.image-gallery.xserp__results.container > div.image-gallery__entries > div > img')
        time.sleep(2)

        with open("URLS/SearchEncrypt_urls.txt", "a+") as textFile:
            for my_href in find_href:
                Url_wanted2 = str(my_href.get_attribute("src"))
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into SearchEncrypt_urls.txt from page "+str(index))
                
        with open("URLS/Every_url.txt", "a+") as textFile:
            for my_href in find_href:
                textFile.write(str(Url_wanted2)+"\n")

        print("--- Image-Urls inserted into Every_url.txt from page "+str(index)+"\n")

        time.sleep(10)

        if index == 1:
            break
        else:
            #tip 6
            print("--- Restart scroll #"+str(index))

    print("6/7: Downloading image from SearchEncrypt_urls.txt"+"\n")
    cnt = 1
    with open('URLS/SearchEncrypt_urls.txt', 'r') as urls:       
        file = open("URLS/SearchEncrypt_urls.txt", "r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                Counter += 1

        print('- Total Number of image urls from SearchEncrypt_urls.txt:', Counter)
        for url in urls.readlines():
            url = url.rstrip("\n")
            if cnt == Counter:
                print("\n"+"7/7: Finish downloading "+str(Counter)+" images from SearchEncrypt to "+str(output_dir)+"\n")
                break
            else:
                print("- Downloading image #"+str(cnt)+" out of "+str(Counter)+" images")
                download_url(url, output_dir, key_, cnt, source)
                cnt+=1
  
    return str("Success")



if __name__ == '__main__':
    app.run(debug=True)
