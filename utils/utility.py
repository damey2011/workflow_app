import subprocess

from django.conf import settings
from django.core.files import File
from django.utils import timezone


def generate_db_dump():
    db = settings.DATABASES['default']
    file_name = 'backup_{}.sql'.format(timezone.now().strftime('%d%m%Y_%H%M%S'))
    compress_command = ['gzip', file_name]
    popen = subprocess.Popen(
        ['pg_dump', '--dbname=postgresql://{}:{}@{}:{}/{}'.format(db.get('USER'), db.get('PASSWORD'), db.get('HOST'),
                                                                  db.get('PORT'), db.get('NAME')),
         '-f', file_name], stdout=subprocess.PIPE, universal_newlines=True
    )
    popen.wait()
    popen2 = subprocess.Popen(compress_command)
    popen2.wait()
    compressed_file_name = '{}.gz'.format(file_name)
    gzipped = open(compressed_file_name, mode='rb')
    file = File(file=gzipped)
    file.content_type = 'text/*'
    subprocess.Popen(['rm', compressed_file_name])
    return file
