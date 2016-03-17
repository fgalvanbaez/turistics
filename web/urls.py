__author__ = 'fgalvan'

from django.conf.urls import url
from web.views import *

urlpatterns = [

    url(r'^$', IndexView.as_view(template_name='web/index.html'), name='web_index'),

    url(r'^blank/$', BlankView.as_view(template_name='web/blank.html'), name='web_blank'),

    url(r'^buttons/$', ButtonsView.as_view(template_name='web/buttons.html'), name='web_buttons'),

    url(r'^flot/$', FlotView.as_view(template_name='web/flot.html'), name='web_flot'),

    url(r'^forms/$', FormsView.as_view(template_name='web/forms.html'), name='web_forms'),

    url(r'^grid/$', GridView.as_view(template_name='web/grid.html'), name='web_grid'),

    url(r'^icons/$', IconsView.as_view(template_name='web/icons.html'), name='web_icons'),

    url(r'^login/$', LoginView.as_view(template_name='web/login.html'), name='web_login'),

    url(r'^morris/$', MorrisView.as_view(template_name='web/morris.html'), name='web_morris'),

    url(r'^notifications/$', NotificationsView.as_view(template_name='web/notifications.html'), name='web_notifications'),

    url(r'^panels-wells/$', PanelsWellsView.as_view(template_name='web/panels-wells.html'), name='web_panelswells'),

    url(r'^tables/$', TablesView.as_view(template_name='web/tables.html'), name='web_tables'),

    url(r'^typography/$', TypographyView.as_view(template_name='web/typography.html'), name='web_typography  '),

]
