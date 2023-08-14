from django.db import models

CATEGORY_CHOICES = [
    (1, 'ข่าวประกาศ'),
    (2, 'โฆษณา'),
    (3, 'บันทึก'),
]

PREFIX_CHOICES = [
    (1, 'นาย'),
    (2, 'นางสาว'),
    (3, 'นาง'),
]

# Create your models here.


class web(models.Model):
    """Model definition for web."""

    # TODO: Define fields here
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    titlev = models.CharField(max_length=255)
    content = models.TextField()
    date_updated = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for web."""

        verbose_name = 'web'
        verbose_name_plural = 'web'

    def __str__(self):
        """Unicode representation of web."""
        return self.titlev



class Author(models.Model):
    """Model definition for Author."""

    # TODO: Define fields here
prefix = models.IntegerField(choices=PREFIX_CHOICES)
first_name = models.CharField(max_length=255)
last_name = models.CharField(max_length=255)
dob = models.DateField()


class Meta:
        """Meta definition for Author."""

        verbose_name = 'Author'
        verbose_name_plural = 'Author'

def __str__(self):
        """Unicode representation of Author."""
        return self,first_name + " " + self,last_name