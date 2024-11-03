import requests
import allure
from data import Url, Flags


class TestOrdersList:

    @allure.title('Test get order list. Handle:/api/v1/orders')
    def test_successful_get_order_list(self):
        response = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}')
        assert response.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()
