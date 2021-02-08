from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from . import links_left
import os
import logging
from bs4 import BeautifulSoup



def get_html_text(filename):
    local_file = 'splash_app/views/' + filename
    text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], local_file), 'r')
    local_read = text_file2.read()
    if os.environ.get('IS_PUBLIC') == "True":
        return build_landing_text(local_read)
    return local_read

def splash_landing_page(request):
    #text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'splash_app/views/landing_text.txt'), 'r')
    #xx = text_file2.read()
    xx = get_html_text('landing_text.txt')
    if settings.IN_PROD:
        xx = get_html_text('landing_text_prod.txt')
    #drupal template for header with bluestripe
    #templates_qed/drupal_2017
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"Q.E.D."
    })
    #html = render_to_string('01uberheader_main_drupal.html', {
    #    'SITE_SKIN': os.environ['SITE_SKIN'],
    #    'TITLE': u"\u00FCbertool"
    #})
    # templates_qed/drupal_2017
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    # templates_qed/splash
    html += render_to_string('03epa_drupal_section_title_splash.html', {})

    #main body of text
    #html += render_to_string('04uber_drupal_frog_intro.html', {})
    #http://jsfiddle.net/9zGQ8/

    # templates_qed/uber2017
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': 'Environmental Models and Services',
        'TEXT_PARAGRAPH': xx
    })

    # templates_qed/uber2017
    html += render_to_string('07ubertext_end_drupal.html', {})

    # fills out 05ubertext_links_left_drupal.html
    if settings.IN_PROD:
        html += links_left.ordered_list_prod()
    elif os.environ.get('IS_PUBLIC') == "True":
        html += links_left.ordered_list_external()
    else:
        html += links_left.ordered_list_internal()

    #scripts and footer
    # templates_qed/uber2017
    html += render_to_string('09epa_drupal_css.html', {})

    # templates_qed/drupal_2017
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def whoami_table():
    try:
        html = "<br>"
        html += "ENV_NAME = " + os.environ.get("ENV_NAME") + "<br>"
        html += "CTS_EFS_SERVER = " + os.environ.get("CTS_EFS_SERVER") + "<br>"
        html += "CTS_EPI_SERVER = " + os.environ.get("CTS_EPI_SERVER") + "<br>"
        html += "CTS_JCHEM_SERVER = " + os.environ.get("CTS_JCHEM_SERVER") + "<br>"
        html += "CTS_OPERA_SERVER = " + os.environ.get("CTS_OPERA_SERVER") + "<br>"
        html += "CTS_REST_SERVER = " + os.environ.get("CTS_REST_SERVER") + "<br>"
        html += "CTS_SPARC_SERVER = " + os.environ.get("CTS_SPARC_SERVER") + "<br>"
        html += "CTS_TEST_SERVER = " + os.environ.get("CTS_TEST_SERVER") + "<br>"
        html += "CYAN_REST_SERVER = " + os.environ.get("CYAN_REST_SERVER") + "<br>"
        html += "DASK_SCHEDULER = " + os.environ.get("DASK_SCHEDULER") + "<br>"
        html += "DJANGO_SETTINGS_FILE = " + os.environ.get("DJANGO_SETTINGS_FILE") + "<br>"
        html += "EPA_ACCESS_TEST_URL = " + os.environ.get("EPA_ACCESS_TEST_URL") + "<br>"
        html += "HMS_BACKEND_SERVER = " + os.environ.get("HMS_BACKEND_SERVER") + "<br>"
        html += "HMS_BACKEND_SERVER_DOCKER = " + os.environ.get("HMS_BACKEND_SERVER_DOCKER") + "<br>"
        html += "HMS_BACKEND_SERVER_INTERNAL = " + os.environ.get("HMS_BACKEND_SERVER_INTERNAL") + "<br>"
        html += "HMS_BACKEND_SERVER_URL = " + os.environ.get("HMS_BACKEND_SERVER_URL") + "<br>"
        html += "HMS_LOCAL = " + os.environ.get("HMS_LOCAL") + "<br>"
        html += "IN_DOCKER = " + os.environ.get("IN_DOCKER") + "<br>"
        html += "IS_PUBLIC = " + os.environ.get("IS_PUBLIC") + "<br>"
        html += "NODEJS_HOST = " + os.environ.get("NODEJS_HOST") + "<br>"
        html += "NODEJS_PORT = " + os.environ.get("NODEJS_PORT") + "<br>"
        html += "OPENCPU_REST_SERVER = " + os.environ.get("OPENCPU_REST_SERVER") + "<br>"
        html += "REDIS_HOSTNAME = " + os.environ.get("REDIS_HOSTNAME") + "<br>"
        html += "REDIS_PORT = " + os.environ.get("REDIS_PORT") + "<br>"
        html += "VARROAPOP_SERVER = " + os.environ.get("VARROAPOP_SERVER") + "<br>"
        html += "<br>"
    except:
        html = "<br> Missing environmental variable! <br>"
    return html

