from http import HTTPStatus
from unittest.mock import patch
import pytest


@pytest.mark.api
class TestMockedMainPage:
    valid_mocked_return_value = (
        True,
        {
            'results': ['VISA', 'DEBIT', 'TESTKORT', 'TEST BANK', 'TS',
                        'DNK', 'Denmark', '123.123', '321.321', '880005553535', 'testbank.com'],
            'bin': '333'
        }
    )
    invalid_mocked_return_value = (
        False,
        {'results': None}
    )

    def test_success_get_data_by_mocked_data(self, custom_client):
        with patch('app.utils.get_data_from_csv', return_value=self.valid_mocked_return_value):
            response = custom_client.send_request(
                view_name='index',
                query_params={'get_data': self.valid_mocked_return_value[1]['bin']},
            )
        assert 'Запись найдена' in response
        assert self.valid_mocked_return_value[1]['bin'] in response
        for value in self.valid_mocked_return_value[1]['results']:
            assert value in response

    def test_failure_get_data_by_mocked_data(self, custom_client):
        with patch('app.utils.get_data_from_csv', return_value=self.invalid_mocked_return_value):
            response = custom_client.send_request(
                view_name='index',
                query_params={'get_data': self.invalid_mocked_return_value[1]},
                expected_status=HTTPStatus.BAD_REQUEST
            )
        assert f'Запись не найдена' in response
