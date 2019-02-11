from django.db import models


def get_chief():
    # TODO: add logic
    return None


class Profile(models.Model):
    first_name = models.CharField('First name', max_length=50)
    middle_name = models.CharField('Middle name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    position = models.CharField('Position', max_length=100)
    employment_date = models.DateField('Employment date')
    salary = models.FloatField('Salary')
    chief = models.ForeignKey(
        'self',
        verbose_name='Chief',
        null=True,
        blank=True,
        related_name='employees',
        on_delete=models.SET(get_chief)
    )

    def get_full_name(self):
        middle_name = self.middle_name.split(' ')[0]
        return '{} {} {}'.format(self.first_name, middle_name, self.last_name)
