from .models import List, Friends, FriendRequest


def available_lists(request):
    try:
        objs = List.objects.filter(user=request.user)
        return {'available_lists': objs}
    except TypeError:
        return {'available_lists': ()}


def current_friends(request):
    try:
        friend_list = Friends.objects.get(user=request.user)
        friends = friend_list.friends.all()
        if str(friends) == '<QuerySet [None]>':
            return {'friends': {}}
        else:
            return {'friends': friends}
    except TypeError:
        return {'friends': ()}
    except:
        return {'friends': ()}


def outgoing_friend_requests(request):
    try:
        outgoing_requests = FriendRequest.objects.filter(sender=request.user, is_active=True)
        return {'outgoing_friend_requests': outgoing_requests}
    except TypeError:
        return {'outgoing_friend_requests': ()}


def incoming_friend_requests(request):
    try:
        incoming_requests = FriendRequest.objects.filter(receiver=request.user, is_active=True)
        return {'incoming_friend_requests': incoming_requests}
    except TypeError:
        return {'incoming_friend_requests': ()}
