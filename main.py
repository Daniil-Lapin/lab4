import unittest
from teloflask import app

class TestApp(unittest.TestCase):
    def setUp(self):         #название теста и дальнейшее импортирование unittest и flask из teloflask
        app.testing = True      #устанавливаем флаг тестирование
        self.app = app.test_client()          #создание клиента для тестирования

    def test_index(self):
        response = self.app.get('/')   # запрос к главной странице приложения
        self.assertEqual(response.status_code, 200)   # проверяем, что кодировка HTTP-ответа равна 200

    def test_result_complex(self):
        response = self.app.post('/', data=dict(a='1', b='2', c='3')) #отправка пост запроса и проверка наличия текста
        self.assertIn('Действительные корни отсутствуют', response.data.decode('utf-8'))

    def test_result_single(self):
        response = self.app.post('/', data=dict(a='1', b='6', c='9'))
        self.assertIn('Уравнение имеет единственный корень', response.data.decode('utf-8'))

    def test_result_double(self):
        response = self.app.post('/', data=dict(a='1', b='5', c='6'))
        self.assertIn('Уравнение имеет два корня', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()