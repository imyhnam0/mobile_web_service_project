import requests

HOST = "http://127.0.0.1:8000"

res = requests.post(
    f"{HOST}/api-token-auth/",
    {
        "username": "yunhyungnam",   
        "password": "1234",     
    }
)
res.raise_for_status()
token = res.json()["token"]
print("토큰:", token)

headers = {
    "Authorization": f"Token {token}", 
    "Accept": "application/json",
}

# 3. 새 Post 작성
data = {
    "author": 1,
    "title": "API내 글",
    "text": "Python requests로 업로드 테스트",
    "created_date": "2025-09-27T18:34:00+09:00",
    "published_date": "2025-09-27T18:34:00+09:00",
}
file = {"image": open("/Users/yunhyungnam/Downloads/2.jpeg", "rb")}

res = requests.post(f"{HOST}/api_root/Post/", data=data, files=file, headers=headers)
print("응답 코드:", res.status_code)
print("응답 JSON:", res.json())
