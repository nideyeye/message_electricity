#！/usr/bin/env python
# _*_coding:utf-8 _*_
import requests, re
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

class SpiderStateGrid():
    def __init__(self):
        self.main_url = 'http://ecp.sgcc.com.cn/project_list.jsp?site=global&column_code=014001001&project_type=1&company_id=&status=&project_name=&pageNo='
        self.headers = {'User-Agent ': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    def get_page(self,page=None):
        if page == None:
            page = 1
            logging.info('使用默认页')
        try:
            logging.debug('开始爬取网站')
            web_data = requests.get(self.main_url+ str(page), headers = self.headers)
            #logging.debug(web_data.text)
            logging.debug('网页爬取成功')
            return web_data.content
        except:
            logging.error('无法打开网页', exc_info=True)
    def parse_web(self, response):
        info_list=[]
        try:
            logging.debug('开始初始化网页')
            soup = BeautifulSoup(response, 'lxml')
            logging.debug('初始化成功，开始解析网页')
            massages = soup.find_all('tr', attrs={'align':'left'})
            for items in massages[1:]:
                item = items.find_all('td',class_="black40")
                status = item[0].get_text().strip()
                number = item[1].get_text().strip()
                title = item[2].a['title']
                date = item[3].get_text().strip()
                url_base = re.search(".*?'(.*?)'.*?'(.*?)'.*?",item[2].a.get('onclick'))
                url = 'http://ecp.sgcc.com.cn/html/project/014001001/'+url_base.group(2)+'.html'
                
                info = {'status':status,'number':number,'title':title,'url': url,'date':date}
                info_list.append(info)
            logging.info('数据存储完毕')    
            logging.debug(info_list)
            return info_list
        except:
            logging.error('解析错误，无法解析网页', exc_info=True)
    def main(self,page=None):
        logging.debug(page)
        logging.info('程序开始执行')
        response = self.get_page(page)
        logging.info('网页爬取完毕开始分析')
        self.parse_web(response)
        logging.info('任务执行完毕')
if __name__ == "__main__":
    test = SpiderStateGrid()
    test.main(3)