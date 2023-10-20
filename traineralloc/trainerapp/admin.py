from django.contrib import admin
from .models import Course 
from .models import Slot
from .models import Batch
from .models import Trainer
from .models import Student
from import_export.admin import ImportExportModelAdmin

class Students(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('FullName','Qualification','CourseName','trainer','Batch','Time')
# Register your models here.
admin.site.register(Course)
admin.site.register(Slot)
admin.site.register(Batch)
admin.site.register(Trainer)
admin.site.register(Student,Students)
