import requests
from bs4 import BeautifulSoup
import re, time, random
from urllib import parse


def naver_blog_list(list_page):
    blog_id = 'luexr'              # <--- change this to your Naver blog ID!

    for page in range(1, list_page):
        url = f'https://blog.naver.com/PostTitleListAsync.naver?blogId={blog_id}&viewdate=&currentPage={page}&categoryNo=0&parentCategoryNo=&countPerPage=10'
        
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }            
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        url_str = parse.unquote(response.text)
        p = re.compile('"logNo":"\d+"')
        logNos = p.findall(url_str)
        
        # only extract URL
        urls = ""
        for log in logNos:
            post_id = log.split('":"')[1][:-1]
            post_url = f"https://blog.naver.com/{blog_id}/{post_id}"
            urls += f"{post_url}\n"
            
        print(urls)

        if urls == "":
            break

        with open('./url_list.txt', 'a', encoding='utf-8') as f:
            f.write(urls)
    
naver_blog_list(80)
