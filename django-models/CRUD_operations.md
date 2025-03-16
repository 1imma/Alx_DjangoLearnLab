```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

output:
Book object created successfully.

```python
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
```

output:
Title: 1984, Author: George Orwell, Year: 1949

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

output:
Title updated successfully.

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
```

output:
<QuerySet []>
