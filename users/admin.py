from django.contrib import admin

from users.models import UserProfile # bunun ayri import edilmesi lazimmis

admin.site.register(UserProfile)


# Register your models here.
