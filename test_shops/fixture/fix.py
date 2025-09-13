import pytest
import os


@pytest.fixture()
def temp_file_fixture():
    file_path = 'temp_test_file.txt'
    print(f'Фикстура: создаю файл {file_path}')
    with open(file_path,'w') as f:
        f.write('Hello, pytest!')

    yield file_path # тест получает это значение

    print(f'Фикстура удаляет файл {file_path}')
    os.remove(file_path)


def test_read_temp_file(temp_file_fixture):
    file_path = temp_file_fixture # получаем путь к файлу от фикстуры
    print(f'Тест чистаю файл {file_path}')
    with open(file_path, 'r') as f:
        content = f.read()
    assert content == 'Hello, pytest!'





