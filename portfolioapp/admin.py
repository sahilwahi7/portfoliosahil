from django.contrib import admin

# Register your models here.

from portfolioapp.models import About, Resume, Projects

admin.site.register(About)

admin.site.register(Resume)

admin.site.register(Projects)
