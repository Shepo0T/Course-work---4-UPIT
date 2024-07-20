import requests

from src.Abstraction import HH_ApiAbstract

class HH(HH_ApiAbstract):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):

        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.vacancies = []
        
    def get_response(self, keyword, per_page):
        params = {'text': keyword, 'per_page': per_page}
        return requests.get(self.url, params=params)
    
    def get_vacancies(self, keyword, per_page):
        return self.get_response(keyword, per_page).json()['items']