def whoami_landing_page(request):
    #text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'splash_app/views/landing_text.txt'), 'r')
    #xx = text_file2.read()
    xx = get_html_text('landing_text_whoami.txt')
    #drupal template for header with bluestripe
    #templates_qed/drupal_2017
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"Q.E.D."
    })
    #html = render_to_string('01uberheader_main_drupal.html', {
    #    'SITE_SKIN': os.environ['SITE_SKIN'],
    #    'TITLE': u"\u00FCbertool"
    #})
    # templates_qed/drupal_2017
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    # templates_qed/splash
    html += render_to_string('03epa_drupal_section_title_splash.html', {})

    #main body of text
    #html += render_to_string('04uber_drupal_frog_intro.html', {})
    #http://jsfiddle.net/9zGQ8/

    yy = whoami_table()
    zz = xx + yy

    # templates_qed/uber2017
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': 'Environmental Variables',
        'TEXT_PARAGRAPH': zz
    })

    # templates_qed/uber2017
    html += render_to_string('07ubertext_end_drupal.html', {})

    # fills out 05ubertext_links_left_drupal.html
    if settings.IN_PROD:
        html += links_left.ordered_list_prod()
    elif os.environ.get('IS_PUBLIC') == "True":
        html += links_left.ordered_list_external()
    else:
        html += links_left.ordered_list_internal()

    #scripts and footer
    # templates_qed/uber2017
    html += render_to_string('09epa_drupal_css.html', {})

    # templates_qed/drupal_2017
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def wiki_landing_page(request):
    #text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'splash_app/views/landing_text_wiki.txt'), 'r')
    #xx = text_file2.read()
    xx = get_html_text('landing_text_wiki.txt')
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
        'TITLE': 'Wiki',
        'TEXT_PARAGRAPH': xx
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    # fills out 05ubertext_links_left_drupal.html
    if settings.IN_PROD:
        html += links_left.ordered_list_prod()
    elif os.environ.get('IS_PUBLIC') == "True":
        html += links_left.ordered_list_external()
    else:
        html += links_left.ordered_list_internal()

    #scripts and footer
    html += render_to_string('09epa_drupal_css.html', {})
    #html += render_to_string('09epa_drupal_pram_scripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def source_landing_page(request):
    #text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'splash_app/views/landing_text_source.txt'), 'r')
    #xx = text_file2.read()
    xx = get_html_text('landing_text_source.txt')
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
        'TITLE': 'Source Code',
        'TEXT_PARAGRAPH': xx
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    # fills out 05ubertext_links_left_drupal.html
    if settings.IN_PROD:
        html += links_left.ordered_list_prod()
    elif os.environ.get('IS_PUBLIC') == "True":
        html += links_left.ordered_list_external()
    else:
        html += links_left.ordered_list_internal()

    #scripts and footer
    html += render_to_string('09epa_drupal_css.html', {})
    #html += render_to_string('09epa_drupal_pram_scripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def api_landing_page(request):
    #text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'splash_app/views/landing_text_api.txt'), 'r')
    #xx = text_file2.read()
    xx = get_html_text('landing_text_api.txt')
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
        'TITLE': 'Environmental APIs',
        'TEXT_PARAGRAPH': xx
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    # fills out 05ubertext_links_left_drupal.html
    if settings.IN_PROD:
        html += links_left.ordered_list_prod()
    elif os.environ.get('IS_PUBLIC') == "True":
        html += links_left.ordered_list_external()
    else:
        html += links_left.ordered_list_internal()

    #scripts and footer
    html += render_to_string('09epa_drupal_css.html', {})
    #html += render_to_string('09epa_drupal_pram_scripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response

