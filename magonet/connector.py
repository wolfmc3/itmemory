from django.conf import settings
import pymssql


class MagoNet(object):

    SELECT_CUSTOMERS = "SELECT * FROM MA_CustSupp WHERE CustSuppType = \'3211264\' and disabled = \'0\'"

    def connect(self):
        self._connection = pymssql.connect(
            settings.MAGONETDB['server'],
            settings.MAGONETDB['user'],
            settings.MAGONETDB['password'],
            settings.MAGONETDB['db'],
        )

    def disconnect(self):
        if self._connection:
            self._connection.close()

    def __del__(self):
        self.disconnect()

    def opencursor(self):
        return self._connection.cursor(as_dict=True)

    def getcustomer_byname(self, name):
        cursor = self.opencursor()
        containname = "%{0}%".format(name)
        cursor.execute(
            self.SELECT_CUSTOMERS + " and CompanyName like %s",
            (containname, )
        )
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def getcustomer_byid(self, id):
        cursor = self.opencursor()
        cursor.execute(
            self.SELECT_CUSTOMERS + " and CustSupp = %s",
            (id, )
        )
        rows = cursor.fetchall()
        cursor.close()
        return rows

