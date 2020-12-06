import requests
url = "http://naver.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()

with open("mygoogle.html", "w", encoding="utf8") as f:
  f.write(res.text)


# what is my user agent 접속하는 브라우저마다 다르다 
# 서버 입장에서는 이 정보에 따라 다른 정보를 준다