from django.db import models
from ckeditor.fields import RichTextField
""" dynamic
    User = apps.get_model(app_label='tree_app', model_name=str(book_id))
    print(User)
 attrs = {
                'username': models.CharField(max_length=32),
                'content': models.CharField(max_length=32),
                'path': models.IntegerField(max_length=32),
                'level': models.IntegerField(max_length=32),
                '__module__': 'tree_app.models'
            }
            new_book_table = type(str(book_id), (models.Model,), attrs)
            site = admin.site
            for reg_model in site._registry.keys():
                if new_book_table._meta.db_table == reg_model._meta.db_table:
                    del site._registry[reg_model]
            call_command('makemigrations')
            call_command('migrate')

            admin.site.register(new_book_table,list_display = ['username', 'content', 'path','level'],)
            reload(import_module(settings.ROOT_URLCONF))
            clear_url_caches()
            new_book_table_obj = new_book_table.objects.create(username=request.user, content=node_1, path=1, level=1)
"""
class Book_id(models.Model):
    username=models.CharField(max_length=100)
    book_id=models.IntegerField()
    bookname=models.CharField(max_length=100)

class Book_page(models.Model):
    username = models.CharField(max_length=100)
    content = RichTextField(max_length=2500)
    node_id = models.CharField(max_length=100)
    branch_name = RichTextField(max_length=700, default='Start')
    path = models.CharField(max_length=1000)
    level = models.IntegerField()
    book_id = models.IntegerField()




