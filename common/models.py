from django.db import models


class CommonModel(models.Model):
    """Common Model Definition"""

    # the time when Object is first Created.
    created_at = models.DateTimeField(auto_now_add=True)
    # set the time when Object is modified.
    updated_at = models.DateTimeField(auto_now=True)
    # Django doesn't save model in DB
    # is not going to use for the database
    
    class Meta:
        abstract = True
