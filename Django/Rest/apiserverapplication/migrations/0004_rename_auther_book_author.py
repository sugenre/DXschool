# Generated by Django 4.2.3 on 2023-07-27 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apiserverapplication", "0003_rename_descirption_book_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="auther",
            new_name="author",
        ),
    ]
