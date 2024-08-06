from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import pytz
import spacy

# Setup spacy model
nlp = spacy.load('ru_core_news_sm')

def contains_cat_mention(text):
    doc = nlp(text.lower())
    cat_lemmas = {'кот', 'кошка', 'кошки', 'котики', 'котом'}
    for token in doc:
        if token.lemma_ in cat_lemmas:
            return True
    return False


class Article:
    article_by_CSS = (By.CSS_SELECTOR, "article.tm-articles-list__item:not(.tm-voice-article)")
    time_by_TAG_NAME = (By.TAG_NAME, "time")
    title_by_CSS = (By.CSS_SELECTOR, "h2.tm-title a.tm-title__link")
    next_page_by_CSS = (By.CSS_SELECTOR, "a.tm-pagination__navigation-link[data-pagination-next='true']")
    disabled_next_page_by_CSS = (By.CSS_SELECTOR, "div.tm-pagination__navigation-link[data-pagination-next='true']")

    def __init__(self, driver):
        self.driver = driver

    def _get_articles_on_current_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.article_by_CSS))
        articles = self.driver.find_elements(*self.article_by_CSS)
        articles_info = []
        for article in articles:
            try:
                date_time_str = article.find_element(*self.time_by_TAG_NAME).get_attribute("datetime")
                title = article.find_element(*self.title_by_CSS).text
                articles_info.append((date_time_str, title))
            except Exception as e:
                print(f"Error locating elements in article: {article.get_attribute('outerHTML')}, Error: {e}")
                continue
        return articles_info

    def _go_to_next_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".tm-pagination"))
            )
            # Check if the "Next" button is disabled
            if self.driver.find_elements(*self.disabled_next_page_by_CSS):
                # Next page button is disabled. The last page has reached
                return False

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.next_page_by_CSS))
            next_page = self.driver.find_element(*self.next_page_by_CSS)
            next_page.click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.article_by_CSS))
            return True
        except Exception as e:
            print(f"Could not go to the next page: {e}")
            return False

    def get_articles_today(self):
        articles_today = []
        today = datetime.datetime.now(pytz.timezone('Europe/Moscow')).date()

        while True:
            articles = self._get_articles_on_current_page()
            for date_time_str, title in articles:
                article_date = datetime.datetime.fromisoformat(date_time_str[:-1]).astimezone(
                    pytz.timezone('Europe/Moscow')).date()
                if article_date == today:
                    articles_today.append(title)
                else:
                    # Since articles are sorted by date no need to continue
                    return articles_today

            if not self._go_to_next_page():
                break

        return articles_today

    def get_articles_last_30_days(self):
        articles_last_30_days = []
        today = datetime.datetime.now(pytz.timezone('Europe/Moscow')).date()
        last_30_days = today - datetime.timedelta(days=30)

        while True:
            articles = self._get_articles_on_current_page()
            for date_time_str, title in articles:
                article_date = datetime.datetime.fromisoformat(date_time_str[:-1]).astimezone(
                    pytz.timezone('Europe/Moscow')).date()
                if last_30_days <= article_date <= today:
                    articles_last_30_days.append(title)
                else:
                    return articles_last_30_days

            if not self._go_to_next_page():
                break

        return articles_last_30_days

    def get_articles_with_cats_last_30_days(self):
        articles_last_30_days = self.get_articles_last_30_days()
        articles_with_cats = [article for article in articles_last_30_days if contains_cat_mention(article)]
        return articles_with_cats
