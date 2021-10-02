import token_def

# To get Authorization Code
# https://kauth.kakao.com/oauth/authorize?client_id=cc335daa766cc74b3de1b1c372a6cce8&response_type=code&redirect_uri=https://localhost.com

KAKAO_APP_KEY = "cc335daa766cc74b3de1b1c372a6cce8"  # REST_API app key
AUTHORIZATION_CODE = "flzXSvhelQ3LLzmAKyo5-bQsafEyGOyFAMyK4N-dTii5B-SxG3-KimikA5vq0zD1ChZ_jQo9dVsAAAF8OjRb-g"  # once in a run
KAKAO_TOKEN_FILENAME = "/Users/jeongwon/Documents/GitHub/project_news_summarize/json/kakao_token.json"  # Token in this file(.json)

# To get Access Token
tokens = token_def.request_tokens(KAKAO_APP_KEY, AUTHORIZATION_CODE)

# To save Access Token in the file(.json)
token_def.save_tokens(KAKAO_TOKEN_FILENAME, tokens)

# # To update Refresh Token after the Access Token is expired
# tokens=token_def.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
# token_def.save_tokens(KAKAO_TOKEN_FILENAME, tokens)
