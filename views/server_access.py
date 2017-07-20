from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from . import links_left
import os

# proxies to various back end machines
def qed_api_ubertool(request):
    flask_server = os.environ.get('UBERTOOL_REST_SERVER')
    api_url = flask_server + '/api/ubertool'
    print(flask_server)
    #TODO: change to proxy
    return redirect(api_url)

def ubertool_rest_model(request, model='none'):
    flask_server = os.environ.get('UBERTOOL_REST_SERVER')
    api_url = flask_server + '/rest/' + model
    print(flask_server)
    # TODO: use requests and get to wrap in a normal qed page
    return redirect(api_url)
