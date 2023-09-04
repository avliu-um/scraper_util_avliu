import time
from src.scraper_util_avliu import util
import os


def test_get_url(url='https://google.com'):

    driver = util.get_selenium_driver(undetected=True)
    driver.get(url)
    print(driver.page_source)
    time.sleep(5)


def test_write_sqs():
    sqs_queue_id = 'ev_test_sqs_queue'
    message_list = [
        {
            'url': 'https://google.com',
            'platform': 'google'
        },
        {
            'url': 'https://yelp.com',
            'platform': 'yelp'
        }
    ]
    util.write_to_sqs(sqs_queue_id, message_list)


if __name__ == '__main__':
    print(os.getcwd())
    test_write_sqs()
