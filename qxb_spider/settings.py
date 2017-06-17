# -*- coding: utf-8 -*-

# Scrapy settings for qxb_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qxb_spider'

SPIDER_MODULES = ['qxb_spider.spiders']
NEWSPIDER_MODULE = 'qxb_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qxb_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qxb_spider.middlewares.QxbSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'qxb_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'qxb_spider.pipelines.QxbSpiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
COOKIE = {'tencentSig': '8738658304', 'aliyungf_tc': 'AQAAAOMdTTLkMAkAIpxA38mZ0O3OBfQM', 'sid': 's%3AATwJfFARrMyerHnXYlAgE5zxw2Is1zDy.ThvjghG07WiLRlDJ4HBpfk2tvVx6XK%2BZNzphob5zCI0', '_qddamta_800809556': '3-0', 'responseTimeline': '20', '_zg': '%7B%22uuid%22%3A%20%2215caad30d41afb-0b5a4fdaf26b42-30637509-13c680-15caad30d42296%22%2C%22sid%22%3A%201497696864.608%2C%22updated%22%3A%201497700733.954%2C%22info%22%3A%201497514577227%2C%22cuid%22%3A%20%221b121b06-d0fa-4b23-86e9-a8b271b511be%22%7D', 'Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71': '1497576841,1497671575,1497693087,1497700731', 'Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71': '1497700734', '_qddaz': 'QD.plzkcz.co2edw.j3y5ij7b', '_qdda': '3-1.24f6qd', '_qddab': '3-eu1sju.j418cgac'}
LOG_LEVEL = "DEBUG"