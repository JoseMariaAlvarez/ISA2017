class INRRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'INR':
            return 'Auth'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'INR':
            return 'Auth'
        return None

    def allow_syncdb(self, db, model):
        if db == 'Auth':
            return model._meta.app.app_label == 'INR':
        elif model._meta.app.app_label == 'INR':
            return False
        return None
