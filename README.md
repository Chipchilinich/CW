Приветствую! Благодаря этой программе ты сможешь получить вакансии с сайта HH.ru от компаний, которые тебя интересуют(companies_id.json). Создать БД и сохранить все данные в таблицы. Благодаря классу DBManager есть возможность работать с этими данными. На выбор 5 вариантов взаимодействия:

1 - вызывая метод 'get_companies_and_vacancies_count' получаем список всех компаний и количество вакансий у каждой компании.

2 - вызывая метод 'get_all_vacancies' получаем список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию

3 - вызывая метод 'get_avg_salary' получаем среднюю зарплату по вакансиям

4 - вызывая метод 'get_vacancies_with_higher_salary' получаем список всех вакансий, у которых зарплата выше средней по всем вакансиям

5 - вызывая метод 'get_vacancies_with_keyword' получаем список всех вакансий по ключевым словам