from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class PerfilAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'user',
    'slug',
    'role',
    'first_name',
    'last_name',
    'full_name',
    'email',
    'mobile',
    'company',
    'state',
    'sub_state',
    'created_at',
    'updated_at',
    )

