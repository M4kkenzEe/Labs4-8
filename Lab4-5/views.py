from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import psycopg2
# Create your views here.


def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html'],
        }})

def GetOrders(request):
    conn = psycopg2.connect(dbname='demo', user='suser',
                            password='suserpassword', host='127.0.0.1')
    cursor = conn.cursor()
    cursor.execute('select company_name, country from companies')
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Ford', 'id': 1},
            {'title': 'Toyota', 'id': 2},
            {'title': 'Volkswagen', 'id': 3}
        ],
        'com_info': [rec for rec in records]
    }})

def GetOrder(request, id):
    conn = psycopg2.connect(dbname='demo', user='suser',
                            password='suserpassword', host='127.0.0.1')
    cursor = conn.cursor()
    cursor.execute('select company_name, title, '
                   'model_type from cars, '
                   'companies where (company_id = fk_company_id )')
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'products':[prod for prod in records]
    }})


