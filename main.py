<<<<<<< HEAD
import json
import os
from datetime import datetime

from dotenv import load_dotenv

from src.clase_2 import HeadHunterAPI
from src.clase_1 import DBManager

load_dotenv()


# def main():
#
#     # Установка соединения
#
#     dbname='your_database',
#     user='postgres',
#     password='123qweewq321',
#     host='localhost',
#     port='5432'
#
#     bd = DBManager(bd_name=dbname, user=user, password=password)
#     bd.create_tables()
#     # bd.close()


def user_interaction():

    hh_api = HeadHunterAPI()
    # Подключение к базе данных
    db = DBManager(os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"))

    # Проверяем наличие таблиц
    # if not db.tables_exist():
    db.create_tables()
    #     print("Таблицы созданы.")

    # Загружаем компании из JSON
    db.load_companies_from_json("data/companies.json")

    with open("data/companies.json") as f:
        copas = json.load(f)
        for i in copas:
            db.load_vac_from_json(hh_api.get_company_vacancies(i.get("employer_id")))

    while True:
        print("\nДобро пожаловать в систему управления вакансиями!")
        print("Выберите действие:")
        print("1. Показать список компаний и количество вакансий у каждой")
        print("2. Показать все вакансии")
        print("3. Показать среднюю зарплату по вакансиям")
        print("4. Показать вакансии с зарплатой выше средней")
        print("5. Поиск вакансий по ключевому слову")
        print("6. Выйти")
        print("7. Вернутся")

        choice = input("Введите номер действия: ")

        if choice == "1":
            # Показать список компаний и количество вакансий
            companies_and_vacancies = db.get_companies_and_vacancies_count()
            for row in companies_and_vacancies:
                print(f"Компания: {row['name']}, Количество вакансий: {row['vacancies_count']}")

        elif choice == "2":
            # Показать все вакансии
            vacancies = db.get_all_vacancies()
            for vac in vacancies:
                print(
                    f"Компания: {vac['company_name']}, Вакансия: {vac['vacancy_title']}, "
                    f"Зарплата: от {vac['salary_min']} до {vac['salary_max']}, Ссылка: {vac['url']}"
                )

        elif choice == "3":
            # Показать среднюю зарплату
            avg_prise = db.get_avg_salary()
            print(f"Средняя зарплата по всем вакансиям: {avg_prise}")

        elif choice == "4":
            # Показать вакансии с зарплатой выше средней
            above_average = db.get_vacancies_with_higher_salary()
            for a_avg in above_average:
                print(
                    f"Компания: {a_avg['company_name']}, Вакансия: {a_avg['vacancy_title']}, "
                    f"Зарплата: от {a_avg['salary_min']} до {a_avg['salary_max']}, Ссылка: {a_avg['url']}"
                )

        elif choice == "5":
            # Поиск вкансий р=по ключевому слову
            keyword = input("Введите ключевое слова для поиска: ")
            search = db.get_vacancies_with_keyword()
            for sear in search:
                print(
                    f"Компания: {sear['company_name']}, Вакансия: {sear['vacancy_title']}, "
                    f"Зарплата: от {sear['salary_min']} до {sear['salary_max']}, Ссылка: {sear['url']}"
                )

        elif choice == "6":
            # Выйти из программы
            db.close()
            print("Программа завершена.")
            break
=======
from src.api_class_module import (FindEmployerFromHHApi,
                                  FindVacancyFromHHApi)
from src.DBCreate_module import DBConnection
from src.utils import (filter_vacancies, get_top_vacancies,
                       get_vacancies_by_salary, sort_vacancies)
from src.vacancy_class import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = FindVacancyFromHHApi().get_vacancies(
        search_query
    )  # Получение вакансий с hh.ru в формате JSON
    vacancies_list = Vacancy.cast_to_object_list(
        hh_vacancies
    )  # Преобразование набора данных из JSON в список объектов
    top_n = int(input("Введите количество вакансий для вывода N самых оплачиваемых: "))
    filter_words = list(
        input("Введите ключевые слова для фильтрации вакансий: ").split()
    )
    salary_range_from = input("Введите диапазон зарплат от: ")  # Пример: 100000
    salary_range_to = input("Введите диапазон зарплат до: ")  # Пример: 150000
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(
        filtered_vacancies, salary_range_from, salary_range_to
    )
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(top_vacancies)
>>>>>>> origin/CW

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

<<<<<<< HEAD

if __name__ == "__main__":
    user_interaction()
=======
def user_interaction_with_db():
    """Функция для создания, заполнения и взаимодействия пользователя с базой данных вакансий"""
    employer_word = input("Введите слово по которому хотите найти работодателя или оставьте поле пустым:\n")
    employers_count = int(input("Введите топ N (число до 50) ваканский для просмотра:\n"))
    employer_obj = FindEmployerFromHHApi()
    employers = employer_obj.get_employer_info(employers_count, keyword=employer_word)
    db = DBConnection()
    db.create_db()
    db.db_creating_employers()
    employers_id_list = list(input("Введите через запятую id не менее 10 компаний для отслеживания:\n").split(", "))
    db.db_filling_columns_for_emps(employers_id_list, employers)
    db.db_creating_vacancies()
    for emp_id in employers_id_list:
        vacancy_list = FindVacancyFromHHApi().get_vacancies_by_employer_id(emp_id)
        db.db_filling_vacancies(vacancy_list)


if __name__ == "__main__":
    user_interaction_with_db()
>>>>>>> origin/CW
