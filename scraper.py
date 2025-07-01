from bs4 import BeautifulSoup
import requests
import math
import time

base_url = 'https://www.snapdeal.com/product/hari-darshan-ghee-wati-2/671023006323/reviews'
headers = {'User-Agent': 'Mozilla/5.0'}

html_text = requests.get(url=base_url,headers=headers).text
soup = BeautifulSoup(html_text,'lxml')


reviews_no = soup.find('small',class_='total LTgray')
if reviews_no is not None:
    total_reviews = int((reviews_no[-10:-8]))
    pages = math.ceil(total_reviews/10)

else:
    pages = 1



i=1
while i<=pages:
    url = f'{base_url}?{i}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    html_text = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(html_text,'lxml')


    review_blocks = soup.find_all('div', class_='user-review')
    for block in review_blocks:
        review_text_tag = block.find('div', class_='head')
        review_text = review_text_tag.text.strip() if review_text_tag else "N/A"

        user_tag = block.find('div', class_='_reviewUserName')
        if user_tag:
            user_info = user_tag.text.strip()  
            if ' on ' in user_info:
                user_name = user_info.split(' on ')[0].replace('by ', '')
                review_date = user_info.split(' on ')[1]
            else:
                user_name = user_info.replace('by ', '')
                review_date = "Unknown date"
        else:
            user_name = "Anonymous"
            review_date = "Unknown date"

        if user_name != "Anonymous":
            print(f"{user_name} | {review_date} | {review_text}")

    

    i += 1
    time.sleep(30)

print("data executed")
