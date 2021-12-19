from django.core.exceptions import FieldError
from rest_framework import filters
from rest_framework.exceptions import ValidationError


IGNORED_FIELDS = {
    'ordering',
    'limit',
    'offset',
}


class GenericRESTFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        query_kwargs = {}
        for field, value in request.query_params.items():
            if field in IGNORED_FIELDS:
                continue
            query_kwargs[field] = value
        try:
            return queryset.filter(**query_kwargs)
        except ValueError:
            raise ValidationError("Invalid value for query")
        except FieldError:
            raise ValidationError("Invalid field for query")
