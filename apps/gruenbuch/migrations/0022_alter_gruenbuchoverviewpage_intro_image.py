# Generated by Django 3.2.16 on 2022-11-02 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_images', '0004_alter_customimage_file_hash'),
        ('apps_gruenbuch', '0021_add_json_and_detail_blocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='intro_image',
            field=models.ForeignKey(blank=True, help_text='Image ratio has to be 2:1 or 4:3.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='apps_images.customimage'),
        ),
    ]