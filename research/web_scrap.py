

import requests
from bs4 import BeautifulSoup

# Function to scrape content from page-body and page-footer
def scrape_webpage(url):
    # Fetch the HTML content of the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract content from page-body
        page_body_content = ""
        page_body = soup.find('div', class_='page-body') # Adjust class name accordingly
        if page_body:
            # Extract content from each section tag within page-body
            section_tags = page_body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'address', 'ol', 'ul', 'li'])
            for section in section_tags:
                # Extract text from each section and append to page_body_content
                page_body_content += section.get_text() + "\n"
                page_body_content += "=====\n"  # Add line of equal signs after each tag's text
        
        # Extract content from page-footer
        page_footer_content = ""
        page_footer = soup.find('div', class_='page-footer') # Adjust class name accordingly
        if page_footer:
            page_footer_content = page_footer.get_text()
        
        return page_body_content, page_footer_content
    else:
        print(f"Failed to retrieve webpage: {url}")
        return None, None


urls = [
    'https://thinkbyte.ai/',
    'https://thinkbyte.ai/solutions/marketing/',
    'https://thinkbyte.ai/solutions/analytics/'
]


for i, url in enumerate(urls):
    content = ''
    filepath = f"{i}.txt"
    print(f"Scraping content from: {url}")
    page_body_content, page_footer_content = scrape_webpage(url)
    content += page_body_content
    content += page_footer_content
    if page_body_content and page_footer_content:
        print("Page Body Content:")
        print(page_body_content)
        print("\n" + "=" * 50)  
        print("Page Footer Content:")
        print(page_footer_content)
        print("\n" + "=" * 100)  
    else:
        print("Failed to retrieve content.")
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        print("HTML code saved to:", filepath)
    except Exception as e:
        print("Error:", e)
