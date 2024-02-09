import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self):
        pass

    def scrape_webpage(self,url):
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            page_body_content = ""
            page_body = soup.find('div', class_='page-body') 
            if page_body:
                section_tags = page_body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'address', 'ol', 'ul', 'li'])
                for section in section_tags:
                    page_body_content += section.get_text() + "\n"
                    page_body_content += "=====\n" 
            
            page_footer_content = ""
            page_footer = soup.find('div', class_='page-footer') 
            if page_footer:
                page_footer_content = page_footer.get_text()
            
            return page_body_content, page_footer_content
        else:
            print(f"Failed to retrieve webpage: {url}")
            return None, None
        
    
    
    def save_webpage(self):
    
        urls = [
        'https://thinkbyte.ai/',
        'https://thinkbyte.ai/solutions/marketing/',
        'https://thinkbyte.ai/solutions/analytics/'
        ]
        for i, url in enumerate(urls):
            content = ''
            filepath = rf"D:\Website-Chatbot-Mistral7b-RAG-App\artifacts\{i}.txt"
            print(f"Scraping content from: {url}")
            page_body_content, page_footer_content = self.scrape_webpage(url)
            content += page_body_content
            content += page_footer_content
            try:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(content)
            except Exception as e:
                    print("Error:", e)


