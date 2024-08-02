import pytest
from conftest import driver_setup
from pages.article import Article

# TODO Исправить неправильный вывод количества артиклей сегодня, за пос 30 дней, и артиклей, в которых упоминаются коты

@pytest.fixture
def article_page(driver_setup):
    driver_setup.get("https://habr.com/ru/articles/")
    article_obj = Article(driver_setup)
    return article_obj

def test_articles_today(article_page):
    articles_today = article_page.get_articles_today()
    assert len(articles_today) > 0, "No articles for today"
    print(len(articles_today))

def test_articles_last_30_days(article_page):
    articles_last_30_days = article_page.get_articles_last_30_days()
    assert len(articles_last_30_days) > 0, "No articles for the last 30 days"
    print(len(articles_last_30_days))

def test_articles_with_cats_last_30_days(article_page):
    articles_with_cats_last_30_days = article_page.get_articles_with_cats_last_30_days()
    assert len(articles_with_cats_last_30_days) > 0, "No articles with cats for the last 30 days"
    print(len(articles_with_cats_last_30_days))