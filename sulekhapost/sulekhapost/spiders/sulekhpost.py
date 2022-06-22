from pickle import APPEND
from attr import s
import scrapy

class PostSpider(scrapy.Spider):
    name = "sulekha"
    
    start_urls = [
        'https://localjobs.sulekha.com/search?q=Developer&l=new-york-metro-area&cm=metro'
        'https://localjobs.sulekha.com/full-time-java-developer-job-in-magnus-technologies-for-freshers_hayward-ca_1478075',
        'https://localjobs.sulekha.com/full-time-software-developer-job-in-protalent-it-services-for-freshers_hayward-ca_1513772',
        'https://localjobs.sulekha.com/0-to-9-years-experience-net-developer-job-from-top-level-consultancy_philipsburg-mt_1577387',
        'https://localjobs.sulekha.com/0-to-32-years-experience-java-backend-developer-job-from-top-level-consultancy_new-york-ny_1577645',
        'https://localjobs.sulekha.com/0-to-10-years-experience-hiring-j2ee-developer-job-in-magnus-technologies_aurora-il_1558667',
        'https://localjobs.sulekha.com/0-to-10-years-experience-j2ee-developer-job-in-magnus-technologies_fargo-nd_1558994',
        'https://localjobs.sulekha.com/0-to-22-years-experience-net-full-stack-developer-job-from-top-level-consultancy_new-york-ny_1579345',
        'https://localjobs.sulekha.com/0-to-18-years-experience-mulesoft-developer-job-from-top-level-consultancy_new-york-ny_1579347',
        'https://localjobs.sulekha.com/0-to-5-years-experience-net-developer-remote-rh-job-from-top-level-consultancy_seattle-wa_1579381',
        'https://localjobs.sulekha.com/0-to-2-years-experience-net-developer-ca-pp-job-from-top-level-consultancy_new-york-ny_1579764',
        'https://localjobs.sulekha.com/0-to-2-years-experience-junior-data-analyst-power-bi-developer-job-in-ellianse-llc_chicago-il_1580217',
        'https://localjobs.sulekha.com/0-to-12-years-experience-java-ui-developer-job-from-top-level-consultancy_new-york-ny_1583774',
        'https://localjobs.sulekha.com/0-to-2-years-experience-java-backend-developer-job-in-magnus-technology-solutions-inc_new-york-ny_1585931',
        'https://localjobs.sulekha.com/0-to-2-years-experience-sql-developer-job-in-magnus-technology-solutions-inc_new-york-ny_1585945',
        'https://localjobs.sulekha.com/0-to-2-years-experience-aws-developer-job-from-top-level-consultancy_new-york-ny_1585965',
        'https://localjobs.sulekha.com/0-to-3-years-experience-dot-net-remote-rm-job-in-magnus-technology-solutions-inc_new-york-ny_1586690',
        'https://localjobs.sulekha.com/0-to-20-years-experience-java-remote-rm-job-in-magnus-technology-solutions-inc_new-york-ny_1586692',
        'https://localjobs.sulekha.com/0-to-2-years-experience-java-ui-developer-remote-ny-np-job-in-magnus-technology-solutions-inc_new-york-ny_1587060',
        'https://localjobs.sulekha.com/full-stack-java-developer-100-remote-tx-np-job-from-top-level-consultancy-for-freshers_texas-city-tx_1587279',
        'https://localjobs.sulekha.com/0-to-2-years-experience-dotnet-developer-100-remote-ny-np-job-from-top-level-consultancy_san-clara-mb_1587258',
        'https://localjobs.sulekha.com/0-to-5-years-experience-junior-python-developer-remote-rh-job-from-top-level-consultancy_hartford-ct_1560881',
        'https://localjobs.sulekha.com/0-to-5-years-experience-sql-developer-ca-pp-remote-job-from-top-level-consultancy_washington-il_1560886',
        'https://localjobs.sulekha.com/0-to-10-years-experience-hadoop-developer-job-in-magnus-technology_cupertino-ca_1560901',
        'https://localjobs.sulekha.com/0-to-13-years-experience-salesforce-developer-remote-ls-job-from-top-level-consultancy_texas-city-tx_1562639',
        'https://localjobs.sulekha.com/0-to-24-years-experience-ui-developer-job-in-magnus-technologies_new-york-ny_1562640',
        'https://localjobs.sulekha.com/0-to-40-years-experience-java-front-end-developer-job-from-top-level-consultancy_new-york-ny_1562647',
        'https://localjobs.sulekha.com/0-to-38-years-experience-java-developer-remote-ls-job-from-top-level-consultancy_new-york-ny_1563726'
        
        
        
        
    ]
    
    def parse(self, response):
        # title = response.css('div.primary-title::text').extract()
        # return title
        # for titles in response.css('h3.title'):
        #     yield{
        #         'title':response.css('a span::text').extract()
        #     }
        #     break
        for post in response.css('article.roomdetail-bg'):
            yield{
                'title':response.css('a span::text').extract(),
                'links':response.css('li a::text').extract(),
                # 'title':response.css('.title a::attr(href)').extract(),
                'descp':''.join(s.strip() for s in response.css('span::text').extract()),
                'skills': response.css('ul.listleft.clearfix li a::text').extract(),
                'table_heading' : response.css('th::text').extract(),  
                'table_data_link': response.css('tr a::text').extract(),
                'table_data':response.css('td::text').extract(),
                'paragraphs':response.css('p::text').extract()
                
                # if {
                #     'paragraphs':response.css('p::text').extract()
                # }
                # else{
                #     'paragraphs':'None'
                # }
                    
            }
            break
            # for post in response.css('div.table'):
            #     yield{
            #         'table_heading': response.css('th::text').extract(),
            #         'table_data': response.css('tr a::text').extract(),
            #         'table_data':''.join(s.append() for s in response.css('td::text').extract())
            #     }
            
        next_page = response.css('.title a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
            
    
        
        
       
        
        