from django.db import models

class Company(models.Model):
    name = models.CharField(verbose_name='Name', max_length=300)
    description = models.TextField(verbose_name='Description')
    city = models.CharField(verbose_name='City', max_length=200)
    address = models.TextField(verbose_name='Address', default=False)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return f'{self.id}: {self.name}'

class Vacancy(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    description = models.TextField(verbose_name='Description')
    salary = models.FloatField(verbose_name='Salary')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='vacancies')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }

    # to get more information in admin side
    def __str__(self):
        return f'{self.id}: {self.name}'

