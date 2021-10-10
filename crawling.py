# user-agent (www.useragentstring.com) : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
import requests
from bs4 import BeautifulSoup # beautifulsoup : python library for pulling data from html and xml files. it works with a parser.
import bs4.element
import datetime

# BeautifulSoup 객체 생성
def get_soup_obj(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
    res = requests.get(url, headers=headers) # type(res) : <class 'requests.models.Response'> //type(res.text) : <class 'str'>
    soup = BeautifulSoup(res.text, 'lxml') # type(soup) : <class 'bs4.BeautifulSoup'> // 파이썬 표준 라이브러리인 html parser도 있지만 lxml이 더 빠르게 동작

    return soup

#뉴스의 기본정보 가져오기
def get_top3_news_info(sec,sid):
    # 임시이미지
    default_img = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#"
    # 해당 분야 상위 뉴스 목록 주소
    sec_url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=" + sid
    # print("********************************************************")
    print("section url : ", sec_url)

    # 해당 분야 상위 뉴스 HTML 가져오기
    soup = get_soup_obj(sec_url) # soup : sec_url을 request.get한 후 lxml 파서로 파싱하고, 원하는 정보를 뽑아오기 위해 beautifulsoup 라이브러리를 이용하려고 soup 클래스 객체로 변환

    # 해당 분야 상위 뉴스 세 개 가져오기
    news_list3 = []
    lis3=soup.find('ul', class_='type06_headline').find_all("li", limit=3) # 태그 이름이 ul, class속성값이 type06_headline 중에서 다시 태그이름이 li인것을 3개까지 찾기
    # print(lis3)
    for li in lis3:
        # title : 뉴스 제목, news_url : 뉴스 url, image_url : 이미지 url
        # news_info : 딕셔너리, 각 기사마다의 정보를 저장해놓은 새로운 딕셔너리
        news_info = {
            "title": li.img.attrs.get('alt') if li.img
            else li.a.text.replace("\n", "").replace("\t", "").replace("\r", ""),
            "date": li.find(class_="date").text,
            "news_url": li.a.attrs.get('href'),
            "image_url": li.img.attrs.get('src') if li.img else default_img
        }
        #print(news_info)
        news_list3.append(news_info)
    
    # print("//////////////////////////////////////////////////////////////")
    # print(lis3)
    return news_list3 # news_list3 : 리스트, news_info 딕셔너리를 요소로 갖는 리스트 news_list3 반환

#뉴스 본문 가져오기
def get_news_contents(url):
    soup=get_soup_obj(url) 
    body=soup.find('div',class_="_article_body_contents")

    news_contents=''
    for content in body:
        if type(content) is bs4.element.NavigableString and len(content) > 50:
            #content.strip() : whitepace 제거
            # 뉴스요약을 위하여 '.'마침표 뒤에 한칸을 띄워 문장을 구분하도록 함
            news_contents += content.strip() + ''
    return news_contents

#'정치', '경제', '사회' 분야의 상위 세 개 뉴스 크롤링
def get_naver_news_top3():
    #뉴스 결과를 담아낼 dictionary
    news_dic=dict() # dic, list : 가변 데이터 타입, 나중에 언제든지 데이터를 추가할 수 있음 // tuple : immutable
            
    #sections : '정치','경제','사회'
    sections=["pol","eco","soc"]
    #section_ids : url에 사용될 뉴스 각 부문 id
    section_ids=["100","101","102"]

    for sec, sid in zip(sections,section_ids): #for 변수 in zip(,,) : 변수에 pair로 묶거나, sec,sid처럼 각각 변수를 지정해도 됨.
        #뉴스의 기본 정보 가져오기
        news_info=get_top3_news_info(sec,sid) # news_info : 리스트, news_info 딕셔너리를 요로소 갖는 news_list3 반환됨
        #print(news_info)
        for news in news_info: # news : 딕셔너리, 리스트 news_info의 요소
            #뉴스 본문 가져오기
            news_url=news['news_url'] # news_url은 각 기사마다의 주소.
            news_contents=get_news_contents(news_url) # 기사 url을 다시 요청하여 contents 가져옴

            #뉴스 정보를 저장하는 dictionary를 구성
            news['news_contents']=news_contents

        news_dic[sec]=news_info

    return news_dic # news_dic : 딕셔너리, [key]=section, [value]= 리스트, section별 기사 3개에 대한 정보를 각각 딕셔너리 요소로 가지고 있음

#함수 호출 - '정치', '경제', '사회' 분야의 상위 세개 뉴스 크롤링
news_dic=get_naver_news_top3()
#경제의 첫번째 결과 확인하기
print("-------------------------------------------------------------")
# print(news_dic)
print(news_dic['eco'][0])