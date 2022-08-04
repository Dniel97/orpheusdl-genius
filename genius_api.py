import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class GeniusApi:
    def __init__(self):
        self.API_URL = "https://api.genius.com/"

        self.access_token = 'ZTejoT_ojOEasIkT9WrMBhBQOz6eYKK5QULCMECmOhvwqjRZ6WbpamFe3geHnvp3'  # anon Android app token

        self.s = requests.Session()

        retries = Retry(total=10,
                        backoff_factor=0.4,
                        status_forcelist=[429, 500, 502, 503, 504])

        self.s.mount('http://', HTTPAdapter(max_retries=retries))
        self.s.mount('https://', HTTPAdapter(max_retries=retries))

    def headers(self, use_access_token=True):
        return {
            'x-genius-app-background-request': '0',
            'user-agent': 'okhttp/4.9.1',
            'authorization': f'Bearer {self.access_token}' if use_access_token else None,
            'x-genius-logged-out': 'true',
            'x-genius-android-version': '5.8.0'
        }

    def _get(self, url: str, params: dict = None):
        r = self.s.get(f'{self.API_URL}{url}', params=params, headers=self.headers())

        if r.status_code not in [200, 201, 202]:
            raise ConnectionError(r.text)

        r = r.json()
        if r['meta']['status'] != 200:
            return None

        return r['response']

    def get_search(self, query: str):
        return self._get('search', {'q': query})['hits']

    def get_search_by_songs(self, query: str, page: int = 1):
        return self._get('search/songs', {'q': query, 'page': page})['sections'][0]['hits']

    def get_song_by_id(self, song_id: str, text_format: str = 'plain'):
        # check if text_format is valid
        valid = {'plain', 'dom', 'html'}
        if text_format not in valid:
            raise ValueError('text_format must be one of %r' % valid)
        return self._get(f'songs/{song_id}', {'text_format': text_format})['song']
