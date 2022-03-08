# -*- coding: utf-8 -*-
{
    'name': "Cesag Module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/cesag_views.xml',
        'report/duplica.xml',
        'report/bulletin.xml',
        'report/passage_annee_sup.xml',
        'report/atte_diplome.xml',
        'report/admission.xml',
        'report/scolarite.xml',
        'report/atte_suivi_cours.xml',
        'report/atte_depot_memoire.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}