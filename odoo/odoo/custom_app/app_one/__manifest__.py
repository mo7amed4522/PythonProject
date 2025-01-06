{
    'name': 'My App',
    'author': 'Khaled Mohamed Abdo',
    'description': 'This is my first app for odoo developer',
    'version': '18.0',
    'installable': True,
    'application': True,
    'auto_install': False,
    'summary': 'A sample Odoo application',
    'category': 'Tools',
    'license': 'LGPL-3',  # Specify your license here
    'depends': ['base', 'sale_management', 'account','sale','mail','contacts'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequance.xml',
        'view/base_menu.xml',
        'view/property_view.xml',
        'view/owner_view.xml',
        'view/tags_view.xml',
        'view/sale_order_view.xml',
        'view/res_partner_view.xml',
        'view/building_view.xml',
        'view/property_history_view.xml',
        'view/account_move_view.xml',
        'wizard/change_wizaed_state_view.xml',
        'report/property_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css',
            'app_one/static/src/components/listView/listView.css',
            'app_one/static/src/components/listView/listView.js',
            'app_one/static/src/components/listView/listView.xml',
        ],
        'web.report_assets_common': ['app_one/static/src/css/font.css'],
    }
}
