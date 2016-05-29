from django.core.management.base import BaseCommand, CommandError

from scraping.scraper_selenium import scrap_tripadvisor


class Command(BaseCommand):
    args = ''
    help = 'Execute scraper.py'

    def add_arguments(self, parser):
        parser.add_argument('link')

    def handle(self, *args, **options):

        try:
            scrap_tripadvisor(options['link'])
            self.stdout.write("Success!!")

        except Exception as e:
            raise CommandError('No se ejecuto el procedimiento correctamente: "%s"' %e)


