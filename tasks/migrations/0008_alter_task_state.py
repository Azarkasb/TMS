# Generated by Django 4.0.4 on 2022-07-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0007_task_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="state",
            field=models.CharField(
                choices=[("P", "تعریف شده"), ("A", "واگذار شده"), ("D", "انجام شده")],
                default="P",
                max_length=1,
            ),
        ),
    ]
