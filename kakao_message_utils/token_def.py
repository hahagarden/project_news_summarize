import json
import requests
import datetime
import os


# 토큰 발급하기
def request_tokens(app_key, authorization_code):
    url = "https://kauth.kakao.com/oauth/token"  # 사용자 토큰 발급용 url

    data = {
        "grant_type": "authorization_code",
        "client_id": app_key,  # REST_API
        "redirect_uri": "https://localhost.com",
        "code": authorization_code,  # 인증코드: request_tokens 실행할때마다 새로 발급받아야함
    }

    response = requests.post(url, data=data)  # 검색(사용자 토큰 발급 요청)

    # 요청에 실패했다면,
    if response.status_code != 200:
        print("error! because ", response.json())
        tokens = None
    else:  # 성공했다면,
        tokens = response.json()  # tokens변수에 담기
        print(tokens)
    # 토큰 발급에 성공했다면 다시 인증코드를 발급받을 필요가 없음. 이제부터 계속 token사용하면 됨. token 잘 관리하기.
    return tokens


# 토큰 관리하기
# 저장하는 함수
def save_tokens(filename, tokens):
    with open(filename, "w") as f:
        json.dump(tokens, f)


# 읽어오는 함수
def load_tokens(filename):
    with open(filename) as f:
        tokens = json.load(f)

    return tokens


# refresh_token으로 access_token 갱신하는 함수
def update_tokens(app_key, filename):
    tokens = load_tokens(filename)

    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": app_key,
        "refresh_token": tokens["refresh_token"],
    }
    response = requests.post(url, data=data)

    # 요청에 실패했다면,
    if response.status_code != 200:
        print("error! because ", response.json())
        tokens = None
    else:  # 성공했다면,
        print(response.json())
        # 기존파일 백업
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename + "." + now
        os.rename(filename, backup_filename)
        # 갱신된 토큰 저장
        tokens["access_token"] = response.json()["access_token"]
        save_tokens(filename, tokens)

    return tokens
