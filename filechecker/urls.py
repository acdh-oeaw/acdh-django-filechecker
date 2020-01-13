# generated by appcreator
from django.conf.urls import url
from . import views

app_name = 'filechecker'
urlpatterns = [
    url(
        r'^fccollection/$',
        views.FcCollectionListView.as_view(),
        name='fccollection_browse'
    ),
    url(
        r'^fccollection/detail/(?P<pk>[0-9]+)$',
        views.FcCollectionDetailView.as_view(),
        name='fccollection_detail'
    ),
    url(
        r'^fccollection/create/$',
        views.FcCollectionCreate.as_view(),
        name='fccollection_create'
    ),
    url(
        r'^fccollection/edit/(?P<pk>[0-9]+)$',
        views.FcCollectionUpdate.as_view(),
        name='fccollection_edit'
    ),
    url(
        r'^fccollection/delete/(?P<pk>[0-9]+)$',
        views.FcCollectionDelete.as_view(),
        name='fccollection_delete'),
    url(
        r'^fcresource/$',
        views.FcResourceListView.as_view(),
        name='fcresource_browse'
    ),
    url(
        r'^fcresource/detail/(?P<pk>[0-9]+)$',
        views.FcResourceDetailView.as_view(),
        name='fcresource_detail'
    ),
    url(
        r'^fcresource/create/$',
        views.FcResourceCreate.as_view(),
        name='fcresource_create'
    ),
    url(
        r'^fcresource/edit/(?P<pk>[0-9]+)$',
        views.FcResourceUpdate.as_view(),
        name='fcresource_edit'
    ),
    url(
        r'^fcresource/delete/(?P<pk>[0-9]+)$',
        views.FcResourceDelete.as_view(),
        name='fcresource_delete'),
]