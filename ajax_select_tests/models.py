from uuid import uuid4

from django.db import models

class TestUser(models.Model):
    USER_TYPES = (
        ('admin', 'Administrator'),
        ('trainee', 'Trainee'),
    )

    uuid = models.CharField(max_length=36, default=make_uuid, unique=True, db_index=True)
    # company = models.ForeignKey(Company, null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='admin')
    job_title = models.CharField(max_length=50, null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=True)

def make_uuid():
    """
    Makes a UUID

    :return: string of UUID
    """
    return str(uuid4())