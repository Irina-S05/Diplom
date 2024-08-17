import configuration
import requests
import data

# Определение функции создания нового заказа
def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
print()

# Вызов функции для создания нового пользователя из модуля data

order_response = post_new_order(data.order_body)

# Запрос на получение заказа по треку заказа
def get_order(track_order):
    return requests.get(configuration.URL_SERVICE+configuration.GET_TRACK_PATH,
                        params=track_order)
