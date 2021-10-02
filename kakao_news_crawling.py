from kakao_message_utils import kakao_utils

KAKAO_TOKEN_FILENAME="json/kakao_token.json"
KAKAO_APP_KEY="cc335daa766cc74b3de1b1c372a6cce8"
# kakao_utils.update_tokens(KAKAO_APP_KEY,KAKAO_TOKEN_FILENAME)

sections_ko={'pol':'정치', 'eco':'경제','soc':'사회'}

navernews_url="https://news.naver.com/main/home.nhn"

contents=[]

template = {
    "object_type": "list",
    "header_title": sections_ko[my_section] + " 분야 상위 뉴스 빅3",
    "header_link": {"web_url": "www.naver.com", "mobile_web_url": "www.naver.com"},
    "contents": contents,
    "buttons_title": "네이버 뉴스 바로가기"
}

for news_info in news_list3:
    content={
        "title" : news_info.get('title'),
        "description" : "작성일 : " + news_info.get('date'),
        "image_url" : news_info.get('image_url'),
        "image_width" : 50, "image_height" : 50,
        "link" : {
            "web_url":news_info.get('news_url'),
            "mobile_web_url":news_info.get('news_url')
        }

    }

    contents.append(content)


# 카카오톡 메시지 보내기
res=kakao_utils.send_message(KAKAO_TOKEN_FILENAME,template)
# if failed to request,
if res.status_code != 200:
    print("error! because= ", res.json())
else:  # if succeed,
    print("메시지를 성공적으로 보냈습니다.")
