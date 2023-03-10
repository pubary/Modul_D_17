from django.core.management.base import BaseCommand
from app1.models import CensorVoc


class Command(BaseCommand):
    help = 'Ввод слов в словарь цензуры'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.write('Введите слово, которое нужно добавить')
        word = input()
        while CensorVoc.objects.filter(word=word).exists():
            self.stdout.write(f'Такое слово уже есть. Введите другое')
            word = input()
        CensorVoc.objects.create(word=word)
        self.stdout.write(self.style.SUCCESS(f'Слово "{word}" добавлено в словарь цензуры'))
        return


