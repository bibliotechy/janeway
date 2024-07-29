from django.conf import settings
from django.core.management.base import BaseCommand

from utils.models import RORImport
from core.models import Organization
from utils.logger import get_logger


logger = get_logger(__name__)


class Command(BaseCommand):
    """
    Fetches ROR data and generates Organization records.
    """

    help = "Fetches ROR data and generates Organization records."

    def handle(self, *args, **options):
        ror_import = RORImport.objects.create()
        ror_import.get_records()
        if ror_import.ongoing or settings.DEBUG:
            if not ror_import.previous_import:
                ror_import.download_data()
            elif ror_import.previous_import.zip_path != ror_import.zip_path:
                ror_import.download_data()
        if ror_import.ongoing or settings.DEBUG:
            Organization.import_ror_batch(ror_import)
        if ror_import.ongoing:
            ror_import.status = ror_import.RORImportStatus.SUCCESSFUL
            ror_import.save()
        logger.info(ror_import.status)
