import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text()) #텍스트만 가져오기
# print(soup.a) #soup객체에서 처음 발견되는 a태그 바로 접근
# print(soup.a.attrs) #속성정보
# print(soup.a["href"]) #a element의 href 속성의 파라미터 값

# print(soup.find("a",attrs={"class":"Nbtn_upload"})) # class = "Nbtn_upload 인 a element를 찾아줘"
# print(soup.find(attrs={"class":"Nbtn_upload"})) #class = "Nbtn_upload"인 어떤 element를 찾아줘
# print(soup.find("li",attrs={"class":"rank01"}))
rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") #개행이 있든말든 li에 해당하는 걸 찾음
# rank1 = rank2.find_previous_sibling("li")
# print(rank1.find_next_siblings("li"))
webtoon = soup.find("a", text="여기에 해당")  # 여기에 해당 에 해당하는 값을 가져옴


