import pytest
from conftest import driver_setup
from pages.article import Article

@pytest.fixture
def article_page(driver_setup):
    driver_setup.get("https://habr.com/ru/articles/")
    article_obj = Article(driver_setup)
    return article_obj

def test_articles_today(article_page):
    assert article_page.check_articles_today(), "No articles for today"

def test_articles_last_30_days(article_page):
    assert article_page.check_articles_last_30_days(), "No articles for the last 30 days"

def test_articles_with_cats_last_30_days(article_page):
    assert article_page.check_articles_with_cats_last_30_days(), "No articles with cats for the last 30 days"
