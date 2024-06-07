from django.contrib import admin

from .models import Product, Home_products, home_picture, conatact_us, contact_info, about_team, Users


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', "price", "image")


@admin.register(Home_products)
class Home_productsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')


@admin.register(home_picture)
class home_pictureAdmin(admin.ModelAdmin):
    list_display = ('image',)


admin.site.register(conatact_us)


@admin.register(contact_info)
class contact_infoAdmin(admin.ModelAdmin):
    list_display = ('image', 'address', 'phone', 'email')


@admin.register(about_team)
class about_teamAdmin(admin.ModelAdmin):
    list_display = ('image', 'full_name', 'job')




# --------------------------------------------------------------------------------------------------
admin.site.register(Users)
