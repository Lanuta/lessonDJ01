from django.http import HttpResponse

def data_view(request):
    return HttpResponse("<h1>Это страница Data</h1><p>Здесь будут какие-то данные.</p>")

def test_view(request):
    return HttpResponse("<h1>Это страница Test</h1><p>Просто тестовая страничка.</p>")