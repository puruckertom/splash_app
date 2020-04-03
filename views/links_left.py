from collections import OrderedDict
from django.template.loader import render_to_string


# 03ubertext_links_left:
def ordered_list_external(model=None, page=None):
    link_dict = OrderedDict([
        ('Q.E.D.', OrderedDict([
            ('public', 'qed_external_redirect/'),
            ('epa internal', 'qed_internal_redirect/'),
        ])
         ),
        ('CSS Apps', OrderedDict([
            ('cts', 'cts/'),
            ('nta', 'nta/'),
            ('pisces', 'pisces/'),
            ('pram', 'pram/'),
            ])
        ),
        ('SHC Apps', OrderedDict([
            # ('hwbi', 'hwbi/'),
        ])
        ),
        ('SSWR Apps', OrderedDict([
            # ('cyan', 'cyan/'),
            ('hms', 'hms/'),
        ])
        ),
        ('Docs', OrderedDict([
            # link qed_api
            ('api documentation', 'api/'),
            ('source code', 'source/'),
            ('wiki', 'wiki/'),
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
        #         ('Run &uuml;bertool', 'run_pram'),
        #         ('Saved Runs', 'user'),
        #     ])
        # ),
    ])
    
    return render_to_string('05qed_splash_links_left_drupal.html', {
        'LINK_DICT': link_dict,
        'MODEL': model,
        'PAGE': page
    })

# 03ubertext_links_left:
def ordered_list_internal(model=None, page=None):
    link_dict = OrderedDict([
        ('Q.E.D.', OrderedDict([
            ('public', 'qed_external_redirect'),
            ('epa internal', 'qed_internal_redirect'),
        ])
         ),
        ('CSS Apps', OrderedDict([
            ('cts', 'cts/'),
            ('nta', 'nta/'),
            ('pisces', 'pisces/'),
            ('pram', 'pram/'),
            ])
        ),
        ('SHC Apps', OrderedDict([
            ('hwbi', 'hwbi/'),
        ])
        ),
        ('SSWR Apps', OrderedDict([
            ('cyan', 'cyan/'),
            ('hms', 'hms/'),
        ])
        ),
        ('Docs', OrderedDict([
            # link qed_api
            ('api documentation', 'api/'),
            ('rest endpoints', 'rest_landing/'),
            ('source code', 'source/'),
            ('wiki', 'wiki/'),
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
        #         ('Run &uuml;bertool', 'run_pram'),
        #         ('Saved Runs', 'user'),
        #     ])
        # ),
    ])

    return render_to_string('05qed_splash_links_left_drupal.html', {
        'LINK_DICT': link_dict,
        'MODEL': model,
        'PAGE': page
    })
