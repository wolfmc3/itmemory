# coding=utf-8
from django.db import models


class CustomerBase(models.Model):
    class Meta:
        abstract = True

    name = models.TextField(max_length=255)
    address = models.TextField("Indirizzo", max_length=500, null=True, blank=True)
    city = models.CharField("Città", max_length=200, null=True, blank=True)
    origin_code = models.CharField("Codice cliente", max_length=25, null=True, blank=True)
    email = models.EmailField("Indirizzo email", max_length=255, null=True, blank=True)
    telephone = models.CharField("Telefono", max_length=255, default='', null=True, blank=True)
    reference_person = models.CharField("Persona di riferimento", max_length=255, null=True, blank=True)

    def fulltext(self):
        return self.name + "\n" + self.address + "\n" + self.city + "\n" + self.telephone + "\n" + self.reference_person + "\n" + self.email

    def __str__(self):
        return self.name


class Customer(CustomerBase):
    class Meta():
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"
        ordering = ['name']


class WorkSite(CustomerBase):
    class Meta():
        verbose_name = "Sede"
        verbose_name_plural = "Sedi"
        ordering = ['name']

    customer = models.ForeignKey(Customer, related_name="Worksites")

    def fulltext(self):
        return self.customer.name + "-" + self.name + "\n" + \
            self.address + "\n" + \
            self.city + "\n" + \
            self.telephone + "\n" + \
            self.reference_person + "\n" + \
            self.email + "\n"

    def __str__(self):
        return "{0} ({1})".format(self.name, self.customer.name)
