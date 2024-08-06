import pytest
from conftest import driver_setup
from pages.article import Article

@pytest.fixture
def article_page(driver_setup):
    driver_setup.get("https://habr.com/ru/articles/")
    article_obj = Article(driver_setup)
    return article_obj

# def test_articles_today(article_page):
#     articles_today = article_page.get_articles_today()
#     assert len(articles_today) > 0, "No articles for today"
# #     print(f"Total articles today: {len(articles_today)}")
# #     for title in articles_today:
# #         print(f"Title: {title}")

# def test_articles_last_30_days(article_page):
#     articles_last_30_days = article_page.get_articles_last_30_days()
#     assert len(articles_last_30_days) > 0, "No articles for the last 30 days"
# #     print(f"Total articles in the last 30 days: {len(articles_last_30_days)}")
# #     for title in articles_last_30_days:
# #         print(f"Title: {title}")

# def test_articles_with_cats_last_30_days(article_page):
#     articles_with_cats_last_30_days = article_page.get_articles_with_cats_last_30_days()
#     assert len(articles_with_cats_last_30_days) > 0, "No articles with cats for the last 30 days"
#     # print(f"Total articles with cats in the last 30 days: {len(articles_with_cats_last_30_days)}")
#     # for title in articles_with_cats_last_30_days:
#     #     print(f"Title: {title}")
