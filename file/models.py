from django.db import models

class File(models.Model):
    class FileStatus(models.IntegerChoices):
        PENDING = 0
        PROCESSING = 1
        PROCESSED = 2
        FAILED = 3

    lines_count = models.IntegerField(null=True)
    file_size = models.IntegerField(null=True)
    file_path = models.CharField(max_length=120)
    status = models.IntegerField(choices=FileStatus.choices, default=FileStatus.PENDING)

