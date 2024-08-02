from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


class Article:

    time_by_CSS = (By.CSS_SELECTOR, "article.tm-articles-list__item")
    time_by_TAG_NAME = (By.TAG_NAME, "time")

    def __init__(self, driver):
        self.driver = driver

    def get_articles_today(self):
        articles_today = []
        today = datetime.datetime.now().date()
        articles = self.driver.find_elements(*self.time_by_CSS)

        for article in articles:
            date_time_str = article.find_element(*self.time_by_TAG_NAME).get_attribute("datetime")
            article_date = datetime.datetime.fromisoformat(date_time_str[:-1]).date()
            if article_date == today:
                articles_today.append(article.text)

        return articles_today

    def get_articles_last_30_days(self):
        articles_last_30_days = []
        today = datetime.datetime.now().date()
        last_30_days = today - datetime.timedelta(days=30)
        articles = self.driver.find_elements(*self.time_by_CSS)

        for article in articles:
            date_time_str = article.find_element(*self.time_by_TAG_NAME).get_attribute("datetime")
            article_date = datetime.datetime.fromisoformat(date_time_str[:-1]).date()
            if last_30_days <= article_date <= today:
                articles_last_30_days.append(article.text)

        return articles_last_30_days

    # TODO подумать как коты будут проверяться
    def get_articles_with_cats_last_30_days(self):
        articles_last_30_days = self.get_articles_last_30_days()
        articles_with_cats = [article for article in articles_last_30_days if " кот " or "Кот " in article.lower()]
        return articles_with_cats
