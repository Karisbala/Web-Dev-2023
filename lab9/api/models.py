from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    city = models.CharField(max_length=300)
    address = models.TextField()

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
    test = models.CharField(max_length=10, null=True)
    def __str__(self):
        return (self.name + f" ({self.company.name})")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': {
                'id': self.company.id,
                'name': self.company.name
            }
        }