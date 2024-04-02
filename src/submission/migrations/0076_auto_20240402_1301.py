# Generated by Django 3.2.20 on 2024-04-02 12:01

from django.db import migrations, models
import django.db.models.deletion


def migrate_relationship_to_fk(apps, schema_editor):
    Article = apps.get_model('submission', 'Article')
    for article in Article.objects.all():
        for funder in article.funders.all():
            print(f"Adding FK to {funder.pk}")
            funder.article = article
            funder.save()


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0075_auto_20240320_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='funder',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='submission.article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='funders',
            field=models.ManyToManyField(blank=True, related_name='funders', to='submission.Funder'),
        ),
        migrations.RunPython(
            migrate_relationship_to_fk,
            reverse_code=migrations.RunPython.noop,
            atomic=False,
        ),
    ]