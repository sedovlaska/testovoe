import pytest
from http import HTTPStatus
from tests import constants


@pytest.mark.api
class TestMainPage:

    def test_success_get_data_by_valid_bin(self, custom_client):
        response = custom_client.send_request(
            view_name='index',
            query_params={'get_data': constants.valid_bank_bin['bin']},
        )
        assert 'Запись найдена' in response
        for key, value in constants.valid_bank_bin.items():
            assert key in response
            assert value in response

    @pytest.mark.parametrize('field_value', constants.bad_bins)
    def test_failure_get_data_by_invalid_bin(self, custom_client, field_value):
        response = custom_client.send_request(
            view_name='index',
            query_params={'get_data': field_value},
            expected_status=HTTPStatus.BAD_REQUEST
        )
        assert f'Запись не найдена' in response

    def test_form_on_page(self, custom_client):
        response = custom_client.send_request(
            view_name='index',
        )
        assert 'Bank bin:' in response
        assert constants.input_field in response
        assert constants.button in response
