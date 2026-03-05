from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "is_published",
        "created_at",
        "views_counter",
    ]  # Убедитесь, что это список []
    list_filter = ["is_published", "created_at"]
    search_fields = ["title", "content"]
    readonly_fields = ["views_counter", "created_at", "updated_at"]
    list_editable = ["is_published"]
