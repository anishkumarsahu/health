from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django_datatables_view.base_datatable_view import BaseDatatableView
from functools import wraps
from html import escape

from .models import *


# Create your views here.
# DataTablebles
# supplier
def check_group(group_name):
    def _check_group(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.groups.filter(name=group_name).exists():
                return redirect('/')
            return view_func(request, *args, **kwargs)

        return wrapper

    return _check_group


class UserListJson(BaseDatatableView):
    order_columns = ['name', 'email', 'password', 'phoneNumber', 'userType', 'action']

    def get_initial_queryset(self):
        return AdminUser.objects.filter(isDeleted__exact=False)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) | Q(password__icontains=search) | Q(email__icontains=search) | Q(
                    userType__icontains=search) | Q(
                    phoneNumber__icontains=search), isDeleted__exact=False)
        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1
        for item in qs:
            action = ''' <a class="column" data-tooltip="Will be enabled Soon" href="#" style="position: absolute;width: 0px;margin-left: -26px;margin-top: -10px;"><i class="edit outline icon"></i></a>
                         <a class="column"  data-tooltip="Will be enabled Soon" style="position: absolute;width: 0px;margin-left: -6px;margin-top: -10px;" onclick="show_Delete_Models({})"><i class="trash alternate outline icon"></i></a>'''.format(
                item.pk, item.pk)
            json_data.append([
                escape(item.name),  # escape HTML for security reasons
                escape(item.email),
                escape(item.password),
                escape(item.phoneNumber),
                escape(item.userType),
                action
            ])
            i = i + 1
        return json_data


def index(request):
    return render(request, 'home/index.html')


