from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("E:\WhitehatJr\c-127\chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

headers = ["Name", "Distance", "Mass", "Radius"]
stars_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tags in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tags.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_td_tags = td_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/"+hyperlink_td_tags.find_all("a", href=True)[0]["href"])
            stars_data.append(temp_list)

scrape()

with open("stars.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)