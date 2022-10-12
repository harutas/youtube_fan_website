from django.contrib import admin

# Register your models here.
from .models import Youtube
from .models import Notable
from .models import Link

admin.site.register(Youtube)
admin.site.register(Notable)
admin.site.register(Link)