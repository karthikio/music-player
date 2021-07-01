from django.db import models

class Music(models.Model):
  song = models.FileField(verbose_name='Song', upload_to='uploads/music/')
  favourite = models.BooleanField(default=False)

  def __str__(self):
    return str(self.song)