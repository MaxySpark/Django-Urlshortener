from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortURL

class Command(BaseCommand):
    help = "Refresh All Shortcodes"

    def handle(self,*args,**kwargs):
        return ShortURL.objects.refresh_shortcodes()    