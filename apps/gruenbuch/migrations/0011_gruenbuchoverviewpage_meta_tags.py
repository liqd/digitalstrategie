# Generated by Django 3.2.12 on 2022-03-31 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_images', '0003_customised_alt_copyright_texts'),
        ('apps_gruenbuch', '0010__restrict_icon_text_link_to_gruenbook_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='gruenbuchoverviewpage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='apps_images.customimage', verbose_name='Search image'),
        ),
    ]
