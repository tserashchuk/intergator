# Generated by Django 5.1.1 on 2024-11-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitrixsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rewiew_company',
            new_name='review_company',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rewiew_job',
            new_name='review_job',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rewiew_person',
            new_name='review_person',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rewiew_text',
            new_name='review_text',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rewiew_image',
        ),
        migrations.AddField(
            model_name='review',
            name='review_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Скан отзыва'),
        ),
        migrations.AddField(
            model_name='review',
            name='review_image_video',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Превью видео'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2024-11-28 13:39:04.410750', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='cat_slug',
            field=models.CharField(default='slug2024-11-28 13:39:04.410750', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_slug',
            field=models.CharField(default='article2024-11-28 13:39:04.410750', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='casecategory',
            name='cat_slug',
            field=models.CharField(default='slug2024-11-28 13:39:04.410750', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='categorywebinar',
            name='cat_slug',
            field=models.CharField(default='slug2024-11-28 13:39:04.410750', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_slug',
            field=models.CharField(default='article2024-11-28 13:39:04.410750', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='webinar_slug',
            field=models.CharField(default='article2024-11-28 13:39:04.410750', max_length=200, verbose_name='URL'),
        ),
    ]