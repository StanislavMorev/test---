import pytest
"""
Фикстура - это объект, который можно рассматривать, как набор условий 
необходимых тесту для выполнения, например, зачастую фикстуры создаются, чтобы генерировать
какие-то данные еще до теста и возвращать их для использования в тесте или перед тестом,
"""

@pytest.fixture()
def sample_list():
    print('\n Фикстура sample_list: создаю список')
    return [1, 2, 3, 4, 5]


@pytest.fixture()
def sample_dict():
    print('\n Фикстура sample_dict: создаю словарь')
    return {'name':'Alice','age':30}


def test_len_list(sample_list): # имя фикстуры передается как аргумент
    assert len(sample_list) == 5

def test_dict_name(sample_dict):
    assert sample_dict['name'] =='Alice'


def test_list_and_dict(sample_dict,sample_list):
    assert len(sample_list) >0
    assert 'age' in sample_dict

























