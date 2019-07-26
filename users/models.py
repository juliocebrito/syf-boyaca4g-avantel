from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import choices


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30)
    role = models.CharField(max_length=255, choices=choices.ROLE_CHOICES, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    state = models.BooleanField(default=True, editable=False)
    sub_state = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        permissions = (
            ('perm_admin', 'Permission Admin'),
            ('perm_customer', 'Permission Customer'),
        )

    def __str__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        user = self.user
        if user.is_active and self.role:
            role = self.role
            new_profile, new = Profile.objects.get_or_create(user=self.user)
            new_group, new = Group.objects.get_or_create(name=role)
            permission = Permission.objects.get(name='Permission ' + role)
            new_group.permissions.add(permission)
            user.groups.add(new_group)
            self.slug = slugify(self.user)
            super(Profile, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.user)
            super(Profile, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('user:detail_profile', kwargs={'slug': self.slug})

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            profile, new = Profile.objects.get_or_create(user=instance,
                                                         first_name=instance.first_name,
                                                         last_name=instance.last_name,
                                                         full_name=instance.get_full_name(),
                                                         email=instance.email,
                                                         )

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
