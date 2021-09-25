from .models import List


def available_lists(request):
    try:
        objs = List.objects.filter(user=request.user)
        return {'available_lists': objs}
    except TypeError:
        return {'available_lists': ()}
