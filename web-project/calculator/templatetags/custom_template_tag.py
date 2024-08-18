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

@register.simple_tag
def is_small_screen(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    return 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent