from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from plaid import Client
from plaid import errors as plaid_errors
from django.conf import settings

def index(request):

    return render(request, 'plaid_tester/index.html')

def data_dump(request):
    accounts=None
    transactions = None
    if request.method == 'POST':

        #print(request.POST)
        client = Client(client_id=settings.PLAID_CLIENT_ID, secret=settings.PLAID_SECRET)

        response = client.exchange_token(request.POST['public_token'])
        # client.access_token should now be populated with a
        # valid access_token;  we can make authenticated requests

        print(response.json())

        accounts = client.auth_get().json()['accounts']

        # client.connect_get retrieves account data as  well!!
        transactions = client.connect_get().json()['transactions']

    return render(request, 'plaid_tester/data_dump.html',{'accounts': accounts, 'transactions':transactions})
