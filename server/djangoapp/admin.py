from django.contrib import admin
from .models import CarMake, CarModel

# Register CarModelInline for CarMakeAdmin
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

# Register CarModelAdmin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')
    list_filter = ('type', 'year')

# Register CarMakeAdmin
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
