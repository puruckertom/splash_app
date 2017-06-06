from django.template.loader import render_to_string
from collections import OrderedDict


# 03ubertext_links_left:
def ordered_list(model=None, page=None):
    link_dict = OrderedDict([
        ('Q.E.D.', OrderedDict([
            ('home', ''),
        ])
         ),
        ('Public', OrderedDict([
                #('', ''),
            ])
        ),
        ('Beta', OrderedDict([
            ('cts', 'cts'),
            ('cyan', 'cyan'),
            ('hem', 'hwbi'),
            ('hms', 'hms'),
            ('hwbi', 'hwbi'),
            ('pisces', 'pisces'),
            ('uber', 'uber'),
            ])
        ),
        ('Alpha', OrderedDict([
            ('sam', 'sam'),
            ('pop', 'pop'),
            ('wqc', 'wqc')
        ])
         ),
        ('Documentation', OrderedDict([
                ('Source Code', 'docs'),
                ('API Documentation', 'api'),
                ('Links', 'links')
            ])
        )
        # ('&uuml;bertool', OrderedDict([
        #         ('Chemical Selection', 'select_chemical'),
        #         ('Use/Label/Site Data', 'site_data'),
        #         ('Pesticide Properties', 'pesticide_properties'),
        #         ('Exposure Concentrations', 'exposure_concentrations'),
        #         ('Aquatic Toxicity', 'aquatic_toxicity'),
        #         ('Terrestrial Toxicity', 'terrestrial_toxicity'),
        #         ('Ecosystem Inputs', 'ecosystem_inputs'),
        #         ('Run &uuml;bertool', 'run_ubertool'),
        #         ('Saved Runs', 'user'),
        #     ])
        # ),
    ])

    return render_to_string('05qed_splash_links_left_drupal.html', {
        'LINK_DICT': link_dict,
        'MODEL': model,
        'PAGE': page
    })