from django.contrib import admin
from topics.models import newsletter_subscriber,website_recommendation
# Register your models here.
admin.site.register(newsletter_subscriber)
admin.site.register(website_recommendation)