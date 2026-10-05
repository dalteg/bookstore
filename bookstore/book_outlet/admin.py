from django.contrib import admin
from .models import Author, Book, Address, Country
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",  "address")

    def display_address(self, obj):
        return obj.address


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('author', 'rating',)
    list_display = ("title", "author", "display_country")

    @admin.display(description="Published Country")
    def display_country(self, obj):
        return ", ".join(
            country.country for country in obj.published_country.all()
        )

admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
