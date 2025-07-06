import requests
import os
from dotenv import load_dotenv

load_dotenv()


class BaseApi:
    def __init__(self, token=None):
        self.base_url = self._get_base_url()
        self.token = token

    def _get_base_url(self):
        base_url = os.getenv('BASE_URL')

        if not base_url:
            raise ValueError("BASE_URL должен быть задан в .env файле")

        return base_url.rstrip('/')

    def _prepare_headers(self, headers=None):
        headers = dict(headers) if headers else {}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'

        return headers

    def _prepare_url(self, url):
        return f'{self.base_url}/{url.lstrip("/")}'

    def _request(self, method, url, *args, **kwargs):
        headers = kwargs.pop('headers', None)
        kwargs['headers'] = self._prepare_headers(headers)
        full_url = self._prepare_url(url)

        return requests.request(method, full_url, *args, **kwargs)

    def get(self, url, *args, **kwargs):
        return self._request('GET', url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        return self._request('POST', url, *args, **kwargs)

    def patch(self, url, *args, **kwargs):
        return self._request('PATCH', url, *args, **kwargs)
