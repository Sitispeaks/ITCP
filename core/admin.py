from django.contrib import admin
from .models import  Contact,Note,Holiday

# Register your models here.
admin.site.register(Contact)
# admin.site.register(Notes)

class NoteAdmin(admin.ModelAdmin):
    list_display=('batch','desc','notes')

admin.site.register(Note,NoteAdmin)


admin.site.register(Holiday)