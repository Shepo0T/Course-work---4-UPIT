import requests
from requests import Response
from src.Abstraction import HH_ApiAbstract


class HH(HH_ApiAbstract):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.vacancies = []
        self.params = {"text": "", "per_page": ""}

    def get_response(self, keyword: str, per_page: int ) -> Response:
        self.params['text'] = keyword
        self.params['per_page'] = per_page
        return requests.get(self.url, params=self.params)

    def get_vacancies(self, keyword: str, per_page: int):
        return self.get_response(keyword, per_page).json()['items']
