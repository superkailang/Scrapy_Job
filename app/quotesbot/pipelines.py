# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .redis.redis_client import redis_client
import json as json
from urllib import request
from urllib import parse

class QuotesbotPipeline(object):
    def __init__(self):
        self.client = redis_client(host='39.105.200.67');
        self.redis_dict = 'joblist';

    def process_item(self, item, spider):
        if(self.key_word_match(item['title'])):
            if(self.client.hexists(self.redis_dict, item['title'])== False):
                # 发送邮件;
                if( self.send_email(item) ):
                    self.client.hset(self.redis_dict, item['title'], json.dumps(item));
                # 发送短信;
            # return item

    def send_email(self,item):
        email_url='http://39.105.200.67:5756/weapp/send_email';
        itemname={
            'title':'暑期实习',
            'release_time':'发布时间',
            'xuanjiang_time':'宣讲时间',
            'xuanjiang_location':'宣讲地点',
            'source': '信息源',
        }
        type='实习'
        html = '<p><br></p>';
        for index,item_name in enumerate(itemname):
            name = itemname[item_name];
            value = item[item_name];
            html = html+ '<p>'+ name + ': '+ value + '</p>'
        html = html + '<p> 链接:</p>'+'<a href="'+item['link']+'" target="_blank"> 实习链接 </a>'
        data = {"subject": item['title'], "text": item['source'],'html':html,"type":type};
        data = parse.urlencode(data).encode('utf-8')
        req = request.Request(email_url, data=data)  # POST方法
        data = request.urlopen(req).read().decode("utf-8")
        data = json.loads(data);
        if(data['code']==0):
            return True;
        return False;

    def key_word_match(self,title):
        keywords=['暑期实习','2020','夏季实习','2019年实习','2019年实习']
        for item in keywords:
            if( title.find(item)>=0):
                return True;
        return False;