def rest_landing_page(request):
    #text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'splash_app/views/landing_text_rest.txt'), 'r')
    #xx = text_file2.read()
    xx = get_html_text('landing_text_rest.txt')
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
        'TITLE': 'RESTful Endpoints',
        'TEXT_PARAGRAPH': xx
    })
    html += render_to_string('07ubertext_end_drupal.html', {})

    # fills out 05ubertext_links_left_drupal.html
    if settings.IN_PROD:
        html += links_left.ordered_list_prod()
    elif os.environ.get('IS_PUBLIC') == "True":
        html += links_left.ordered_list_external()
    else:
        html += links_left.ordered_list_internal()

    #scripts and footer
    html += render_to_string('09epa_drupal_css.html', {})
    #html += render_to_string('09epa_drupal_pram_scripts.html', {})
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)

    return response


def qed_external_redirect(request):
    return redirect("https://qed.epa.gov/")

def qed_internal_redirect(request):
    return redirect("https://qedinternal.epa.gov")

def source_code_redirect(request):
    return redirect("https://github.com/quanted/qed")


def wiki_external_redirect(request):
    return redirect("https://github.com/quanted/qed/wiki")


def file_not_found(request, exception=None):
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
    response = HttpResponse(status=404)
    response.write(html)
    return response


def page_404(request, exception=None):
    
    page_body = render_to_string("qed_splash_landing_404.html")
    
    html = render_to_string('01epa_drupal_header.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"Q.E.D."
    })

    # templates_qed/drupal_2017
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    # templates_qed/splash
    html += render_to_string('03epa_drupal_section_title_splash.html', {})

    # templates_qed/uber2017
    html += render_to_string('06ubertext_start_index_drupal.html', {
        'TITLE': 'Environmental Models and Services',
        'TEXT_PARAGRAPH': page_body
    })

    # templates_qed/uber2017
    html += render_to_string('07ubertext_end_drupal.html', {})

    # fills out 05ubertext_links_left_drupal.html
    if settings.IS_PUBLIC:
        html += links_left.ordered_list_external()
    else:
        html += links_left.ordered_list_internal()

    #scripts and footer
    # templates_qed/uber2017
    html += render_to_string('09epa_drupal_css.html', {})

    # templates_qed/drupal_2017
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse(status=404)
    response.write(html)
    return response

def build_landing_text(full_landing_text):
    """
    Builds landing text with beautiful soup.
    """
    if not hasattr(settings, 'PUBLIC_APPS'):
        return full_landing_text  # returns original landing text if not 'PUBLIC_APPS' list
    try:
        soup = BeautifulSoup(full_landing_text, 'html.parser')
        landing_html_string = ""
        for app in settings.PUBLIC_APPS:
            app_link = soup.find('a', '/'+app)
            app_header = soup.find('a', href='/'+app).parent  # gets app header
            landing_html_string += str(app_header)
            landing_html_string += str(app_header.findNext('p'))  # app description
        return landing_html_string
    except Exception as e:
        logging.warning("Error building landing text: {}".format(e))
        return full_landing_text
