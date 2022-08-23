from django.db import models


class NumberRequested(models.Model):
    number = models.IntegerField('Number')
    result = models.IntegerField('Result', null=True, blank=True)

    def __str__(self):
        return f'{self.number} = {self.result}'
