from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Concert)
admin.site.register(Composition)
admin.site.register(Conductor)
admin.site.register(ConcertSeason)
admin.site.register(ConcertDate)
admin.site.register(Movement)
admin.site.register(Soloist)
admin.site.register(Bookings)