def adminLogin(request):
    if request.method == 'POST':

        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'RO' in request.user.groups.values_list('name', flat=True):
                return redirect('/roHome/')
            elif 'Inspection' in request.user.groups.values_list('name', flat=True):
                return redirect('/inspectionHome/')
        else:
            messages.success(request, "Wrong Credential! Please try again.")

            return render(request, "home/admin/adminLogin.html", {})
    return render(request, 'home/admin/adminLogin.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@check_group('RO')
def roHome(request):
    user_count = AdminUser.objects.filter(isDeleted__exact=False).count()

    context = {
        'user_count':user_count
    }
    return render(request, 'home/admin/roHomepage.html', context)


@check_group('RO')
def add_user(request):
    return render(request, 'home/admin/addUser.html')


@check_group('RO')
def user_name_exist(request, *args, **kwargs):
    username = request.GET.get('q')
    try:

        user = User.objects.get(username__iexact=username)
        return JsonResponse({'message': 'Email already taken. Please try some other name.', 'canUse': 'No'})
    except:
        return JsonResponse({'message': 'Email available.', 'canUse': 'Yes'})


@check_group('RO')
def add_admin_user_post(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phoneNumber')
            userType = request.POST.get('userType')
            password = request.POST.get('password')

            staff = AdminUser()
            staff.name = name
            staff.email = email
            staff.phoneNumber = phone
            staff.password = password
            staff.userType = userType
            new_user = User()
            new_user.username = email
            new_user.set_password(password)
            new_user.save()

            staff.userID_id = new_user.pk
            if userType == 'RO':
                try:
                    g = Group.objects.get(name='RO')
                    g.user_set.add(new_user.pk)
                    g.save()
                except:
                    g = Group()
                    g.name = "RO"
                    g.save()
                    g.user_set.add(new_user.pk)
                    g.save()
            elif userType == 'Inspector':
                try:
                    g = Group.objects.get(name='Inspection')
                    g.user_set.add(new_user.pk)
                    g.save()
                except:
                    g = Group()
                    g.name = "Inspection"
                    g.save()
                    g.user_set.add(new_user.pk)
                    g.save()

            staff.save()

            return redirect('/roHome/user_list/')

        except:
            messages.success(request, 'Error. Please try again.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@check_group('RO')
def user_list(request):
    return render(request, 'home/admin/userList.html')

@check_group('RO')
def pending_list(request):
    return render(request, 'home/admin/pendingList.html')


@check_group('RO')
def applicant_detail(request):
    return render(request, 'home/admin/applicantDetail.html')


def applicant_form_detail(request,id=None):
    instance = get_object_or_404(Applicant,id=id)
    applicant_person_employed = ApplicantPersonEmployed.objects.filter(applicantID_id = instance.pk)
    applicant_doctor_staff = ApplicantDoctorStaff.objects.filter(applicantID_id=instance.pk)
    applicant_nurse_staff = ApplicantNurseStaff.objects.filter(applicantID_id = instance.pk)
    context = {
        'instances': instance,
        'applicantPersonEmployer': applicant_person_employed,
        'applicantDoctorStaff': applicant_doctor_staff,
        'applicantNurseStaff': applicant_nurse_staff
    }
    return render(request, 'home/admin/applicantFormDetail.html',context)

# ------------------------------Inspection-------------------------------------------

@check_group('Inspection')
def inspectionHome(request):
    total = Applicant.objects.filter(isDeleted__exact=False, isDetailCompletelySubmitted__exact=True).count()
    total_v = Applicant.objects.filter(isDeleted__exact=False, isCheckedByInspector__exact=True, isDetailCompletelySubmitted__exact=True).count()
    total_p = Applicant.objects.filter(isDeleted__exact=False, isCheckedByInspector__exact=False, isDetailCompletelySubmitted__exact=True).count()

    context ={
        'total':total,
        'total_v':total_v,
        'total_p':total_p
    }
    return render(request, 'home/inspection/inspectionHomepage.html', context)

@check_group('Inspection')
def inspectionPendingList(request):

    return render(request, 'home/inspection/pendingList.html')


class inspectionPendingListJson(BaseDatatableView):
    order_columns = ['name','enrollmentNumber','typeOfApplicationCategory','typeOfApplicationSubCategory','datetime']

    def get_initial_queryset(self):
        return Applicant.objects.filter(isDeleted__exact=False, isDetailCompletelySubmitted__exact=True, isCheckedByInspector=False)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) | Q(enrollmentNumber__icontains=search)| Q(typeOfApplicationCategory__icontains=search)
                |Q(typeOfApplicationSubCategory__icontains=search)|Q(datetime__icontains=search), isDeleted__exact=False)
        return qs
    def prepare_results(self, qs):
        json_data = []
        i = 1
        for item in qs:
            action = ''' <a class="column" data-tooltip="View" href="/inspectionHome/applicant_from_detail/{}/" style="position: absolute;width: 0px;margin-left: -26px;margin-top: -10px;"><i class="file alternate outline icon"></i></a>
                         '''.format(item.pk)

            json_data.append([
                escape(item.name),  # escape HTML for security reasons
                escape(item.enrollmentNumber),
                escape(item.typeOfApplicationCategory),
                escape(item.typeOfApplicationSubCategory),
                escape(item.datetime.strftime('%d-%m-%Y %I:%M %p')),
                action
            ])
            i = i + 1
        return json_data


@check_group('Inspection')
def applicant_form_detail_inspection(request, id=None):
    instance = get_object_or_404(Applicant, id=id)
    applicant_person_employed = ApplicantPersonEmployed.objects.filter(applicantID_id=instance.pk)
    applicant_doctor_staff = ApplicantDoctorStaff.objects.filter(applicantID_id=instance.pk)
    applicant_nurse_staff = ApplicantNurseStaff.objects.filter(applicantID_id=instance.pk)
    context = {
        'instances': instance,
        'applicantPersonEmployer': applicant_person_employed,
        'applicantDoctorStaff': applicant_doctor_staff,
        'applicantNurseStaff': applicant_nurse_staff
    }
    return render(request, 'home/inspection/applicantFormDetailInspection.html', context)

@check_group('Inspection')
def verify_applicant_checklist_inspection(request, id=None):
    instance = get_object_or_404(Applicant, id=id)
    context = {
        'instances': instance,
    }
    return render(request, 'home/inspection/applicantDetailChecklist.html', context)



# ------------------------------ Customer ---------------------------------
@csrf_exempt
def register_applicant(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        user_exist = ApplicantLoginDetail.objects.filter(email__icontains=Email).count()
        if user_exist == 0:
            # first_dateTime = datetime.now()
            # new_dataTime = first_dateTime - timedelta(minutes=5)
            # try:
                # geteData = OtpVerification.objects.get(otp__exact=OTP, email__iexact=Email, isDeleted__exact=False,
                #                                datetime__gte=new_dataTime)
                # geteData.isDeleted = True
                # geteData.save()
                cus = ApplicantLoginDetail()
                cus.email = Email
                cus.password = Password
                cus.save()
                user = User()
                user.username = Email
                user.set_password(Password)
                user.save()
                cus.userID_id = user.id
                cus.username = user.username
                cus.save()
                app = Applicant()
                app.applicantUserID_id = cus.pk
                app.save()
                app.enrollmentNumber = str(app.pk).zfill(5)
                app.save()
                return JsonResponse({'message': 'success'})
            # except:
            #     return JsonResponse({'message': 'error'})

        else:
            return JsonResponse({'message': 'alreadyExist'})
    else:
        return JsonResponse({'message': 'fail'})

@csrf_exempt
def login_applicant(request):
    if request.method == 'POST':
        Email = request.POST.get('username')
        Password = request.POST.get('password')
        user_exist = ApplicantLoginDetail.objects.filter(email__icontains=Email, password__exact=Password).count()
        if user_exist != 0:
            # first_dateTime = datetime.now()
            # new_dataTime = first_dateTime - timedelta(minutes=5)
            try:
                # geteData = OtpVerification.objects.get(otp__exact=OTP, email__iexact=Email, isDeleted__exact=False,
                #                                datetime__gte=new_dataTime)
                # geteData.isDeleted = True
                # geteData.save()
                user = authenticate(request, username=Email, password=Password)
                if user is not None:
                    login(request, user)
                return JsonResponse({'message': 'success'})
            except:
                return JsonResponse({'message': 'fail'})

        else:
            return JsonResponse({'message': 'error'})
    else:
        return JsonResponse({'message': 'error'})


# Registration Form A
def registrationformA(request):
    applicantID = Applicant.objects.get(applicantUserID__userID_id=request.user.pk)
    context = {
        'applicantID':applicantID.pk
    }
    return render(request,'home/customer/registrationFormA.html', context)

# Applicant Dashboard
def applicantDashboard(request):
    return render(request,'home/customer/applicantDashboard.html')