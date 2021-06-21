from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): # Post is the name of our django model (models.Model) so that it can be saved on our database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # ForeignKey is the link to another model
    title = models.CharField(max_length=200)# limited number of characters -- CharField
    text = models.TextField() # long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # __ => dunder (short for double underscore)
        return self.title
