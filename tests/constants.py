from django.conf import settings

local_url = 'http://127.0.0.1:8000'
docker_url = 'http://django:8003'
base_url = docker_url if settings.USE_DOCKER else local_url
success_message = 'Запись найдена'
error_message = 'Запись не найдена'
required_field_message = 'Заполните это поле.'

valid_bank_bin = {
    'bin': '45719797',
    'brand': 'VISA',
    'type': 'DEBIT',
    'category': 'DANKORT',
    'issuer': 'BROAGER SPAREKASSE',
    'alpha_2': 'DK',
    'alpha_3': 'DNK',
    'country': 'Denmark',
    'latitude': '56.2639',
    'longitude': '9.50179',
    'bank_phone': '74 18 38 38',
    'bank_url': 'www.portalbank.dk/broager/',
}

invalid_ban_bin = {'bin': 123}

input_field = '<input id="get_data" type="text" name="get_data" data-cy="input_bin" value="">'
button = '<button type="submit" data-cy="submit_button" class="btn btn-primary">SEND</button>'

bad_bins = [
    'bad_value',
    '-123',
    '',
    '@!#$$',
    '123',
]
