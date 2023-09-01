from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings


import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])

@register.filter
def add_lang_code(url, lang_code):
    url_map = url.split("/")
    if url_map[1] in dict(settings.LANGUAGES).keys():
        return f"{url.replace(f'/{url_map[1]}',f'/{lang_code}')}"
    else:
        return f"/{lang_code}{url}"