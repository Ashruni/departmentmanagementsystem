from django import forms


# class staffregistrationforms(forms.Form):
#     staffname = forms.CharField(max_length=30)
#     staffeid = forms.EmailField()
#     staffpassword = forms.CharField(max_length=40)
#     staffconfirmationps = forms.CharField(max_length=40)
class staffloginforms(forms.Form):
    staffnamel = forms.CharField(max_length=30)
    staffpasswordl = forms.CharField(max_length=30)
class studentloginforms(forms.Form):
    studentrollno=forms.CharField()
    studentpassword=forms.CharField(max_length=30)


class departmentsem8markuploadforms(forms.Form):
    suba = forms.IntegerField(min_value=0,max_value=50)
    subb = forms.IntegerField(min_value=0,max_value=50)
    subc = forms.IntegerField(min_value=0,max_value=50)
    subd = forms.IntegerField(min_value=0,max_value=50)
    semester = forms.IntegerField()
    # sube = forms.IntegerField()
    # subf = forms.IntegerField()

class departmentsem8assignmentuploadforms(forms.Form):
    assignmentm1 = forms.IntegerField(min_value=0,max_value=5)
    assignmentm2 = forms.IntegerField(min_value=0,max_value=5)
    assignmentm3 = forms.IntegerField(min_value=0,max_value=5)
    assignmentm4 = forms.IntegerField(min_value=0,max_value=5)

    # assignmentm6 = forms.IntegerField(min_value=0, max_value=50)


class pdfsuploadforms(forms.Form):
    filename = forms.CharField()
    pdfs = forms.FileField()
    date = forms.DateField()
    sem = forms.IntegerField()


class attendanceuploadstudentforms(forms.Form):
    Status = (('present', 'present'),
              ('absent', 'absent'),
              ('late', 'late'),
              ('not uploaded', 'not uploaded')
              )
    date=forms.DateField()
    status=forms.CharField()
    rollno=forms.CharField()

class admindeforms(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    dep=forms.CharField()
class admindeloginforms(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class studentregistrationform(forms.Form):

    studentname=forms.CharField()
    studentrollno=forms.CharField()
    studentimage=forms.ImageField()
    studentdeparment=forms.CharField()
    studentdob=forms.DateField()
    studentbatch=forms.CharField()
    studentsemester=forms.CharField()
    studentpassword=forms.CharField()
    studentemail=forms.EmailField()
    studentclassteacher=forms.CharField()

class staffregistrationform(forms.Form):
    staffname = forms.CharField()
    staffeid = forms.EmailField()
    staffpassword =forms.CharField()
    staffconfirmationps = forms.CharField()
    classteacherbatch=forms.CharField()
    staffsemeter=forms.IntegerField()

class stusernotificationforms(forms.Form):
    content = forms.CharField()
    stnottime = forms.DateTimeField()
class teachernotificationforms(forms.Form):
    content = forms.CharField()
    tnottime = forms.DateTimeField()