from django.http import HttpResponse
from django.views.decorators.http import require_GET

from django.shortcuts import render


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /404/",
        "Sitemap: /sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def notfound_page(request):
    response = render(request, '404.html',)
    return response