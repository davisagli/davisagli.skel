import copy

from zopeskel.plone import BasicZope
from zopeskel.base import get_var


class DavisagliSkel(BasicZope):
    _template_dir = 'templates/davisagli'
    summary = "A project set up per David Glick's preferences"
    help = """
"""
    category = "Plone Development"
    required_templates = []
    use_local_commands = False
    use_cheetah = True
    vars = copy.deepcopy(BasicZope.vars)
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'package').default = 'example'
    get_var(vars, 'description').default = 'Example Add-on'
    get_var(vars, 'license_name').default = 'GPL'
