import json
from datetime import datetime
from http import HTTPStatus

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def json_echo_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


def add(request):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if data.get("A") == '':
            response = JsonResponse(data, status=HTTPStatus.BAD_REQUEST)
            response.status_code = 400
            return response
        try:
            result = int(data['A']) + int(data['B'])
            return JsonResponse({'result': result})
        except ValueError:
            response = JsonResponse(data, status=HTTPStatus.BAD_REQUEST)
            response.status_code = 400
            return response


def subtract(request):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if not data.get("A") or not data.get("B"):
            response = JsonResponse(data, status=HTTPStatus.BAD_REQUEST)
            response.status_code = 400
            return response
        try:
            result = int(data['A']) - int(data['B'])
            return JsonResponse({'result': result})
        except ValueError:
            response = JsonResponse(data, status=HTTPStatus.BAD_REQUEST)
            response.status_code = 400
            return response


def multiply(request):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if not data.get("A") or not data.get('B'):
            response = JsonResponse(data, status=HTTPStatus.BAD_REQUEST)
            response.status_code = 400
            return response
        try:
            result = int(data['A']) * int(data['B'])
            return JsonResponse({'result': result})
        except ValueError:
            response = JsonResponse(data, status=HTTPStatus.BAD_REQUEST)
            response.status_code = 400
            return response


def divide(request):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if not data.get("A") or not data.get('B'):
            response = JsonResponse({'error': 'Введите два числа'})
            response.status_code = 400
            return response
        try:
            result = int(data['A']) / int(data['B'])
            return JsonResponse({'result': result})
        except ZeroDivisionError:
            response = JsonResponse(data, status=HTTPStatus.BAD_REQUEST)
            response.status_code = 400
            return response

