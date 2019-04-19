# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotesbotItem
from urllib.parse import urljoin

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'my_spider'
    main_url = 'https://scc.pku.edu.cn';
    start_urls = [
        'https://scc.pku.edu.cn/home!recruitList.action?category=2',
        # name: pageNo: 3
    ]
    Form_url = start_urls[0];

    def parse(self, response):
        rows = response.xpath('//*[@id="articleList-body"]/tr')
        source = response.xpath('//*[@id="home-footer"]/div/div[1]/div[1]/span/text()').extract_first().strip();
        for index, row in enumerate(rows):
            if (index > 0):
                item = QuotesbotItem();
                item_url = row.xpath('./td[2]/a/@href').extract_first()
                link_url = urljoin(self.main_url, item_url);
                item = {
                    'title': row.xpath('./td[2]/a/text()').extract_first(),
                    'link':link_url,
                    'release_time': row.xpath('./td[3]/text()').extract_first().strip(),
                    'source': source
                }
                #yield item;
                yield scrapy.Request(link_url, meta={'item': item},callback=self.link_item);
                #yield item;
        next_page_url = response.xpath(' // *[ @ id = "content1"] / tr / td / div / a[3]/@href').extract_first()
        """
        CurPage = response.xpath('//*[@id="articleList"]/tfoot/tr/td/ul');
        CurPage = int(CurPage);
         if (CurPage < 4):
            if next_page_url is not None:
                # yield scrapy.Request(response.urljoin(next_page_url))
                myFormData = {'name': '', 'pageNo': str(CurPage + 1)};
                # 自定义信息，向下层响应(response)传递下去
                customerData = {'pageNo': '2'};
                yield scrapy.FormRequest(url=self.Form_url,
                                         method='POST',  # GET or POST
                                         formdata=myFormData,  # 表单提交的数据
                                         meta=customerData,  # 自定义，向response传递数据
                                         callback=self.parse,
                                         errback=self.error_handle,
                                         # 如果需要多次提交表单，且url一样，那么就必须加此参数dont_filter，防止被当成重复网页过滤掉了
                                         dont_filter=True)
        """

    def get_link_item(self,response):
        item = response.meta['item']
        image = response.xpath('//*[@id="Image1"]/@src').extract_first();
        item['image'] = image;
        #zx = zxing.BarCodeReader();
        #zxdata = zx.decode(image);
        yield item;

    def link_item(self, response,item=None):
        result = response.xpath('//*[@class="articleKeyInfo"]');
        xuanjianghui_time ='';
        xuanjianghui_location='';
        if(len(result)>0):
            xuanjianghui_time = result.xpath('./p[2]/span[2]/text()').extract_first().strip()
            xuanjianghui_location = result.xpath('./p[3]/span[2]/text()').extract_first().strip();
        #image = response.xpath('//*[@id="yc_new"]/div/table/tbody/tr[7]/td[2]/iframe/');
        item = response.meta['item']
        item['xuanjiang_time'] =xuanjianghui_time;
        item['xuanjiang_location'] = xuanjianghui_location;
        yield item;

    def error_handle(self, response):
        print(response);
