import requests
import re
import time
import threading
import os
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}
chapter_link=requests.get('https://manhua.fzdm.com/39/',headers=headers)
chapter_link_get=re.findall('<a href="([^<]*?)" title="(进击的巨人.*?)">',chapter_link.text)
g_lock=threading.Lock()
os.makedirs('进击的巨人')
class downloadpic(threading.Thread):
    def run(self):
        global chapter_link_get
        while len(chapter_link_get>0):
            g_lock.acquire()
            url,title=chapter_link_get.pop()
            g_lock.release()
            if not os.path.exists('进击的巨人\%s'%title):
                os.makedirs('进击的巨人\%s'%title)
            url='https://manhua.fzdm.com/39/%s'%url
            try:
                cover=requests.get(url)
                a=re.findall('<script type="text/javascript">var Title="进击的巨人.*?话";var Clid="39";var mhurl="(.*?)"',cover.text)
            
            
            



    
