from django.db import models
import os


class Music(models.Model):
  song = models.FileField(verbose_name='Song', upload_to='uploads/music/')
  favourite = models.BooleanField(default=False)

  def __str__(self):
    return str(self.song)

@property
def get_file_name(filename):
  full_path = filename
  base = os.path.basename(full_path)
  file_name = os.path.splitext(base)[0]
  return file_name
