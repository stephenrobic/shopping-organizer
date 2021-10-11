from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, default=0)
    checked_off = models.BooleanField(default=False)

    class Meta:
        ordering = ['checked_off', 'name']

    def __str__(self):
        return self.name


class List(models.Model):
    user = models.ForeignKey(User, related_name="shoppinglist",
                             on_delete=models.SET_NULL,
                             null=True, blank=True)
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(Item)
    created_on = models.DateTimeField('created on', auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    budget = models.IntegerField(default=0)

    def was_created_recently(self):
        return self.created_on >= timezone.now()

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.name

    def share_list(self):
        pass


class Friends(models.Model):
    #Casecade delete => if a user is deleted, their corresponding friend list will be deleted
    #This is one-one because, there only 1 friend list per 1 user
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    #A list of users; you can think of it as a list of primary keys to the account of who the user is friends with
    #blank= True, because it is possible that they have no friends
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        """
        Add a new friend
        """
        #check if they're already in friends, and if not, add them
        if account not in self.friends.all():
            self.friends.add(account)

    def remove_friend(self, account):
        """
        Remove a friend
        """
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        """
        Initiate the action of unfriending someone
        """
        remover_friends_list = self #person executing the friendship termination

        # Remove friend from remover friend list
        remover_friends_list.remove_friend(removee)

        # Remove friend from removee friend list
        friends_list = Friends.objects.get(user=removee)
        friends_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        """
        Is this a mutual friend?
        """
        return True if friend in self.friends.all() else False


class FriendRequest(models.Model):
    """
    A friend request consists of two parts:
        1. A SENDER who initiates the friend request
        2. A RECEIVER whom receives the friend request
    """
    #1 user can send out any number of friend requests
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        """
        Accept a friend request
        Update both SENDER and RECEIVER friend lists
        """
        receiver_friend_list, created = Friends.objects.get_or_create(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list, created = Friends.objects.get_or_create(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        """
        Decline a friend request
        It is "declined by setting the 'is_active' field to false
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """
        Cancel a friend request
        The request is canceled by setting the 'is_active' field to False
        This is only different with respect to "declining" through the notification that is generated
        """
        self.is_active = False
