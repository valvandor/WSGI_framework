from jinja2 import Environment, FileSystemLoader


def render(template_name, folder='application/templates', **kwargs):
    # TODO: the folder argument should be declared in settings
    """

    :param template_name: name of rendering template
    :param folder: where to find templates
    :param kwargs:
    :return:
    """
    env = Environment(
        loader=FileSystemLoader(folder)
    )
    template = env.get_template(template_name)
    return template.render(**kwargs)


