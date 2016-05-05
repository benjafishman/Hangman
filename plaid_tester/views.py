from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from plaid import Client
from plaid import errors as plaid_errors
from django.conf import settings
import sys


def index(request):
    return render(request, 'plaid_tester/index.html')


def data_dump(request):
    accounts = None
    transactions = None
    if request.method == 'POST':

        # print(request.POST)
        client = Client(client_id=settings.PLAID_CLIENT_ID, secret=settings.PLAID_SECRET)

        try:
            response = client.exchange_token(request.POST['public_token'])
            print(response.json())
        except:
            print(sys.exc_info()[0])


        try:
            response = client.upgrade('connect')
            print(response.json())
        except:
            print(sys.exc_info()[0])
        # client.access_token should now be populated with a
        # valid access_token;  we can make authenticated requests


        try:
            accounts = client.auth_get().json()['accounts']
        except:
            print(sys.exc_info()[0])
        # client.connect_get retrieves account data as  well!!
        try:
            transactions = client.connect_get().json()['transactions']
        except:
            print(sys.exc_info()[0])

    return render(request, 'plaid_tester/data_dump.html', {'accounts': accounts, 'transactions': transactions})
