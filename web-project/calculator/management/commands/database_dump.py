# your_app/management/commands/database_dump.py
from django.core.management.base import BaseCommand
from subprocess import run

class Command(BaseCommand):
    help = 'Execute python -m conf.commands.databaseDump'

    def handle(self, *args, **options):
        # Use the subprocess module to execute the specified command
        command = 'python -m conf.commands.databaseDump'
        result = run(command, shell=True)

        if result.returncode == 0:
            self.stdout.write(self.style.SUCCESS('Command executed successfully'))
        else:
            self.stdout.write(self.style.ERROR('Command failed'))

