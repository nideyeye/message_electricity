import requests, re
from bs4 import BeautifulSoup
class Beijixin:
    def __init__(self):
        self.main_url = 'http://news.bjx.com.cn/list?page='
        self.headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',}
    def get_page(self, num=None):
        if num == None:
            num=1
        web_data = requests.get(self.main_url+str(num), headers=self.headers, timeout=5)
        return web_data.content
    def parse_page(self, web_data):
        soup = BeautifulSoup(web_data, 'lxml')
        details = soup.find('div',class_="list_left")
        details = details.find_all('a', attrs={'title':True, 'href':re.compile('http')})
        result = {}
        for i in details:
            title = re.sub('\\.', '\u002E', i['title'])
            url = i['href']
            result[title] = url
        return result
    def run(self,num=None):
        web_data = self.get_page(num)
        result = self.parse_page(web_data)
        return result
if __name__ == '__main__':
    test = Beijixin()
    print(test.run(2))