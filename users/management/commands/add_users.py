from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        CustomUser.objects.all().delete()
        CustomUser.objects.create_superuser(username='nanku',
                                            email='fireloki@mail.ru',
                                            password='123')
        CustomUser.objects.create_user(username='test',
                                       email='test@test.com',
                                       password='123',
                                       )
        CustomUser.objects.create_user(username='test1',
                                       email='test1@test.com',
                                       password='123',
                                       )
