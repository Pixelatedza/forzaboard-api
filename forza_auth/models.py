import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser


def get_default_username():
    return "ForzaboardUser" + str(User.objects.count())


class User(AbstractUser):
    # Overriding the default username so that it is no longer unique
    # but still works exactly like the existing one.
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        default=get_default_username,
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username
