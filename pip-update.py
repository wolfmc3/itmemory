import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip-2.7 install --upgrade " + dist.project_name, shell=True)