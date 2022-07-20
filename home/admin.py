from django.contrib import admin

# Register your models here.
from home.models import *


@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ("name", "phoneNumber", "email", "password", "userType", "isDeleted",)
    search_fields = ["name", "phoneNumber", "email", "password", "userType", ]


@admin.register(ApplicantLoginDetail)
class ApplicantLoginDetailAdmin(admin.ModelAdmin):
    list_display = ("email", "password", "isDeleted","datetime",)


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("applicantUserID","isDeleted","datetime",)


@admin.register(ApplicantPersonEmployed)
class ApplicantPersonEmployedAdmin(admin.ModelAdmin):
    list_display = ("applicantID","isDeleted","datetime",)


@admin.register(ApplicantDoctorStaff)
class ApplicantDoctorStaffAdmin(admin.ModelAdmin):
    list_display = ("applicantID","isDeleted","datetime",)


@admin.register(ApplicantNurseStaff)
class ApplicantNurseStaffAdmin(admin.ModelAdmin):
    list_display = ("applicantID","isDeleted","datetime",)


@admin.register(ApplicationTransactionDetail)
class ApplicantTransactionDetailAdmin(admin.ModelAdmin):
    list_display = ("applicantID",)


@admin.register(ApplicantCheckList)
class ApplicantCheckListAdmin(admin.ModelAdmin):
    list_display = ("applicantID",)


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ("applicantID",)


@admin.register(CheckListOtherDetails)
class CheckListOtherDetailsAdmin(admin.ModelAdmin):
    list_display = ("applicantID",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("applicantID",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("status",)


@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ("applicantID","statusID","applicant_remark","admin_remark","datetime",)


@admin.register(ApplicantFacilities)
class ApplicantFacilitiesAdmin(admin.ModelAdmin):
    list_display = ("applicantID","facilitiesID",)