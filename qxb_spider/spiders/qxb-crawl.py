import scrapy
from scrapy.conf import settings


class QxbCrawl(scrapy.Spider):
    name = "qxb-crawl"
    start_urls = [
        'http://www.qixin.com'
    ]

    cookie = settings['COOKIE']

    def parse(self, response):
        print("first crawl start======================================")
        list_page_url = response.xpath(
            '//div[@class="city-province-items-container last"]/div[@class="city-province-items"]/a/@href').extract()
        for url in list_page_url:
            if url == '/search/prov/AH':
                list_page_url_ah = url
        if list_page_url_ah is not None:
            print("list page url is:" + response.urljoin(list_page_url_ah) + "======================================")
            yield scrapy.Request(response.urljoin(list_page_url_ah), cookies=self.cookie, callback=self.parse_list)

    def parse_list(self, response):
        print("list crawl start======================================")
        for div in response.xpath('//div[@class="search-ent-row"]'):
            detail_page_url = div.xpath(
                './/div[@class="search-result-desc"]/a[@class="search-result-title"]/@href').extract_first()
            if detail_page_url is not None:
                print("detail page url is:" + response.urljoin(detail_page_url) + "===========================")
                yield scrapy.Request(response.urljoin(detail_page_url), cookies=self.cookie, callback=self.parse_detail)

        paging_page_url = response.xpath(
            '//div[@class="oni-pager search-pager"]/a[@class="oni-pager-next"]/@href').extract_first()
        if paging_page_url is not None:
            print("paging url is:" + response.urljoin(paging_page_url) + "======================================")
            yield scrapy.Request(response.urljoin(paging_page_url), cookies=self.cookie, callback=self.parse_list)

    def parse_detail(self, response):
        print("detail crawl start======================================")
        table = response.xpath('//table[@class="table table-bordered word-break"]')
        company_name = response.xpath('//span[@class="company-name-now"]/text()').extract_first()
        tds = table.xpath('.//td')
        base_info_key = []
        base_info_value = []
        base_info = {}
        for index, td in enumerate(tds, start=0):
            td_text = td.xpath('./text()').extract_first()
            if index % 2 == 0:
                base_info_key.append(td_text)
            else:
                if not td_text.strip():
                    base_info_value.append(td.xpath('./a/text()').extract_first())
                else:
                    base_info_value.append(td_text)
        base_info = dict(zip(base_info_key, base_info_value))

        gd_key = []
        gd_info = []
        divs = response.xpath('//div[@id="info"]/div/div[@class="panel panel-default"]')
        print(str(len(divs)) + "==============len(divs)=============")
        if len(divs) < 1:
            return
        gd_div = divs[0]
        ths_text = gd_div.xpath('.//table[@class="table table-bordered"]/thead/tr/th/text()').extract()
        for th in ths_text:
            gd_key.append(th)
        trs = gd_div.xpath('.//table[@class="table table-bordered"]/tbody/tr')
        for tr in trs:
            gd_value = []
            for td in tr.xpath('./td'):
                td_text = td.xpath('./text()').extract_first()
                if td_text is None:
                    ran = td.xpath('./a/span/text()').extract_first()
                    if ran is None:
                        ran2 = td.xpath('./div/span/text()').extract_first()
                        gd_value.append(ran2)
                    else:
                        gd_value.append(ran)
                else:
                    gd_value.append(td_text)

            gd_info.append(dict(zip(gd_key, gd_value)))

        yield {
            "company_name": company_name,
            "base_info": base_info,
            "gd_info": gd_info
        }
