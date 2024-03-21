import re
from playwright.sync_api import Page, expect, sync_playwright
import time
import pandas as pd

url = "https://www.youtube.com/@MemeAsylum/shorts"


class YoutubeScraper():
    def __init__(self, url):
        
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.url = url
    
    def scrape(self):
        self.page.goto(url)

        url_results = []
        self.page.wait_for_timeout(5000)
        for i in range(5):
            #get url of video
            video = self.page.locator("ytd-rich-grid-row").get_by_label("Discord Memes - play Short").nth(i)
            vid_url = "https://www.youtube.com" +str(video.get_attribute("href"))
            
            #create new tab and go the url
            new_page = self.context.new_page()
            new_page.goto(vid_url)
            #load the new tab
            new_page.wait_for_timeout(3000)

            new_page.locator("#menu-button > #button-shape > button").click()
            time.sleep(15)
            print(vid_url)
            # self.page.keyboard.type(vid_url)
            # self.page.keyboard.press("Enter")
            new_page.close()
            time.sleep(3)

        print(url_results)

        
        time.sleep(10)
        self.page.screenshot(path="example.png")
        self.shutOff()

    def shutOff(self):
        #turns of playwright
        self.browser.close()
        self.playwright.stop()

scrape = YoutubeScraper(url)
scrape.scrape()

'''
get url of each video
go the url the video and see the date posted
if date poseted is within a certain range, then keep
find the viewcount, 


'''


class Video():
    def __init__(self, viewcount, url, hash, ) -> None:
        pass


