from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    contact = models.CharField(max_length=20, default='')
    speciality = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return f'{self.user.username} UserProfile'


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class ProjectPage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='creater')
    image = models.ImageField(default='default_project.jpg', upload_to='project_pics')
    type = models.CharField(max_length=20, default='project')
    title = models.CharField(max_length=30, default='New Project')
    description = models.CharField(max_length=500, default='')
    waiting_list = models.ManyToManyField(User, blank=True, related_name="users")
    participants = models.ManyToManyField(User, blank=True, related_name="participate")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    project = models.ForeignKey('ProjectPage', on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True)

    text = models.TextField()
    creation = models.DateTimeField(auto_now=True)


def save(self):
    super().save()

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)
