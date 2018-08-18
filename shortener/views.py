from django.http import HttpResponse
from django.shortcuts import render
from django.views import View #function based view FBV

from .models import ShortURL

# Create your views here.
def short_redirect_view(request, shortcode=None, *args, **kwargs):
    # print(request.user)
    # print(request.user.is_authrnticated())
    # print(args)
    # print(kwargs)
    print(shortcode)
    # try:
    #     obj = ShortURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = ShortURL.objects.all().first()

    obj_url = None

    qs = ShortURL.objects.filter(shortcode__iexact=shortcode)
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url

    return HttpResponse("HELLO {sc}".format(sc=obj_url))

class ShortCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        # print(request)
        # print(args)
        # print(kwargs)
        print(shortcode)
        return HttpResponse("Hello Again {sc}".format(sc=shortcode))
