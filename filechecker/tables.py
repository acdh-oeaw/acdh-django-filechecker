# generated by appcreator
import django_tables2 as tables
from django_tables2.utils import A

from browsing.browsing_utils import MergeColumn
from . models import (
    FcCollection,
    FcResource
)


class FcCollectionTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = FcCollection
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FcResourceTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = FcResource
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}
