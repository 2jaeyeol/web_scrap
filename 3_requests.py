import requests
res = requests.get("http://naver.com")
res.raise_for_status()

print("응답코드 : ",res.status_code) #200이면 정상

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
  f.write(res.text)

# if res.status_code == requests.codes.ok:
#   print("정상입니다.")
# else:
#   print("문제가 생겼습니다. [에러코드 :", res.status_code, "]")

