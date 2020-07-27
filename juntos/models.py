from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id, dn, groups, name, tenant, username, monitoring_admin):
        self.id = user_id
        self.dn = dn
        self.groups = groups
        self.name = name
        self.tenant = tenant
        self.username = username
        self.monitoring_admin = monitoring_admin


class Resource:

    def __init__(self, username, password):
        # self.auth = HTTPBasicAuth(username, password)
        pass
