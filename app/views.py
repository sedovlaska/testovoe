from django.contrib import messages
from django.shortcuts import render
from app.utils import get_data_from_csv, waiter
from http import HTTPStatus


async def index(request):
    await waiter()
    data = request.GET.get('get_data')
    if data is None:
        return render(request, 'index.html', status=HTTPStatus.OK)
    flag, results = get_data_from_csv(data)
    if flag:
        messages.info(request, 'Запись найдена', fail_silently=True)
        return render(request, 'index.html', results, status=HTTPStatus.OK)
    else:
        messages.error(request, f'Запись не найдена')
        return render(request, 'index.html', results, status=HTTPStatus.BAD_REQUEST)
