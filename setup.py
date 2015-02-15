from distutils.core import setup

setup(
    name='itmemory',
    version='1.0',
    packages=['lib', 'cron', 'cron.management', 'cron.management.commands', 'cron.migrations', 'home',
              'home.migrations', 'home.templatetags', 'hpilo', 'hpilo.migrations', 'hpilo.templatetags', 'hwlogs',
              'hwlogs.management', 'hwlogs.management.commands', 'hwlogs.migrations', 'ittasks', 'ittasks.management',
              'ittasks.management.commands', 'ittasks.migrations', 'ittasks.templatetags', 'magonet',
              'magonet.migrations', 'objects', 'objects.migrations', 'objects.templatetags', 'itmemory', 'customers',
              'customers.migrations', 'sample-data'],
    url='https://github.com/wolfmc3/itmemory',
    license='',
    author='Marco Camplese',
    author_email='marco.camplese.mc@gmail.com',
    description='It Memory'
)
