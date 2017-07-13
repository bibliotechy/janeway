from django.core.management import call_command
from django.core.management.base import BaseCommand

from journal import models as journal_models
from core import models as core_models
from utils import models as utils_models


class Command(BaseCommand):
    """ A management command to nuke the current import cache."""

    help = "Nukes the current import cache in its entirety."

    def handle(self, *args, **options):
        """ Deletes all import cache entries in the DB and on disk

        :param args: None
        :param options: None.
        :return: None
        """
        print("Nuking import cache.")

        utils_models.ImportCacheEntry.nuke()
