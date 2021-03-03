from secrets import token_hex

from django.conf import settings
from django.db import models


class Token(models.Model):
    """
    An access token that is associated with a user.  This is essentially the same as the token model from Django REST Framework
    """
    key = models.CharField(max_length=70, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="token", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return token_hex(32)

    def __unicode__(self):
        return self.key
