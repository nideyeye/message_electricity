import requests, re
from bs4 import BeautifulSoup

main_url = 'http://news.bjx.com.cn/list'
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',}
web_data = requests.get(main_url, headers=headers, timeout=5)
soup = BeautifulSoup(web_data.content, 'lxml')
details = soup.find('div',class_="list_left")
details = details.find_all('a', attrs={'title':True, 'href':re.compile('http')})
result = {}
for i in details:
    title = i['title']
    url = i['href']
    result[title] = url
return result

    
#detail = 