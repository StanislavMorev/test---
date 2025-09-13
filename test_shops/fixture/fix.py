import pytest
# облость действие фикстуры scope
@pytest.fixture(scope='session')
def session_db_connection():
    print('\n Фикстура session_db_connection: устанавливаю соединение с БД-1 раз за сессию')
    connection = {'status': 'connected'} # Имитация соединения
    yield connection
    print('\n Фикстура session_db_connection: закрываю соединение с БД -один раз за сессию')


# Фикстура выполняется один раз для каждого модуля.
@pytest.fixture(scope='module')
def module_data_setup(session_db_connection):
    #эта фикстура зависит от session_db_connection
    assert session_db_connection['status'] == 'connected'
    print('\n Фикстура module_data_setup: настраиваю данные для модуля - Один раз за сессию')
    data = {'module_id': 123}
    yield data
    print('\n Фикстура module_data_setup: ощищаю данные модуля')

class TestUserOperations:
    def test_user_create(self, module_data_setup, session_db_connection):
        print("(Тест test_user_create)")
        assert session_db_connection["status"] == "connected"
        assert module_data_setup["module_id"] == 123

    def test_user_view(self, module_data_setup, session_db_connection):
        print("(Тест test_user_view)")
        assert session_db_connection["status"] == "connected"
        assert module_data_setup["module_id"] == 123


def test_another_operation(module_data_setup, session_db_connection):
    print("(Тест test_another_operation в том же модуле)")
    assert session_db_connection["status"] == "connected"
    assert module_data_setup["module_id"] == 123



