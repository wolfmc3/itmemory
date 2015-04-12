# coding=utf-8
from django.db import models
from django.forms.models import model_to_dict


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
        return u"\n".join([
            self.name,
            self.address if self.address else "",
            self.city if self.city else "",
            self.telephone if self.telephone else "",
            self.reference_person if self.reference_person else "",
            self.email if self.email else "",
            ""
        ])

    def __unicode__(self):
        return self.name


class Customer(CustomerBase):
    class Meta():
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"
        ordering = ['name']

    onlylegal = models.BooleanField(verbose_name="Solo sede legale", default=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        isnew = self.id is None
        super(Customer, self).save(force_insert, force_update, using, update_fields)
        if isnew and not self.onlylegal:
            newworksite = WorkSite(customer=self)
            newworksite.name = "Sede principale"
            newworksite.address = self.address
            newworksite.city = self.city
            newworksite.email = self.email
            newworksite.telephone = self.telephone
            newworksite.reference_person = self.reference_person
            newworksite.save()

class WorkSite(CustomerBase):
    class Meta():
        verbose_name = "Sede"
        verbose_name_plural = "Sedi"
        ordering = ['name']

    customer = models.ForeignKey(Customer, related_name="Worksites")

    def fulltext(self):
        return u"\n".join([
            self.name,
            self.address if self.address else "",
            self.city if self.city else "",
            self.telephone if self.telephone else ( self.customer.telephone if self.customer.telephone else ""),
            self.reference_person if self.reference_person else (self.customer.reference_person if self.customer.reference_person else ""),
            self.email if self.email else (self.customer.email if self.customer.email else ""),
            ""
        ])

    def __unicode__(self):
        return u"{0} ({1})".format(self.name, self.customer.name)
