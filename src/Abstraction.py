from abc import ABC, abstractmethod

class HH_ApiAbstract(ABC):
    @abstractmethod
    def get_response(self, keyword, per_page):
        pass
    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        pass


class Creat_JsonAbstract(ABC):

    @abstractmethod
    def write(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass
