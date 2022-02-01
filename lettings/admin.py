from django.contrib import admin

from lettings.models import Letting, Address


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
