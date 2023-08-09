from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, MyUser

@receiver(post_save, sender=MyUser)
def createprofile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=MyUser)
def saveprofile(sender, instance, **kwargs):
    instance.profile.save()