from django import template


register = template.Library()


@register.filter
def get_item(mapping, key):
    return mapping.get(key)


@register.simple_tag
def pk_path_value(config, row):
    return "/".join(str(row[field]) for field in config.pk_fields)
