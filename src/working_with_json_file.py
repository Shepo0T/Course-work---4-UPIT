import json
from src.work_with_vacancies import Vacancies
from src.Abstraction import Creat_JsonAbstract
class CreationJson(Creat_JsonAbstract):
    """Класс для создания json файла"""
    def __init__(self, filename='../data/vacancies.json'):
        self.filename = filename

    def write(self, vacancies):
        with open(self.filename, 'w') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
    def get_vacancies(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancies(name=vacancy['name'],
                                       salary=vacancy['salary'],
                                       alternative_url=vacancy['alternate_url'],
                                       area_name=vacancy['area'],
                                       requirement=vacancy['requirement']))
        return vacancies

    def delete_vacancies(self):
        pass