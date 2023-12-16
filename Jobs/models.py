from django.db import models
from django.contrib.auth.models import User

# from django.utils.html import escape, mark_safe

# class User(AbstractUser):
#     is_employer = models.BooleanField(default=False)
#     is_applicant = models.BooleanField(default=False)
# class CustomUser(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError("username must be set")
#         user = self.model(username = username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None):
#         user = self.create_user(username=username, password=password)
#         user.is_staff= True
#         user.is_superuser = True
#         user.save(usind=self._db)
#         return user

# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=50,unique=True)
#     email = models.EmailField(unique=True, null=True, blank=True)
#     is_employer = models.BooleanField(default=False)
#
#     objects = CustomUser()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return self.email + self.username








class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    # is_applicant = models.BooleanField(default=False)

    # def __str__(self):
        # return f'{self.user} {self.is_employer} {self.is_applicant}'

User.userprofile = property(lambda u : Userprofile.objects.get_or_create(user=u)[0])




class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.created_by.username} - {self.job.title}"

