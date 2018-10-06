#！/usr/bin/env python
# _*_coding:utf-8 _*_
import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)

class Spiderdayin():
    def __init__(self):
        self.main_url = 'http://ecp.sgcc.com.cn/project_list.jsp?site=global&column_code=014001001&project_type=1&company_id=&status=&project_name=&pageNo='
        self.page = 1
        self.headers = {'User-Agent ': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    def get_page(self,page=None):
        if page == None:
            page = self.page
        else:
            try:
                web_data = requests.get(self.main_url+ str(page), headers = self.headers)
                self.parse_web(web_data)
            except:
                logging.debug('无法打开网页')
    def parse_web(self, response):
        try:
            soup = BeautifulSoup(response.content, 'lxml')

        except:
            logging.debug('解析错误，无法解析网页')
