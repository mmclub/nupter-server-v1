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


class Jwc(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100)
    time = models.IntegerField(blank=True)
    isCheck = models.BooleanField()

    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)

  
    
class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100)
    time = models.IntegerField(blank=True)
    isCheck = models.BooleanField()


    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)
    

class Trade(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100)
    time = models.IntegerField(blank=True)
    isCheck = models.BooleanField()


    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)
    
    

class Lost(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100)
    time = models.IntegerField(blank=True)
    isCheck = models.BooleanField()


    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)



class Newspaper(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=100)
    time = models.IntegerField(blank=True)
    isCheck = models.BooleanField()


    def __unicode__(self):
        return u'%s %s' % (self.title, self.content)
    
    
    

    