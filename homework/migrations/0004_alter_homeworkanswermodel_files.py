# Generated by Django 4.1.4 on 2022-12-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_alter_homeworkanswermodel_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworkanswermodel',
            name='files',
            field=models.FileField(blank=True, upload_to='uploads/homework/dacb51a8-85e3-4d8c-a1b0-5d4d927b00ee'),
        ),
    ]