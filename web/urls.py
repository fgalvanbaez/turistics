__author__ = 'fgalvan'

from django.conf.urls import url
from web.views import IndexView

urlpatterns = [

    url(r'^$', IndexView.as_view(template_name='web/index.html'), name='web_index'),

]
