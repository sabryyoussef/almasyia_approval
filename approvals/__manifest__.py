# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Almasyia_scc2',
    'version': '1.0',
    'category': 'Human Resources/Approvals',
    'sequence': 190,
    'summary': 'Create and validate approvals requests',
    'description': """
This module manages approvals workflow
======================================

This module manages approval requests like business trips,
out of office, overtime, borrow items, general approvals,
procurements, contract approval, etc.

According to the approval type configuration, a request
creates next activities for the related approvers.
    """,
    'depends': ['mail', 'hr', 'product','sale'],
    'data': [
        'security/approval_security.xml',
        'security/ir.model.access.csv',

        'data/approval_category_data.xml',
        'data/mail_activity_type_data.xml',

        'views/approval_category_views.xml',
        'views/approval_category_approver_views.xml',
        'views/approval_product_line_views.xml',
        'views/approval_request_views.xml',
        'views/inherit_sales_order_view.xml',
        'views/res_users_views.xml',
    ],
    'demo':[
        'data/approval_demo.xml',
    ],
    'application': True,
    'installable': True,
    'assets': {
        'mail.assets_messaging': [
            'approvals/static/src/models/*.js',
        ],
        'mail.assets_discuss_public': [
            'approvals/static/src/components/*/*',
        ],
        'web.assets_backend': [
            'approvals/static/src/backend_components/*/*',
            'approvals/static/src/components/*/*',
        ],
        'web.assets_tests': [
            'approvals/static/tests/tours/**/*',
        ],
        'web.tests_assets': [
            'approvals/static/tests/helpers/**/*',
        ],
        'web.qunit_suite_tests': [
            'approvals/static/tests/qunit_suite_tests/**/*.js',
        ],
    },
    'license': 'OEEL-1',
}
