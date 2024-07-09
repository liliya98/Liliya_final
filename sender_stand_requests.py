# Переплетчикова Лилия, 18-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

# Создание заказа
def create_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE} {configuration.ORDERS_TRACK} {track_number}"
    response = requests.get(get_order_url)
    return response



# Получение данных заказа по треку
    order_response = get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)