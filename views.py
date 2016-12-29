from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
#import links_left
import os
#import secret
from django.conf import settings


def eco_landing_redirect(request):
    return redirect('/ubertool')

def qed_splash_page(request):

    #html = render_to_string('01uberheader_main_drupal.html', {
    #    'SITE_SKIN': os.environ['SITE_SKIN'],
    #    'TITLE': 'Error'})
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02qed_splash_landing.html', {'title': 'qed'})
    html += render_to_string('03epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def file_not_found(request):
    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': 'Error'})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL']})
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': 'Error Processing Request',
        'TEXT_PARAGRAPH': ""})
    html += """<br><img src="/static/images/404error.png" width="300" height="300">"""
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list()
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse()
    response.write(html)

    return response