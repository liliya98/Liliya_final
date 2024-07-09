import data
import sender_stand_requests

# Автотест
def test_order_creation_and_retrieval():
    response = sender_stand_requests.create_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

