from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("http://placement.iitm.ac.in/students/login.php")

username = browser.find_element_by_id("rollno")
password = browser.find_element_by_id("pass")
username.send_keys("username")
password.send_keys("password")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']").click()

alert = browser.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()

browser.get("http://placement.iitm.ac.in/students/home.php")
browser.get("http://placement.iitm.ac.in/students/comp_list.php")

content = browser.find_element_by_id("content")
table = content.find_element_by_xpath('div/div/table[4]/tbody') #

rows = table.find_elements_by_tag_name("tr")

database = [["Sl.No", "Company Name", "Profile Name", "Resume Deadline", "PPT Date", "Test Date", "GD Date", "Interview Date"]]
for row in rows[1:]:
    temp = row.find_elements_by_tag_name("td")
    database.append([temp[0].text,temp[1].find_element_by_tag_name("a").find_element_by_tag_name("strong").text,temp[2].find_element_by_tag_name("a").find_element_by_tag_name("font").text,temp[3].text,temp[4].text,temp[5].text,temp[6].text,temp[7].text])

time.sleep(5)
browser.close()
browser.quit()

import pandas as pd
df_new = pd.DataFrame(database[1:], columns = database[0])

df_old = pd.read_csv('companies.csv')

if df_old.shape == df_new.shape:
    print('No new companies')
else:
    print('Newly added')
    for i in df_new['Company Name']:
        if (i == df_old['Company Name']).any() == False:
            print(df_new[i == df_new['Company Name']])
    df_new.to_csv('companies.csv', index=False, encoding='utf-8')
