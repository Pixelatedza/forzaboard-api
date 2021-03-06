from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class UUIDRelatedField(serializers.RelatedField):

    default_error_messages = {
        'required': _('This field is required.'),
        'does_not_exist': _('Object with uuid={value} does not exist.'),
        'invalid': _('Invalid value.'),
    }

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get(uuid=data)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', value=data)
        except (TypeError, ValueError):
            self.fail('invalid')

    def to_representation(self, value):
        return value.uuid


class UUIDModelSerializer(serializers.ModelSerializer):
    serializer_related_field = UUIDRelatedField
