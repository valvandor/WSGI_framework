from os.path import join
from jinja2 import Template


def render(template_name, folder='application/templates', **kwargs):
    """

    :param template_name: name of rendering template
    :param folder: where to find templates
    :param kwargs:
    :return:
    """
    template_file = join(folder, template_name)

    # open template by name
    with open(template_file, encoding='utf-8') as file:
        template = Template(file.read())

    return template.render(**kwargs)
