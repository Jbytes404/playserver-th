import requests, re, os

urlajx_getpic = "http://playserver.co/index.php/Vote/ajax_getpic/YG-Forest-%E0%B9%80%E0%B8%95%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%A1%E0%B8%A5%E0%B8%B8%E0%B8%A2%E0%B8%9B%E0%B9%88%E0%B8%B2%E0%B8%94%E0%B8%87%E0%B8%94%E0%B8%B4%E0%B8%9A%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%84%E0%B8%94%E0%B9%89-%E0%B9%80%E0%B8%A3%E0%B9%87%E0%B8%A7%E0%B9%86%E0%B8%99%E0%B8%B5%E0%B9%89-14961"
header_ = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
"Accept-Encoding": "gzip, deflate",
"Referer": "http://playserver.in.th/index.php/Vote/prokud/YG-Forest-%e0%b9%80%e0%b8%95%e0%b8%a3%e0%b8%b5%e0%b8%a2%e0%b8%a1%e0%b8%a5%e0%b8%b8%e0%b8%a2%e0%b8%9b%e0%b9%88%e0%b8%b2%e0%b8%94%e0%b8%87%e0%b8%94%e0%b8%b4%e0%b8%9a%e0%b8%81%e0%b8%b1%e0%b8%99%e0%b9%84%e0%b8%94%e0%b9%89-%e0%b9%80%e0%b8%a3%e0%b9%87%e0%b8%a7%e0%b9%86%e0%b8%99%e0%b8%b5%e0%b9%89-14961"
}
requests_id = requests.post(urlajx_getpic, headers=header_)
print(requests_id.text)
imageid = re.search('m":"(.+?)"',requests_id.text)
print(imageid.group(1))

url_image = ("http://playserver.co/index.php/VoteGetImage/"+imageid.group(1))
print(url_image)
requests_pic = requests.post(url_image, headers=header_)
print(requests_pic.content)
imagename = "image.png"
with open(imagename,"wb") as f:
    f.write(requests_pic.content)
