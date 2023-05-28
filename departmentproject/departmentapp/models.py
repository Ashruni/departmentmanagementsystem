from django.db import models

# Create your models here.


class staffregistrationmodel(models.Model):
    staffname = models.CharField(max_length=30)
    staffeid = models.EmailField()
    staffpassword = models.CharField(max_length=40)
    staffconfirmationps = models.CharField(max_length=40)
    classteacherbatch=models.CharField(max_length=90)
    staffsemeter=models.IntegerField()



    def __str__(self):
        return self.staffname

class studentregistrationmodel(models.Model):

    studentname=models.CharField(max_length=30)
    studentrollno=models.CharField(max_length=30)
    studentimage=models.ImageField(upload_to ='departmentapp/static')
    studentdeparment=models.CharField(max_length=30)
    studentdob=models.DateField()
    studentbatch=models.CharField(max_length=30)
    studentsemester=models.CharField(max_length=30)
    studentpassword=models.CharField(max_length=30)
    studentemail=models.EmailField()
    studentclassteacher=models.CharField(max_length=50)

    # studentfather = models.CharField(max_length=50)
    # studentmother = models.CharField(max_length=50)
    # studentplace = models.CharField(max_length=50)
    # studentaddress = models.CharField(max_length=50)

    def __str__(self):
        return self.studentname




class departmentsem8subjects(models.Model):
    semester = models.IntegerField()
    sub1 = models.CharField(max_length=100)
    sub2 = models.CharField(max_length=100)
    sub3 = models.CharField(max_length=100)
    sub4 = models.CharField(max_length=100)






    def __str__(self):
        return self.sub1

class departmentsemmarkupload(models.Model):
    sid = models.IntegerField()
    semester = models.IntegerField(default="-")
    suba = models.IntegerField(default="-")
    subb = models.IntegerField(default="-")
    subc = models.IntegerField(default="-")
    subd = models.IntegerField(default="-")
    # sube = models.IntegerField()
    # subf = models.IntegerField()


    # def __str__(self):
    #     return self.sid
#
# class departmentsem8assignmentsubnames(models.Model):
#     assignmentsub1= models.CharField(max_length=90)
#     assignmentsub2 = models.CharField(max_length=90)
#     assignmentsub3 = models.CharField(max_length=90)
#     assignmentsub4 = models.CharField(max_length=90)
    # semeseter8=models.IntegerField()
    # assignmentsub5 = models.CharField(max_length=90)
    # assignmentsemeseter =models.IntegerField()
    # assignmentsub5 = models.CharField(max_length=90)
    # assignmentsub6 = models.CharField(max_length=90)



class departmentsem8assignmentuploadmodel(models.Model):
    sid = models.IntegerField()
    assignmentm1 = models.IntegerField(default="-")
    assignmentm2 = models.IntegerField(default="-")
    assignmentm3 = models.IntegerField(default="-")
    assignmentm4 = models.IntegerField(default="-")
    # assignmentm5 = models.IntegerField()
    # assignmentm6 = models.IntegerField()


class department(models.Model):
    sidi = models.IntegerField()
    assignmentmi = models.IntegerField()

class semsubjectsuploadother(models.Model):
    subo1=models.CharField(max_length=80)
    subo2=models.CharField(max_length=80)
    subo3 = models.CharField(max_length=80)
    subo4 = models.CharField(max_length=80)
    subo5 = models.CharField(max_length=80)
    subo6 = models.CharField(max_length=80)
    semestero = models.IntegerField()
class stusernotification(models.Model):
    content = models.CharField(max_length=200)
    stnottime = models.DateTimeField(auto_now_add=True)
class teachernotification(models.Model):
    content = models.CharField(max_length=200)
    tnottime = models.DateTimeField(auto_now_add=True)
class departmentsemassignmentsubnames(models.Model):
    sem=models.IntegerField()
    assgsub1= models.CharField(max_length=90)
    assgsub2 = models.CharField(max_length=90)
    assgsub3 = models.CharField(max_length=90)
    assgsub4 = models.CharField(max_length=90)
    def __str__(self):
        return self.assgsub1

class internals(models.Model):
    pid =models.IntegerField
    pp1= models.IntegerField(default="-")
    pp2 = models.IntegerField(default="-")
    pp3 = models.IntegerField(default="-")
    pp4 = models.IntegerField(default="-")

class pdfsuploadmodels(models.Model):
    filename=models.CharField(max_length=50)
    pdfs=models.FileField(upload_to='departmentapp/static')
    date=models.DateField(auto_now_add=True)
    sem=models.IntegerField()

class attendanceuploadstudents(models.Model):
    date=models.DateField()
    Status=(('present','present'),
            ('absent', 'absent'),
            ('late', 'late'),
            ('not uploaded','not uploaded')
            )
    status = models.CharField(max_length=70, choices=Status,default='not uploaded')

    rollno=models.CharField(max_length=30)
class admindetmodel(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    dep=models.CharField(max_length=20)