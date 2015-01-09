"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'itmemory.custom_dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    columns = 3

    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append a group for "Administration" & "Applications"
        self.children.append(modules.AppList(
                    _('Applications'),
                    column=1,
                    css_classes=('collapse closed',),
                    exclude=('django.contrib.*',),
                )
        )
        self.children.append(modules.AppList(
                    _('Amministrazione'),
                    column=2,
                    collapsible=False,
                    models=('django.contrib.*',),
        ))


        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Sito'),
            column=2,
            children=[
                {
                    'title': _('Torna al sito'),
                    'url': '/',
                    'external': False,
                },
            ]
        ))
        

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


