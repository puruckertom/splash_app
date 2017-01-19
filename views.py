from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
#import links_left
import os
#import secret
from django.conf import settings


def qed_splash_page(request):
    """ Returns the html of the landing page for qed. """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    if settings.IS_PUBLIC:
        html += render_to_string('04qed_splash_landing_public.html', {'title': 'qed'})
    else:
        tml += render_to_string('04qed_splash_landing_intranet.html', {'title': 'qed'})
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response


def file_not_found(request):
    """ Returns generic page whenever there is a problem. """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_404.html', {'title': 'qed'})
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response
