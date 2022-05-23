from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    
    list_display = ('staff_id',  'email', 'first_name',
                    'last_name', 'is_employee', 'is_admin')
    list_filter = ('is_staff', 'is_superuser')
    list_display_links = ('staff_id', 'email')
    search_fields = ('email', 'first_name', 'last_name', 'staff_id')
    ordering = ('email',)

    filter_vertical = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)
