from fabric.api import local


def djp_setup(project_name, destination="/home/dmalik5/django-dev/"):
    destination = "/home/dmalik5/django-dev/%s/" % project_name
    local("mkdir %s" % destination)
    local("django-admin.py startproject --template=https://github.com/dmalikcs/django-project-template/archive/master.zip  %s %s" % (project_name, destination))
    local("git init %s" % destination)
