import sendor_stand_request
import data


def get_new_track(order_response):
    return order_response.json().get("track")

data.params_get["t"] = get_new_track(sendor_stand_request.order_response)

# Тест
def positive_assert():
    track_response = sendor_stand_request.get_order(data.params_get)
    assert track_response.status_code == 200

def test_order():
    positive_assert()

# Ирина Степанова, 20-я когорта — Финальный проект. Инженер по тестированию плюс