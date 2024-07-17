# Generated by Django 4.2 on 2024-07-17 09:52

from django.db import migrations
from utils import migration_utils

OLD_VALUE_ONE = 'Dear {{ review_assignment.editor.first_name }}, <br><br>This is a notification that the reviewer status on "{{ article.safe_title }}" in {{ article.journal.name }} has been updated.  You can view more information on the journal site: {{ review_in_review_url }}  <br><br>All best wishes, <br>{{ request.user.signature }}'
OLD_VALUE_TWO = 'Dear {{ review_assignment.editor.full_name }}, <br/><br/>This is a notification that the reviewer status on "{{ article.safe_title }}" in {{ article.journal.name }} has been updated.  You can view more information on the journal site: {{ review_in_review_url }}  <br/><br/>Regards,'
OLD_VALUE_THREE = 'Dear {{ review_assignment.editor.full_name }}, <br/><br/>This is a notification that the reviewer status on "{{ article.safe_title }}" in {{ article.journal.name }} has been updated.  You can view more information on the journal site: {{ review_in_review_url }}  <br/><br/>Regards, <br/>{{ request.user.signature }}'
OLD_VALUE_FOUR = 'Dear {{ review_assignment.editor.full_name }}, <br><br>This is a notification that the reviewer status on "{{ article.safe_title }}" in {{ article.journal.name }} has been updated.  You can view more information on the journal website at: {{ review_in_review_url }}  <br><br>Best wishes,<br> <br>{{ request.user.signature }}'
OLD_VALUE_FIVE = 'Dear {{ review_assignment.editor.full_name }}, <br><br>This is a notification that the reviewer status on "{{ article.safe_title }}" in {{ article.journal.name }} has been updated.  You can view more information on the journal site: {{ review_in_review_url }}  <br><br>Regards, <br>{{ request.user.signature }}'
OLD_VALUE_SIX = 'Dear {{ review_assignment.editor.full_name }}, <br><br>This is a notification that the reviewer status on "{{ article.safe_title }}" in {{ article.journal.name }} has been updated.  You can view more information on the journal site: {{ review_in_review_url }}  <br><br>Regards,'
NEW_VALUE = "<p>Dear {{ review_assignment.editor.full_name }},</p><p>{{ review_assignment.reviewer.full_name }} has completed their review of \"{{ review_assignment.article.title }}\"{% if review_assignment.decision %} with this recommendation: {{ review_assignment.get_decision_display }}{% endif %}.</p><p>You can view more information on the journal site: {% journal_url 'review_view_review' review_assignment.article.pk review_assignment.pk %}</p><p>Regards,</p>"


def replace_review_completed_ack(apps, schema_editor):
    migration_utils.update_default_setting_values(
        apps,
        setting_name='review_complete_acknowledgement',
        group_name='email',
        values_to_replace=[OLD_VALUE_ONE, OLD_VALUE_TWO, OLD_VALUE_THREE, OLD_VALUE_FOUR, OLD_VALUE_FIVE, OLD_VALUE_SIX],
        replacement_value=NEW_VALUE,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0095_auto_20240605_1024'),
    ]N

    operations = [
        migrations.RunPython(
            replace_review_completed_ack,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
