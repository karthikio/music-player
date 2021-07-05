from django.db import models
import os


class Music(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True)
  song = models.FileField(verbose_name='Song', upload_to='uploads/music/')
  favourite = models.BooleanField(default=False)

  def __str__(self):
    return str(self.name)

  # def file_name(self):
  #   full_path = self.song.name
  #   base = os.path.basename(full_path)
  #   file_name = os.path.splitext(base)[0]
  #   return file_name

  def save(self, commit=True):
    song = super()
    full_path = self.song.name
    base = os.path.basename(full_path)
    self.name = os.path.splitext(base)[0]
    if commit:
      song.save()
    return song