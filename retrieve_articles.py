import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.article import Article

def setup_driver():
    driver_path = ChromeDriverManager().install()
    chrome_service = Service(driver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.maximize_window()
    return driver

def save_articles_to_csv(articles, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Date', 'Title', 'Link'])
        for article in articles:
            csvwriter.writerow(article)

def main():
    driver = setup_driver()
    try:
        driver.get("https://habr.com/ru/articles/")
        article_page = Article(driver)
        articles_last_30_days = article_page.get_articles_last_30_days()

        # Save articles to CSV
        save_articles_to_csv(articles_last_30_days, 'articles_last_30_days.csv')
        print(f"Saved {len(articles_last_30_days)} articles to 'articles_last_30_days.csv'.")

    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    main()