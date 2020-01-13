# generated by appcreator
import django_filters
from django import forms

from dal import autocomplete

from . models import (
    FcCollection,
    FcResource
)


class FcCollectionListFilter(django_filters.FilterSet):
    fc_fullname = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcCollection._meta.get_field('fc_fullname').help_text,
        label=FcCollection._meta.get_field('fc_fullname').verbose_name
    )
    fc_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcCollection._meta.get_field('fc_name').help_text,
        label=FcCollection._meta.get_field('fc_name').verbose_name
    )
    fc_ordername = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcCollection._meta.get_field('fc_ordername').help_text,
        label=FcCollection._meta.get_field('fc_ordername').verbose_name
    )
    fc_arche_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcCollection._meta.get_field('fc_arche_id').help_text,
        label=FcCollection._meta.get_field('fc_arche_id').verbose_name
    )
    fc_arche_description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcCollection._meta.get_field('fc_arche_description').help_text,
        label=FcCollection._meta.get_field('fc_arche_description').verbose_name
    )

    class Meta:
        model = FcCollection
        fields = [
            'id',
            'id',
            'fc_fullname',
            'fc_name',
            'fc_ordername',
            'fc_firstmod',
            'fc_lastmod',
            'fc_size',
            'fc_items',
            'parent',
            'fc_arche_id',
            'fc_arche_description',
            'lft',
            'rght',
            'tree_id',
            'level',
            ]


class FcResourceListFilter(django_filters.FilterSet):
    fc_fullname = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcResource._meta.get_field('fc_fullname').help_text,
        label=FcResource._meta.get_field('fc_fullname').verbose_name
    )
    fc_filename = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcResource._meta.get_field('fc_filename').help_text,
        label=FcResource._meta.get_field('fc_filename').verbose_name
    )
    fc_type = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcResource._meta.get_field('fc_type').help_text,
        label=FcResource._meta.get_field('fc_type').verbose_name
    )
    fc_extension = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcResource._meta.get_field('fc_extension').help_text,
        label=FcResource._meta.get_field('fc_extension').verbose_name
    )
    fc_arche_cat = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcResource._meta.get_field('fc_arche_cat').help_text,
        label=FcResource._meta.get_field('fc_arche_cat').verbose_name
    )
    fc_arche_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcResource._meta.get_field('fc_arche_id').help_text,
        label=FcResource._meta.get_field('fc_arche_id').verbose_name
    )
    fc_arche_description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=FcResource._meta.get_field('fc_arche_description').help_text,
        label=FcResource._meta.get_field('fc_arche_description').verbose_name
    )

    class Meta:
        model = FcResource
        fields = [
            'id',
            'id',
            'fc_fullname',
            'fc_filename',
            'fc_lastmod',
            'fc_size',
            'fc_directory',
            'fc_type',
            'fc_extension',
            'fc_arche_cat',
            'fc_arche_id',
            'fc_arche_description',
            ]