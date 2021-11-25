from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return f'users/{instance.user.username}/{filename}'


class UserInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False)
    about = models.TextField(null=True, blank=True)
    user_pic = models.ImageField(upload_to=user_directory_path,
                                 default='default_user_pic.jpg',
                                 blank=True,
                                 null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.user.username
        return super().save(*args, **kwargs)



