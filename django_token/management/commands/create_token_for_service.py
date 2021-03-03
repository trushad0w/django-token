from secrets import token_hex

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from django_token.models import Token


class Command(BaseCommand):
    help = "Creating token for api access for service"

    def add_arguments(self, parser):
        parser.add_argument("service", type=str, help="Service name")

    @transaction.atomic()
    def handle(self, *args, **kwargs):
        service = kwargs["service"]

        user = User.objects.create_user(username=service, email="", password=token_hex(32))

        token = Token.objects.create(user=user)
        self.stdout.write(f"Token: '{token.key}' has been generated for service {service}")
