from .models import List


def available_lists(request):
    return {'available_lists': List.objects.all()}
