from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import*
from .models import*
from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import datetime

#
#
# Create your views here.
# def staffregistration(request):
#     if request.method == 'POST':
#         a=staffregistrationforms(request.POST)
#         if a.is_valid():
#             us = a.cleaned_data["staffname"]
#             es = a.cleaned_data["staffeid"]
#             pp = a.cleaned_data["staffpassword"]
#             cp = a.cleaned_data["staffconfirmationps"]
#             if pp == cp:
#                 b=staffregistrationmodel(staffname=us, staffeid=es, staffpassword=pp, staffconfirmationps=cp)
#                 b.save()
#                 return redirect(stafflogin)
#
#         else:
#             return HttpResponse('REGISTRATION FAILED')
#
#     return render(request,'staffregistration.html')
# staff 123
def index(request):
    if request.method == 'POST':
        a = staffloginforms(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["staffnamel"]
            ps = a.cleaned_data["staffpasswordl"]

            b = staffregistrationmodel.objects.all()
            for i in b:
                tid= i.id
                batch = i.classteacherbatch
                stffsem= i.staffsemeter

                if nm == i.staffname and ps == i.staffpassword:
                    return render(request,"Teacherprofile.html",{"nm":nm,"batch":batch,"tid":tid,"stffsem":stffsem})
            else:
                return HttpResponse("login failed")
    return render(request,'index.html')


def studentlogin(request):
    if request.method == 'POST':
        a = studentloginforms(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["studentrollno"]
            ps = a.cleaned_data["studentpassword"]

            b = studentregistrationmodel.objects.all()
            for i in b:
                snm=i.studentname
                sb=i.studentsemester
                sid=i.id
                sbt=i.studentbatch
                # request.session['id'] = sid
                if nm == i.studentrollno and ps == i.studentpassword:
                    return render(request,"Studentprofile.html",{'snm':snm,'sb':sb,'sid':sid,'sbt':sbt})
            else:
                return HttpResponse("login failed")
    return render(request, 'Studentlogin.html')
def batch1(request,id):
    c = staffregistrationmodel.objects.get(id=id)
    staffnm =c.staffname
    staffid = c.staffsemeter


    b = studentregistrationmodel.objects.filter(studentsemester=staffid).only('studentsemester','studentname','studentrollno','studentemail')

    return render(request, "studentlist.html",{"b":b})
    #     sid=[]
    #     sname=[]
    #     rollno=[]
    #     email=[]
    #     id=i.id
    #     nm=i.studentname
    #     rn=i.studentrollno
    #     em=i.studentemail
    #     sid.append(id)
    #     sname.append(nm)
    #     rollno.append(rn)
    #     email.append(em)
    # zipping=zip(sname,rollno,email)



def semestereightsubjects(request,id):
    # stuid=request.session['id']
    v = studentregistrationmodel.objects.get(id=id)
    s=v.studentsemester
    b = departmentsem8subjects.objects.filter(semester=s)
    if departmentsemmarkupload.objects.filter(sid=id).exists():
        return HttpResponse("Marks are already uploaded, if you want to edit, go to the edit page")
    if request.method == "POST":
        a = departmentsem8markuploadforms(request.POST)
        if a.is_valid():
            sa = a.cleaned_data["suba"]
            sb = a.cleaned_data["subb"]
            sc = a.cleaned_data["subc"]
            sd = a.cleaned_data["subd"]
            sm = a.cleaned_data["semester"]

            # se = a.cleaned_data["sube"]
            # sf =a.cleaned_data["subf"]
            # b = departmentsem8markupload(sid=id,suba=sa,subb=sb,subc=sc,subd=sd,sube=se,subf=sf)

            g = departmentsemmarkupload(sid=id, suba=sa, subb=sb, subc=sc, subd=sd,semester=sm)
            g.save()
            return HttpResponse('Successfully  added')


        else:
            return HttpResponse('not saved')

    return render(request,"semestermarks.html",{"b":b,"v":v})
# def departmentothersemestersub(request):
#     return render(request,"departmentothersemesters.html")

def semassignment8(request,id):
    v = studentregistrationmodel.objects.get(id=id)
    sim=v.studentsemester

    b = departmentsemassignmentsubnames.objects.filter(sem=sim).only('assgsub1','assgsub2','assgsub3','assgsub4')
    if departmentsem8assignmentuploadmodel.objects.filter(sid=id).exists():
        return HttpResponse("Marks are already uploaded, if you want to edit, go to the edit page")
    if request.method == "POST":
        a = departmentsem8assignmentuploadforms(request.POST)
        if a.is_valid():
            sa = a.cleaned_data["assignmentm1"]
            sb = a.cleaned_data["assignmentm2"]
            sc = a.cleaned_data["assignmentm3"]
            sd = a.cleaned_data["assignmentm4"]

            o = departmentsem8assignmentuploadmodel(sid=id, assignmentm1=sa, assignmentm2=sb, assignmentm3=sc, assignmentm4=sd)

            o.save()
            return HttpResponse('saved')
        else:
            return HttpResponse('not saved')
    else:
        return render(request, "sem8assignmentupload.html", {"b": b, "v": v})




def studentprofileview(request,id):
    b=studentregistrationmodel.objects.get(id=id)
    nme=[]
    rollno=[]
    img=[]
    dep=[]
    dob=[]
    batch=[]
    sem=[]
    email=[]
    classteacher=[]
    im=str(b.studentimage).split('/')[-1]
    img.append(im)
    nm = b.studentname
    nme.append(nm)
    db = b.studentdob
    dob.append(db)
    bt = b.studentbatch
    batch.append(bt)
    rn = b.studentrollno
    rollno.append(rn)
    emailid = b.studentemail
    email.append(emailid)
    semesters = b.studentsemester
    sem.append(semesters)
    dept = b.studentdeparment
    dep.append(dept)
    clteacher = b.studentclassteacher
    classteacher.append(clteacher)
    combining=zip(img,nme,rollno,dep,dob,batch,sem,email,classteacher)
    return render(request,"profileviewofstudent.html",{"combining":combining})
def studentaca(request):
    return render(request,'studentacademics8.html')
def internalmarks8(request,id):
    st = studentregistrationmodel.objects.get(id=id)
    stnm=st.studentname
    stb=st.studentsemester
    b = departmentsemmarkupload.objects.filter(sid=id)

    if len(b)==0:
        return HttpResponse("Internal marks can only be seen if the series marks and assignment marks are uploaded")


    p1=0
    p2=0
    p3=0
    p4=0
    for i in b:
        sub1=i.suba
        sub2=i.subb
        sub3=i.subc
        sub4=i.subd
        s = i.sid
        p1=int(sub1/50*80)
        p2=int(sub2/50*80)
        p3=int(sub3/50*80)
        p4=int(sub4/50*80)
    assi = departmentsemassignmentsubnames.objects.filter(sem=stb)
    assu = departmentsem8assignmentuploadmodel.objects.filter(sid=id)
    if len(assu)==0:
        return HttpResponse("Internal marks can only be seen if the assignment marks are uploaded")
    assi1= None
    assi2 = None
    assi3 = None
    assi4 = None

    for i in assu:
        assi1=i.assignmentm1
        assi2=i.assignmentm2
        assi3=i.assignmentm3
        assi4=i.assignmentm4
        f1 = assi1 + p1
        f2 = assi2 + p2
        f3 = assi3 + p3
        f4 = assi4 + p4
    return render(request,'studentacademics8.html',{"s":s,"b":b,"assi":assi,"assu":assu,"f1":f1,"f2":f2,"f3":f3,"f4":f4,"stnm":stnm,"stb":stb})

def logout_view(request):
    request.session.clear()
    request.session.set_expiry(-1)
    logout(request)
    return redirect(index)
def stlogout_view(request):
    request.session.clear()
    request.session.set_expiry(-1)
    logout(request)
    return redirect(index)
def stusernotificationf(request,id):
    o=studentregistrationmodel.objects.get(id=id)

    nm=o.studentname
    sem=o.studentsemester

    a = stusernotification.objects.all()  # image name , image file
    stunottime = []
    cont = []

    return render(request, 'studentnotification.html',{'a':a,'nm':nm,'sem':sem})
def teachernotifications(request,id):
    o = staffregistrationmodel.objects.get(id=id)

    nm=o.staffname
    sem=o.staffsemeter

    a = teachernotification.objects.all()  # image name , image file


    return render(request,'teachernotif.html',{'a':a,'nm':nm,'sem':sem})

def editdel(request):
    return render(request,'editdeletepage.html')
def studenteditpage(request,id):

    student=studentregistrationmodel.objects.get(id=id)
    s=student.studentsemester
    snm=student.studentname
    sb=student.studentbatch

    b = departmentsem8subjects.objects.filter(semester=s)
    m = departmentsemmarkupload.objects.filter(sid=id)

    if request.method=='POST':
        for i in m:

            i.semester=request.POST.get("semester")
            i.subar = request.POST.get("suba")
            i.subb = request.POST.get("subb")
            i.subc = request.POST.get("subc")
            i.subd = request.POST.get("subd")
            i.save()
            return redirect(editseriesmessage)
    return render(request,'studentseriesedit.html',{"b":b,"student":student,"m":m})

def studentasstmarksedit(request,id):
    v = studentregistrationmodel.objects.get(id=id)
    sim = v.studentsemester

    b = departmentsemassignmentsubnames.objects.filter(sem=sim).only('assgsub1', 'assgsub2', 'assgsub3', 'assgsub4')
    asg = departmentsem8assignmentuploadmodel.objects.filter(sid=id)
    if request.method=='POST':
        # assg=departmentsem8assignmentuploadforms(request.POST)
        # if assg.is_valid():
            for i in asg:
             i.assignmentm1 =request.POST.get("assignmentm1")
             i.assignmentm2 = request.POST.get("assignmentm2")
             i.assignmentm3 = request.POST.get("assignmentm3")
             i.assignmentm4 = request.POST.get("assignmentm4")
             i.save()
             return redirect(editasgmessages)

    return render(request,'editasstmarks.html',{"v":v,"b":b,"asg":asg})
def editasgmessages(request):
    return render(request,"editasgmessage.html")
def editseriesmessage(request):
    return render(request,"editseriesmessage.html")
def seriesmarkuploadsstatuss(request,id):
    return render(request,'seriesmarkuploadsstatus.html')
def pdfsuploads(request,id):
    if request.method=='POST':
        a=pdfsuploadforms(request.POST,request.FILES)

        if a.is_valid():
            d=a.cleaned_data['filename']
            f=a.cleaned_data['pdfs']
            s=a.cleaned_data['date']
            seme=a.cleaned_data['sem']
            b=pdfsuploadmodels(filename=d,pdfs=f,date=s,sem=seme)
            b.save()
            return HttpResponse("success")
    return render(request,'studymaterial.html')
def studymaterialview(request,id):
    te=studentregistrationmodel.objects.get(id=id)
    snm=te.studentname
    sbt=te.studentbatch
    ste=te.studentsemester
    stm=pdfsuploadmodels.objects.filter(sem=ste)
    if len(stm)==0:
        return HttpResponse("not enough data to show")
    filenm=[]
    pdf=[]
    dates=[]
    semester=[]
    for i in stm:
        f=i.filename
        filenm.append(f)
        p =str(i.pdfs).split('/')[-1]
        pdf.append(p)
        d=i.date
        dates.append(d)
        s=i.sem
        semester.append(s)
    combine=zip(filenm,pdf,dates,semester)
    return render(request,'viewstudymaterials.html',{"combine":combine,"snm":snm,"ste":ste})
def studentattendanceupload(request,id):
    t=staffregistrationmodel.objects.get(id=id)
    tsem=t.staffsemeter
    b=studentregistrationmodel.objects.filter(studentsemester=tsem)
    student_attendances=[]
    if request.method =="POST":
        # date = request.POST['date']
        # rollno = request.POST['rollno']
        status = request.POST.get('status')
        rollno = request.POST.get('rollno')
        date = request.POST.get('date')
        a=attendanceuploadstudentforms(date)
        my_date_str = request.POST.get('date')
        date = datetime.strptime(my_date_str, '%Y-%m-%d').date()
        my_model_instance = attendanceuploadstudents(date=date,status=status,rollno=rollno)
        my_model_instance.save()
        return HttpResponse("success")
        # else:
        #   return HttpResponse("nooooo")
    return render(request,"attendanceupload.html",{"b":b})
def attendancedisplay(request,id):
    st=studentregistrationmodel.objects.get(id=id)
    sr=st.studentrollno
    sn=st.studentname
    at=attendanceuploadstudents.objects.filter(rollno=sr)
    return render(request,'attendancedisplay.html',{'at':at,'sn':sn})


def adminpro(request):
    return render(request,"admin.html")

def adminplogin(request):
    if request.method=="POST":
        b=admindetmodel.objects.all()
        a=admindeloginforms(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']
            ps = a.cleaned_data['password']
            for i in b:
                nm =i.username
                de =i.dep
                if us==i.username and ps==i.password:
                    return render(request,'admin.html',{'nm':nm,'de':de})
                else:
                    return HttpResponse('something went wrong')
    return render(request,"adminlogin.html")

def studenttdetailbadmin(request):
    if request.method=="POST":
        a=studentregistrationform(request.POST,request.FILES)
        if a.is_valid():
            snm=a.cleaned_data['studentname']
            sr = a.cleaned_data['studentrollno']
            si = a.cleaned_data['studentimage']
            sdp = a.cleaned_data['studentdeparment']
            sdob = a.cleaned_data['studentdob']
            sb = a.cleaned_data['studentbatch']
            ssm = a.cleaned_data['studentsemester']
            sps = a.cleaned_data['studentpassword']
            se = a.cleaned_data['studentemail']
            scl = a.cleaned_data['studentclassteacher']
            b=studentregistrationmodel(studentname=snm,studentrollno=sr,studentimage=si,
                                       studentdeparment=sdp,studentdob=sdob,studentbatch=sb,
                                       studentsemester=ssm,studentpassword=sps,studentemail=se,
                                       studentclassteacher=scl)
            b.save()
            return HttpResponse("Success")
    return render(request,'studentdetailupload.html')
def staffdetailadmin(request):
    if request.method=="POST":
        a=staffregistrationform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['staffname']
            em = a.cleaned_data['staffeid']
            sp = a.cleaned_data['staffpassword']
            cp = a.cleaned_data['staffconfirmationps']
            cb = a.cleaned_data['classteacherbatch']
            st = a.cleaned_data['staffsemeter']
            if sp==cp:
                b=staffregistrationmodel(staffname=nm,staffeid=em,
                                         staffpassword=sp,staffconfirmationps=cp,
                                         classteacherbatch=cb,staffsemeter=st)
                b.save()
                return HttpResponse('Success')


    return render(request,"staffregadmin.html")

def adminstunoti(request):
    if request.method =='POST':
        a=stusernotificationforms(request.POST)
        if a.is_valid():
            ct=a.cleaned_data['content']
            sn=a.cleaned_data['stnottime']
            b=stusernotification(content=ct,stnottime=sn)
            b.save()
            return HttpResponse('SUCCESS')
        return HttpResponse("NO")

    return render(request,'adminstudentnotification.html')

def adminttunoti(request):
        if request.method == 'POST':
            a = teachernotificationforms(request.POST)
            if a.is_valid():
                ct = a.cleaned_data['content']
                sn = a.cleaned_data['tnottime']
                b = teachernotification(content=ct, tnottime=sn)
                b.save()
                return HttpResponse('SUCCESS')
            return HttpResponse("NO")
        return render(request, 'teachernotificationadmin.html')
    # content = models.CharField(max_length=200)
    # tnottime = models.DateTimeField(auto_now_add=True)