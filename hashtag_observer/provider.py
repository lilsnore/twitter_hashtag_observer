import time
from twitter_scraper import get_tweets

__SLEEP_SECONDS__ = 10


class HashtagRequest:

    def __init__(self, hashtag: str, pages=25):
        assert hashtag is not None and type(hashtag) == str, f"Provided " \
                                                            f"hashtag " \
                                                            f"{hashtag}" \
                                                            "is not valid"
        self._pages = pages
        self._hashtag = f"#{hashtag}"
        self._tweets = get_tweets(self._hashtag, pages=pages)
        self._urls = set()

    @staticmethod
    def _get_images_url(tweet: dict):
        return tweet["entries"]["photos"]

    def reset_tweets(self):
        self._tweets = get_tweets(self._hashtag, pages=self._pages)

    def already_provided(self, url: str):
        return url in self._urls

    def get_urls(self, number: int):
        urls = list(self._get_generator()())
        if len(urls) >= number:
            return urls[:number]
        return urls + [None] * (number - len(urls))

    def _get_generator(self):
        def images():
            for tweet in self._tweets:
                for url in self._get_images_url(tweet):
                    if self.already_provided(url):
                        continue
                    self._urls.add(url)
                    yield url
        return images

    def get_images_nonstop(self):
        '''Warning: Don't try to convert this generator into any sequence'''
        images = self._get_generator()
        while True:
            try:
                yield next(images())
            except StopIteration:
                self.reset_tweets()
                next_image = self._get_generator()
                time.sleep(__SLEEP_SECONDS__)
