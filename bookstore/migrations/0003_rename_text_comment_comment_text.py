# Generated by Django 4.0 on 2022-01-02 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_alter_book_created_date_alter_book_updated_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment_text',
        ),
    ]
