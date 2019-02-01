#!/usr/bin/python3
#-*-coding:utf-8-*-
#@File: cronjobs.py
#@Author:duzhongqiu
#@time: 2019-02-01 13:36

import requests
from bs4 import BeautifulSoup
import sqlite3


def getnews():
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    conn = sqlite3.connect('/Users/zqd/PycharmProjects/GeneralAdmin/db.sqlite3')
    cur = conn.cursor()
    for page in range(1,5):
        #print('第%s页正在爬取' % page, '*' * 30)
        url = 'http://cn.dailyeconomic.com/roll/page/' + str(page)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        urllist = soup.find_all('a', attrs={"rel": "bookmark"})
        for url in urllist:
            requrl = url.get('href')
            resp = requests.get(requrl, headers=headers)
            resoup = BeautifulSoup(resp.text, 'lxml')
            titles = resoup.find('h1', class_='entry-title').text
            times = resoup.find('span', class_='entry-meta-date updated').text.strip().split(' ')[0].replace('年',
                                                                                                             '-').replace(
                '月', '-').replace('日', '')
            cls = resoup.find('a', attrs={"rel": "category tag"}).text
            artbody = resoup.find('div', class_='entry-content clearfix')
            # print(str(cls),'-'*20)
            cur.execute("select * from blogs_category where (name='%s')" % str(cls))
            if cur.fetchone():
                pass
            else:
                sqlinsert = "insert into blogs_category (name) values ('%s')" % (str(cls))
                cur.execute(sqlinsert)
                conn.commit()
            cur.execute("select id from blogs_category where (name='%s')" % str(cls))
            for id in cur.fetchall()[0]:
                cur.execute("select * from blogs_blog where (title='%s')" % str(titles))
                if cur.fetchone():
                    #print('文章已存在......', titles)
                    pass
                else:
                    # print(id)
                    #print('爬取中......', titles)
                    sql = "insert into blogs_blog(title,author,content,category_id,image,pub) values ('%s','%s','%s','%s','%s','%s')" % (
                    str(titles), '每日经济', str(artbody), str(id), 'null', times)
                    try:
                        cur.execute(sql)
                        conn.commit()
                    except Exception as e:
                        pass
                        #print('爬取失败......', titles, e)
    conn.close()