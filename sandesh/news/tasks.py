# your_app/tasks.py
#import os
from celery import shared_task
import time
import requests
#import io  # Import io module
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from django.utils import timezone
from .models import Category, News

@shared_task
def scrape_news():
    try:
        # Path to your Chrome WebDriver executable
        chrome_driver_path = 'D:/Imran/Project/chromedriver.exe'


        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument('log-level=3')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-web-security")  # Disable third-party cookie blocking

        # Create a new Chrome WebDriver instance
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        categories = Category.objects.all()
        
        for category in categories:
            url = category.category_url

            # Use Selenium to get the page content
            driver.get(url)
            time.sleep(2)  # Allow some time for the JavaScript to load
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            all_links = soup.find_all('a')

            links_list = []
            for link in all_links:
                href = link.get('href')
                if href and href.startswith(url):
                    absolute_url = urljoin(url, href).strip()
                    links_list.append(absolute_url)

            unique_list = list(set(links_list))

            for link in unique_list:
                try:
                    # Use Selenium to get the content of each article
                    driver.get(link)
                    time.sleep(5)  # Allow some time for the JavaScript to load
                    linked_html_content = driver.page_source
                    s = BeautifulSoup(linked_html_content, 'html.parser')

                    headings = []
                    boxes1 = s.find_all('div', class_="details-title")
                    for box in boxes1:
                        h1_element = box.find('h1')
                        if h1_element:
                            h1_text = h1_element.text.strip()
                            headings.append(h1_text)

                    boxes2 = s.find_all('div', class_="details-brief")
                    paragraphs = []
                    for box in boxes2:
                        p_elements = box.find_all('p')
                        for p_element in p_elements:
                            p_text = p_element.text.strip()
                            paragraphs.append(p_text)

                    title = headings[0] if headings else "No Title"
                    content = "\n".join(paragraphs)

                    image_url = None
                    image_div = s.find('div', class_="details-img")
                    if image_div:
                        img_element = image_div.find('img')
                        if img_element and img_element.get('src'):
                            image_url = img_element['src']

                    # Save image to the ImageField
                    # image_file = None
                    # if image_url:
                    #     image_response = requests.get(image_url)
                    #     if image_response.status_code == 200:
                    #         image_bytes = image_response.content
                    #         image_name = os.path.basename(image_url)
                            
                    #         # Create a file-like object from the image response content
                    #         image_file = io.BytesIO(image_bytes)
                    #         image_file.name = image_name
                            
                            # Optionally, you can resize the image using PIL if needed
                            # resized_image = Image.open(image_file)
                            # resized_image = resized_image.resize((width, height))
                            # image_file = io.BytesIO()
                            # resized_image.save(image_file, format='JPEG')
                            # image_file.seek(0)

                    if not News.objects.filter(heading=title, news_content=content).exists():
                        News.objects.create(
                            category=category,
                            heading=title,
                            news_content=content,
                            image_url=image_url,
                            url=link,
                            date=timezone.now()
                        )

                except Exception as e:
                    print(f"Error fetching data from {link}: {e}")

        # Close the Selenium driver
        driver.quit()

    except Exception as e:
        print(f"Error during scraping: {e}")
