from django.db import models

# Create your models here.

class users(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    role = models.CharField(max_length=10)

class courses(models.Model):
    cid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=50)
    creatorid = models.ForeignKey(users,on_delete=models.CASCADE)
    enrolllist = models.ManyToManyField(users,related_name='enrolllist')
    coursedescription = models.CharField(max_length=200)
    gradedistribution = models.JSONField()

class enrollments(models.Model):
    cid = models.ForeignKey(courses, on_delete=models.CASCADE)
    uid = models.ForeignKey(users, on_delete= models.CASCADE)

class assesments(models.Model):
    ##################################################################
    ##It should be uid - json(contains quiz grade infomation) table.##
    ##################################################################
    uid = models.ForeignKey(users, on_delete=models.CASCADE)
    grade = models.JSONField()
class quizzes(models.Model):
    qid = models.AutoField(primary_key=True)
    ddl = models.CharField(max_length=100)
    q1 = models.CharField(max_length=50)
    q2 = models.CharField(max_length=50)
    q3 = models.CharField(max_length=50)
    ans = models.CharField(max_length=50)
class assignments(models.Model):
    aid = models.AutoField(primary_key = True)
    ddl = models.CharField(max_length=50)
    url = models.CharField(max_length=50)

class material(models.Model):
    mid = models.AutoField(primary_key = True)
    type = models.CharField(max_length= 10)
    cid = models.ForeignKey(courses, on_delete=models.CASCADE)
    fileapath = models.CharField(max_length=50)

class posts(models.Model):
    pid = models.AutoField(primary_key = True)
    creatorid = models.ForeignKey(users, on_delete=models.CASCADE)
    cid = models.ForeignKey(courses, on_delete=models.CASCADE)
    createtime = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    multimedia = models.CharField(max_length=50)
    replyments = models.ManyToManyField(users, "replyments")
    likes = models.IntegerField()
    editted = models.BooleanField()
    flagged = models.ManyToManyField(users, "flagged")
class replyment(models.Model):
    pid = models.ForeignKey(posts,on_delete=models.CASCADE)
    creator_id = models.ForeignKey(users, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)