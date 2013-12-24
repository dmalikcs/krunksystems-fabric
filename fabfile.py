from fabric.api import local


def setup(project_name):
    print project_name

def hello():
    local("ls")
