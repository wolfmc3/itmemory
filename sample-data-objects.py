from objects.models import HardwareObject
from customers.models import WorkSite
import random

OBJECT_PRODUCER = ["Hp",
                   "Asus",
                   "Zyxel",
                   "Cisco",
                   "Fujitsu"]
OBJECT_PRODUCER_TITLE = ["ML", "DT", "ST", "RR"]
for x in range(30):
    ws = WorkSite.objects.all()[random.randint(0, WorkSite.objects.count() - 1)]
    newobj = HardwareObject(worksite=ws)
    newobj.name = '{0} {1} {2}'.format(
        OBJECT_PRODUCER[random.randint(0, len(OBJECT_PRODUCER) - 1)].title(),
        OBJECT_PRODUCER_TITLE[random.randint(0, len(OBJECT_PRODUCER_TITLE) - 1)],
        str(random.randint(0, 9999))
    )
    newobj.item = 'ITM {0}'.format(str(random.randint(0, 9999)))
    newobj.serial = 'S{0}'.format(str(random.randint(0, 999999)))
    newobj.know_name = newobj.name[:7]
    newobj.primary_ip = "192.168.{0}.{1}".format(random.randint(1, 254), random.randint(1, 254))
    newobj.location = "Stanza {0}".format(random.randint(1, 25))
    newobj.save()
