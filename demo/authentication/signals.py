from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.groups.add(Group.objects.get(name='customer'))
        print('Profile created')

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
        print('Profile updated')

@receiver(pre_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    try:
        instance.picture.delete(save=False)
    except:
        print('No picture to delete')
