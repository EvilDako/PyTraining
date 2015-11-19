__author__ = 'dako'

import random

def test_add_contact_in_group(app):
    #yужно получить список групп из выпадающего списка, сделать проверку, если групп нет, надо создать
    groups = app.contact.get_group_list_from_contact_page()
    app.contact.open_contact_list()
    #индекс контакта сделать рандомным
    app.contact.select_contact_by_index(index=3)
    group = random.choice(old_groups)

    #в качестве имени группы передаем случайное значение из списка полученных групп, берем пока первое совпадение
    app.contact.add_to_group(group='new_name')

    #выбрать контакт по id или индексу
    #вызвать метод add_to_group
    #выполнить проверки - проверить, что контакт добавился в выбранную группу
    #выполнить поиск контакта по id на странице с контактами выбранной группы, должен быть