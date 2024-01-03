from django.contrib.admin import register as admin_register, ModelAdmin
from .models import Employe


@admin_register(Employe)
class EmployeAdmin(ModelAdmin):

    fieldsets = (
        ('Резюме', {'fields': ('name', 'age', 'experience', 'previous_job', 'about_me', 'phone', )}),
        ('Дополнительно', {'fields': ('is_favourite', 'note',)}),
    )

    list_display = ('name', 'age', 'experience', 'phone', 'is_favourite', 'created_at', 'id',)
    search_fields = ('id', 'name', 'phone', 'previous_job', 'about_me', 'note', )
    list_filter = ('is_favourite', 'age', 'experience', 'created_at', )
