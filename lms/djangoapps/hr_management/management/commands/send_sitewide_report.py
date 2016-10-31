"""
Email NYIF sitewide report to all users on list 
"""
from textwrap import dedent

from django.core.management.base import BaseCommand

from hr_management.tasks import generate_and_email_nyif_report


class Command(BaseCommand):
    """
    Generate sitewide report and email to site admins
    """
    args = ""
    help = dedent(__doc__).strip()

    def handle(self, *args, **options):
        generate_and_email_nyif_report()
