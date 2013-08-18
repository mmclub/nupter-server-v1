from django.db import models


class Jwc(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100, blank=True)
    time = models.IntegerField(blank=True)
    isCheck = models.BooleanField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)

  
    
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100, blank=True)
    time = models.IntegerField(blank=True)
    isCheck = models.BooleanField(blank=True)



    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)
    

    

class Lost(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100, blank=True)
    time = models.IntegerField(blank=True, null=True)
    isCheck = models.BooleanField(blank=True)


    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)



class Newspaper(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100, blank=True)
    time = models.IntegerField(blank=True)
    isCheck = models.BooleanField(blank=True)



    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)
    
    
    

    