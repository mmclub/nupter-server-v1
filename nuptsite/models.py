from django.db import models

class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    college = models.CharField(max_length=50, blank=True)
    major = models.CharField(max_length=50, blank=True)
    classes = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = u'students'
    def __unicode__(self):
    	return u'%s %s' % (self.number, self.name)

    	