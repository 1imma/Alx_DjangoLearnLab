### Admin Interface Configuration

1. **Registered the `Book` Model:**

   - Added the following code to `bookshelf/admin.py`:

     ```python
     from django.contrib import admin
     from .models import Book

     admin.site.register(Book)
     ```

2. **Customized the Admin Interface:**

   - Updated `bookshelf/admin.py` with the following:

     ```python
     from django.contrib import admin
     from .models import Book

     class BookAdmin(admin.ModelAdmin):
         list_display = ('title', 'author', 'publication_year')
         list_filter = ('author', 'publication_year')
         search_fields = ('title', 'author')

     admin.site.register(Book, BookAdmin)
     ```

3. **Created a Superuser:**

   - Ran the command:
     ```bash
     python manage.py createsuperuser
     ```

4. **Accessed the Admin Interface:**
   - Logged in at `http://127.0.0.1:8000/admin/` and verified the `Book` model is visible and customizable.
