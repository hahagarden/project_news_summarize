# user-agent (www.useragentstring.com) : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime

# BeautifulSoup 객체 생성
def get_soup_obj(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    return soup


default_img = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#"
for sid in ['100', '101', '102']:
    # 해당 분야 상위 뉴스 목록 주소
    sec_url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec" + "&sid1=" + sid
    print("section url : ", sec_url)

    # 해당 분야 상위 뉴스 HTML 가져오기
    soup = get_soup_obj(sec_url)

    # 해당 분야 상위 뉴스 세 개 가져오기
    lis3 = soup.find('ul', class_='type06_headline').find_all("li", limit=3)
    for li in lis3:
        # title : 뉴스 제목, news_url : 뉴스 url, image_url : 이미지 url
        news_info = {
            "title": li.img.attrs.get('alt') if li.img
            else li.a.text.replace("\n", "").replace("\t", "").replace("\r", ""),
            "date": li.find(class_="date").text,
            "news_url": li.a.attrs.get('href'),
            "image_url": li.img.attrs.get('src') if li.img else default_img
        }
        print(news_info)
