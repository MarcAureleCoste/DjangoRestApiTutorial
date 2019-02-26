from django_filters import FilterSet
from django_filters.rest_framework import filters

from .models import Todo


class TodoFilter(FilterSet):
    ids = filters.BaseInFilter(field_name='id', lookup_expr='in')
    finished = filters.BooleanFilter()

    class Meta():
        model = Todo

        fields = {
            'ids': [],
            'title': ['icontains'],
            'description': ['icontains'],
            'finished': []
        }
