from django.db import models


class Customer(models.Model):
    name = models.TextField(max_length=255)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=200)
    origin_code = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    reference_person = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkSite(Customer):
    customer = models.ForeignKey(Customer, related_name="Worksites")

    def __str__(self):
        return self.customer.name + "\n" + self.name
