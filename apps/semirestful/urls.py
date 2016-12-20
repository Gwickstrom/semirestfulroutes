from django.conf.urls import url
from views import index, new, create, destroy, edit
from views import users_w_id, users

urlpatterns = [
    url(r'^$', users),
    # url(r'^$', index, name="index"),
    url(r'^new$', new),
    url(r'^create/$', create, name="create"),
    url(r'^(?P<id>\d+)/$', users_w_id, name="users_w_id"),
    # url(r'^show/(?P<id>\d+)/$', show, name="show"),
    url(r'^(?P<id>\d+)/edit/$', edit, name="edit"),
    url(r'^(?P<id>\d+)/destroy/$', destroy, name="destroy"),
]
