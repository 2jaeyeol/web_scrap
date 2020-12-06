import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&m=&q=2018%20%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&nzq=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=NSJ"
headers = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
res = requests.get(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"})
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


images = soup.find_all("img", attrs = {"class" : "thumb_img"})

for image,index in enumerate(images):
  # print(image["src"])
  image_url = image["src"]
  if image_url.startswith("//"):
    image_url = "https:" + image_url

  print(image_url) 
  image_res = requests.get(image_url)
  image_res.raise_for_status()

  with open("movie{}.jpg".format(index+1),"wb") as f:
    f.write(image_res.content)