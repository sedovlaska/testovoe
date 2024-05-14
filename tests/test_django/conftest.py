import pytest
from django.test import Client
from django.http import HttpResponse
from django.urls import reverse
from http import HTTPStatus
from typing import Dict, Any
from enum import Enum


@pytest.fixture()
def custom_client():
    return CustomClient()


def decode_response(response):
    return response.content.decode('utf-8')


class RequestType(Enum):
    POST = 'post'
    GET = 'get'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'


class CustomClient(Client):
    def send_request(
            self,
            view_name: str,
            data: Dict[str, Any] = None,
            expected_status: HTTPStatus = HTTPStatus.OK,
            request_type: RequestType = RequestType.GET,
            reverse_kwargs: Dict[str, Any] = None,
            format='json',
            query_params: Dict[str, Any] = None,
            additional_error_msg: str = None,
            headers: Dict[str, Any] = None,
            validate_status: bool = True,
    ) -> HttpResponse:
        url = reverse(view_name, kwargs=reverse_kwargs)
        if query_params:
            url = f'{url}?{"&".join([f"{field}={field_value}" for field, field_value in query_params.items()])}'
        http_request = getattr(self, request_type.value, None)
        if not http_request:
            raise TypeError('Request type is not known')
        if headers:
            response = http_request(url, data=data, format=format, **headers)
        else:
            response = http_request(url, data=data, format=format)

        additional_info = f'\nAdditional info: {additional_error_msg}' if additional_error_msg else ''
        err_msg = f'Expected response code "{expected_status}", actual: "{response.status_code}"' \
                  f'Response content: {getattr(response, "content", "No content")}{additional_info}'
        if validate_status:
            assert response.status_code == expected_status, err_msg
        return decode_response(response)
