from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import links_left
import os
#import secret
from django.conf import settings


def eco_landing_redirect(request):
    return redirect('/ubertool')

def qed_splash_test(request):

    #html = render_to_string('01uberheader_main_drupal.html', {
    #    'SITE_SKIN': os.environ['SITE_SKIN'],
    #    'TITLE': 'Error'})
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02qed_splash_landing.html', {'title': 'qed'})
    html += render_to_string('03epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def qed_landing_page(request):
    #if settings.MACHINE_ID == secret.MACHINE_ID_PUBLIC:
    #    html = render_to_string('00landing_page_qed_slides_public.html', {'title': 'Ubertool'})
    #else:
    #    html = render_to_string('00landing_page_qed_slides.html', {'title': 'Ubertool'})

    html = render_to_string('00landing_page_qed_slides.html', {'title': 'qed'})

    response = HttpResponse()
    response.write(html)

    return response

def qed_splash_page(request):
    #if settings.MACHINE_ID == secret.MACHINE_ID_PUBLIC:
    #    html = render_to_string('00landing_page_qed_slides_public.html', {'title': 'Ubertool'})
    #else:
    #    html = render_to_string('00landing_page_qed_slides.html', {'title': 'Ubertool'})

    html = render_to_string('00landing_page_qed_slides.html', {'title': 'qed'})

    response = HttpResponse()
    response.write(html)

    return response