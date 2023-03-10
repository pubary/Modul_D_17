from django.db import models

# Create your models here.

class CensorVoc(models.Model):
    word = models.CharField(max_length=63)

    @property
    def len_word(self):
        return len(self.word)

