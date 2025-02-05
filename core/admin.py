from django.contrib import admin
from core import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email")
    ordering = ("id",)

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "passport", "snils")

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "region", "city", "area")
    ordering = ("id",)

@admin.register(models.EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ("id", "relations", "relation", 'name', "phone")
    ordering = ("id",)

    @admin.display(description="Relation")
    def relations(self, obj):
        return (obj.user.first_name + " " + obj.user.last_name).title()