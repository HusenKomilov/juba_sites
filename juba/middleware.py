# myproject/middleware.py

from django.utils import translation


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URL parametridan tilni olish
        lang = request.GET.get('lang', None)

        # Agar til mavjud bo'lsa, uni faollashtirish
        if lang:
            translation.activate(lang)
            request.LANGUAGE_CODE = lang

        response = self.get_response(request)
        return response
