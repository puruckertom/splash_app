# import links_left
# import secret
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from . import links_left
import os

def splash_landing_page(request):
    text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'splash_app/views/landing_text.txt'), 'r')
    xx = text_file2.read()

    #drupal template for header with bluestripe
    #html = render_to_string('01epa_drupal_header.html', {})
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"Q.E.D."
    })
    #html = render_to_string('01uberheader_main_drupal.html', {
    #    'SITE_SKIN': os.environ['SITE_SKIN'],
    #    'TITLE': u"\u00FCbertool"
    #})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title_splash.html', {})

    #main body of text
    #html += render_to_string('04uber_drupal_frog_intro.html', {})
    #http://jsfiddle.net/9zGQ8/

    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': 'Environmental Models and Services',
        'TEXT_PARAGRAPH': xx
    })
    html += render_to_string('07ubertext_end_drupal.html', {})
    html += links_left.ordered_list()  # fills out 05ubertext_links_left_drupal.html

    #scripts and footer
    html += render_to_string('09epa_drupal_ubertool_css.html', {})
    #html += render_to_string('09epa_drupal_ubertool_scripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def qed_splash_page_old(request):
    """ Returns the html of the landing page for qed. """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    if settings.IS_PUBLIC:
        html += render_to_string('04qed_splash_landing_public.html', {'title': 'qed'})
    else:
        html += render_to_string('04qed_splash_landing_intranet.html', {'title': 'qed'})
    html += render_to_string('09epa_drupal_splashscripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    response = HttpResponse()
    response.write(html)
    return response


def file_not_found(request):
    """ Returns the html of the landing page for qed. """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    if settings.IS_PUBLIC:
        html += render_to_string('04qed_splash_landing_public.html', {'title': 'qed'})
    else:
        html += render_to_string('04qed_splash_landing_intranet.html', {'title': 'qed'})
    html += render_to_string('09epa_drupal_splashscripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})
    response = HttpResponse()
    response.write(html)
    return response
