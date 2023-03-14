from django.db import models


class Observer(models.Model):
    observer_name = models.TextField(max_length=50)
    subject_number = models.IntegerField()
    day_number = models.IntegerField(primary_key=False)

    class Meta:
        db_table = "observer_data"
