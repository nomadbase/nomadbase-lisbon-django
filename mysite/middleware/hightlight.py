import re

from django.conf import settings
from django.utils.safestring import mark_safe

CLASS = getattr(settings, 'CURRENT_PAGE_CLASS', 'current_page')
CLASS_RE = re.compile(r"""(\bclass\s*=\s*(['"]))""", re.IGNORECASE)
HREF_RE = re.compile(r"""(<a\W[^>]*\bhref\s*=\s*
                         (["'])(.*?)(?<!\\)(["'])[^>]*>)""",
                         re.IGNORECASE + re.VERBOSE)
HTML_TYPES = ('text/html', 'application/xhtml+xml')


class CurrentPageMiddleware(object):
    """
    Middleware that post-processes a response to add a
    class 'current_page' to a link if its href attribute
    matches the current URL.
    """

    def process_response(self, request, response):
        path = request.get_full_path()
        if path.endswith('/'):
            paths = [path, path[:-1]]
        else:
            paths = [path, path + '/']

        if response['Content-Type'].split(';')[0] in HTML_TYPES:

            def add_current_page_class(match):
                """Returns the matched <a href="..."> tag with
                class="current_page """
                tag = match.group()
                if match.group(3) in paths:
                    has_class = CLASS_RE.search(tag)
                    if has_class:
                        tokens = CLASS_RE.split(tag)
                        new_tag = ''.join(tokens[:2]) + '%s ' % CLASS + \
                                ''.join([t for t in tokens[2:] \
                                if t not in ('"', "'")])
                    else:
                        new_tag = tag[:-1] + ' class="%s">' % CLASS
                    return mark_safe(new_tag)
                return tag
            response.content = HREF_RE.sub(add_current_page_class,
                                           response.content.decode('utf-8'))
        return response
