from abc import ABC, abstractmethod

class HH_ApiAbstract(ABC):
    @abstractmethod
    def get_response(self):
        pass
    @abstractmethod
    def get_vacancies(self):
        pass