from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse
from CAWPspider.items import SiteData
#from .gs_utils import upload_blob, download_blob
import html2text


class CandidateSpider(CrawlSpider):
    name="candidate"

    def __init__(self, *args, **kwargs):
        url=kwargs['url']
        #BUCKET_NAME=kwargs['BUCKET_NAME']
        #REMOTE_BLOB_NAME=kwargs['REMOTE_BLOB_NAME']
        url_domain=urlparse(url).netloc
        self.start_urls=[url]
        self.allowed_domains=[url_domain]
        #self.rules=[Rule(LinkExtractor(allow=r'.*'),callback='parse_links', follow=False, cb_kwargs={'url': url,'BUCKET_NAME':BUCKET_NAME, 'REMOTE_BLOB_NAME': REMOTE_BLOB_NAME})]
        self.rules=[Rule(LinkExtractor(allow=r'.*'),callback='parse_links', follow=False, cb_kwargs={'url': url})]

        #upload_blob(BUCKET_NAME,"",REMOTE_BLOB_NAME)
        super().__init__(*args, **kwargs)


    #def parse_links(self,response,url,BUCKET_NAME,REMOTE_BLOB_NAME):
    def parse_links(self,response,url):
        sitedata=SiteData()
        sitedata['url']=url
        sitedata['text']=response.text
        #text=download_blob(BUCKET_NAME,REMOTE_BLOB_NAME).decode('utf-8')
        #textfile=text+"\n"+cleanhtml
        #upload_blob(BUCKET_NAME,textfile,REMOTE_BLOB_NAME)
        with open('tempscrapy.html','at') as fout:
            fout.write(sitedata['text'])
        return sitedata	
