from customers.models import Customer, WorkSite
import random

CUSTOMER_NAMES = ["abc",
                  "pippo",
                  "pluto",
                  "paperino",
                  "paperone",
                  "consulting",
                  "dollar",
                  "information",
                  "fast",
                  "good"]
CUSTOMER_NAMES_TITLE = ["Srl", "Snc", "Sas", "Spa"]
for x in range(25):
    newcust = Customer()
    newcust.name = CUSTOMER_NAMES[random.randint(0, len(CUSTOMER_NAMES) - 1)].title() + ' ' + \
                   CUSTOMER_NAMES[random.randint(0, len(CUSTOMER_NAMES) - 1)] + ' ' + \
                   CUSTOMER_NAMES_TITLE[random.randint(0, len(CUSTOMER_NAMES_TITLE) - 1)]

    newcust.address = 'via {0}'.format(CUSTOMER_NAMES[random.randint(0, len(CUSTOMER_NAMES) - 1)])
    newcust.city = "City"
    newcust.email = "email@localhost.com"
    newcust.reference_person = CUSTOMER_NAMES[random.randint(0, len(CUSTOMER_NAMES) - 1)]
    newcust.origin_code = "sample"
    newcust.telephone = "008881123456"
    newcust.save()
    for sx in range(3):
        newws = WorkSite(customer=newcust)
        newws.name = "Branch {0} {1}".format(str(sx), newcust.name)
        newws.address = "via {0}".format(CUSTOMER_NAMES[random.randint(0, len(CUSTOMER_NAMES) - 1)])
        newws.city = "City"
        newws.email = "email@localhost.com"
        newws.reference_person = CUSTOMER_NAMES[random.randint(0, len(CUSTOMER_NAMES) - 1)]
        newws.origin_code = "sample"
        newws.telephone = "008881123456"
        newws.save()