
# LDAP
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

AUTH_LDAP_SERVER_URI = "ldap://LDAP_SERVER_OR_IP"
AUTH_LDAP_BIND_DN = "CN=Administrator,CN=Users,DC=test,DC=local"
AUTH_LDAP_BIND_PASSWORD = "EMPTY"
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 10,
    ldap.OPT_REFERRALS: 0,
}

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "OU=groups,DC=test,DC=local",
    ldap.SCOPE_SUBTREE,
    ""
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="CN")
AUTH_LDAP_REQUIRE_GROUP = "CN=djangousers,OU=groups,DC=test,DC=local"

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff": "cn=djangostaff,OU=groups,DC=test,DC=local",
    "is_superuser": "CN=djangoadmins,OU=groups,DC=test,DC=local"
}

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "CN=Users,DC=test,DC=local",
    ldap.SCOPE_SUBTREE,
    "(sAMAccountName=%(user)s)"
)
# AUTH_LDAP_USER_DN_TEMPLATE = "CN=%(user)s,CN=Users,DC=test,DC=local"

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)


try:
    from settings_ldap_local import *
except ImportError:
    pass