from django.db import models
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    #null=True means that the text could be empty for database and blank for django
    discription = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    #Make timestamp when created
    created = models.DateTimeField(auto_now_add=True)
    #Unique id with uuid, set to pk and not editable
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


