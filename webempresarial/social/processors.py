from .models import Link

def contextdict(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context