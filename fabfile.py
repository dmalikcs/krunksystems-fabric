from fabric.api import local


def djp_setup(project_name, destination=None):
    '''
    Django project setup with default templates from Django
    '''
    destination = "/home/dmalik5/django-dev/%s/" % project_name
    template = 'https://github.com/dmalikcs/django-project-template/archive/master.zip'
    local("mkdir %s" % destination)
    local("django-admin.py startproject --template=%s  %s %s" % (template, project_name, destination))
    local("git init %s" % destination)
