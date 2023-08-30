    
class DefaultRouter:
    """
    A router to control all database operations except database models.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read data
        """
        return "default"

    def db_for_write(self, model, **hints):
        """
        Attempts to write anything, return None.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations always
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure no migrations are applied to this database.
        """
        return True