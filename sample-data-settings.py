from objects.models import SettingGroup, SettingsType


def group(groupname):
    grp = SettingGroup.objects.filter(name=groupname)
    if not grp:
        grp = SettingGroup()
        grp.name = groupname
        grp.save()
    else:
        grp = grp[0]
    return grp


def setting(group_obj, setting_name):
    setobj = SettingsType.objects.filter(group_id=group_obj.id, name=setting_name)
    if not setobj:
        setobj = SettingsType(group=group_obj, name=setting_name)
        setobj.save()


setting(group("Network"), "DNS")
setting(group("Network"), "IP address")
setting(group("Network"), "Gateway")
setting(group("Network"), "Subnet mask")
setting(group("Backup"), "Destinazione")
setting(group("Backup"), "Tipo")
setting(group("Active directory"), "Amministratori")
setting(group("Active directory"), "Utenti")
setting(group("Active directory"), "Ripristino dominio")
setting(group("Amministrazione"), "Utenti")
setting(group("WIFI"), "SSID")
setting(group("WIFI"), "Password")


