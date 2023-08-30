
class LakeRouter:
    """
    A router to control all database operations on datalake models.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read patient data from database, go to datalake.
        """
        if model._meta.app_label == 'datalake':
            return "datalake"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write anything, return None.
        """
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations always
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure no migrations are applied to this database.
        """
        return None
