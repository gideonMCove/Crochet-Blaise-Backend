from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

SKILL_LEVEL_CHOICES = {
    'BEG': 'Beginner',
    'INT': 'Intermediate',
    'EXP': 'Expert'
}

def validate_positive(value):
    '''Determines if value entered is a positive number'''
    if value < 0 :
        raise ValidationError(
            _("%(value)s needs to be a positive number"),
            params = {"value": value},
        )
# Create your models here.


class Profile(models.Model):
    name = models.CharField(30)    

    def __str__(self):
        return self.name
    
class Patterns(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='patterns')
    name = models.CharField(30)
    description = models.TextField

    def __str__(self):
        return self.name

class Patterns_Yarn(models.Model):
    patterns = models.ForeignKey(Patterns, on_delete=models.CASCADE, related_name='yarn')

    def __str__(self):
        return self.patterns

class Yarn(models.Model):
    patterns = models.ForeignKey(Patterns_Yarn, on_delete=models.CASCADE, related_name='yarn')
    name = models.CharField(60)
    brand = models.CharField(30)
    colour = models.CharField(15)
    price = models.IntegerField(validators=[validate_positive])
    size = models.CharField(30)
    

    def __str__(self):
        return self.name
class Techniques(models.Model):
    patterns = models.ForeignKey(Patterns, on_delete=models.CASCADE, related_name='techniques')
    name = models.CharField(30)
    description = models.TextField()
    skill_level = models.CharField(max_length=3, choices=SKILL_LEVEL_CHOICES, default='Beginner')

    def __str__(self):
        return self.name

class Tools(models.Model):
    Techniques = models.ForeignKey(Techniques, on_delete=models.CASCADE, related_name='tools')
    name = models.CharField(30)
    description = models.TextField()
    brand = models.CharField()

    def __str__(self):
        return self.name