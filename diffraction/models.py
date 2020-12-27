from django.db import models

# Create your models here.
class AboutCompany(models.Model):
    """Общая информация о компании"""
    information = models.TextField()

    def __str__(self):
        return self.information

class DirectionOfActivity(models.Model):
    direction = models.CharField(max_length=250)
    company = models.ForeignKey(
        AboutCompany,
        on_delete=models.CASCADE,
        related_name='directions',
    )

    def __str__(self):
        return self.direction

