from django.contrib import admin
from .models import UploadedFile, File

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ['user']

class FileAdmin(admin.ModelAdmin):
    list_display = ['uploaded_file', 'file']

admin.site.register(UploadedFile, UploadedFileAdmin)
admin.site.register(File, FileAdmin)
