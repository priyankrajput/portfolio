from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:47]

    def pub_date_prety(self):
        return self.pub_date.strftime('%b %d, %Y')

    def __str__(self):
        return self.title

