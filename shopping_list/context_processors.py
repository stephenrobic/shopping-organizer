from .models import List, Friends, FriendRequest


def user_lists(request):
    try:
        user_lists = List.objects.filter(user=request.user)
        return {'user_lists': user_lists}

    except TypeError:
        return {'user_lists': ()}


def shared_lists(request):
    try:
        shared_lists = List.objects.filter(shared_with=request.user)
        return {'shared_lists': shared_lists}
    except TypeError:
        return {'shared_lists': ()}


def current_friends(request):
    try:
        friend_list = Friends.objects.get(user=request.user)
        friends = friend_list.friends.all()
        if str(friends) == '<QuerySet [None]>':
            return {'friends': {}}
        else:
            return {'friends': friends}
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
