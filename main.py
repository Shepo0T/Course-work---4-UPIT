from src.work_with_vacancies import Vacancies
from src.working_with_json_file import CreationJson
from src.HH_Api import HH
from src.utils import user_interface, get_vacancies_by_salary, print_vacancies


def main():
    keyword, range_salary, top_n = user_interface()

    hh_api = HH()
    vacancies = hh_api.get_vacancies(keyword, 50)

    saver = CreationJson()
    saver.write(vacancies)
    sort_by_salary = get_vacancies_by_salary(vacancies, range_salary)
    sorted_vacancies = sorted(sort_by_salary, key=lambda x: x.get('salary').get('from'), reverse=True)
    top_vacancies = sorted_vacancies[:top_n]
    print_vacancies(Vacancies.object_list(top_vacancies))


if __name__ == "__main__":
    main()
