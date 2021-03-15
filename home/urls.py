from django.urls import path

from .views import *
from .apiView import *
#
# app_name = 'polls'
urlpatterns = [

    path('', index, name='index'),
    path('registrationformA/',registrationformA,name='registrationformA'),
    path('ApplicantBasicApiView/', ApplicantBasicApiView, name='ApplicantBasicApiView'),
    path('ApplicantPersonEmployeeApiView/', ApplicantPersonEmployeeApiView, name='ApplicantPersonEmployeeApiView'),
    path('DeleteApplicantPersonEmployeeApiView/', DeleteApplicantPersonEmployeeApiView, name='DeleteApplicantPersonEmployeeApiView'),
    path('ApplicantDoctorStaffApiView/', ApplicantDoctorStaffApiView, name='ApplicantDoctorStaffApiView'),
    path('DeleteApplicantDoctorApiView/', DeleteApplicantDoctorApiView, name='DeleteApplicantDoctorApiView'),
    path('ApplicantNurseStaffApiView/', ApplicantNurseStaffApiView, name='ApplicantNurseStaffApiView'),
    path('DeleteApplicantNurseApiView/', DeleteApplicantNurseApiView, name='DeleteApplicantNurseApiView'),
    path('RequestForApplicantApprovalApiView/', RequestForApplicantApprovalApiView, name='RequestForApplicantApprovalApiView'),

    path('applicantDashboard/',applicantDashboard,name='applicantDashboard'),
    path('register_applicant/',register_applicant,name='register_applicant'),
    path('login_applicant/',login_applicant,name='login_applicant'),
    # login
    path('adminLogin/', adminLogin, name='adminLogin'),
    #Logout
    path('logout_user/', logout_user, name='logout_user'),
# --------------------------------RO------------------------------------------------------------
    path('roHome/', roHome, name='roHome'),
    #user
    path('roHome/add_user/', add_user, name='add_user'),
    path('roHome/user_name_exist/', user_name_exist, name='user_name_exist'),
    path('roHome/add_admin_user_post/', add_admin_user_post, name='add_admin_user_post'),
    path('roHome/user_list/', user_list, name='user_list'),
    path('UserListJson/', UserListJson.as_view(), name='UserListJson'),
    path('roHome/pending_list/', pending_list, name='pending_list'),
    path('roHome/approval_list/', approval_list, name='approval_list'),
    path('roHome/RoPendingListJson/', RoPendingListJson.as_view(), name='RoPendingListJson'),
    path('roHome/RoApprovalListJson/', RoApprovalListJson.as_view(), name='RoApprovalListJson'),
    path('roHome/applicant_from_detail_ro/<int:id>/', applicant_form_detail_ro,
         name='applicant_form_detail_Ro'),

    path('roHome/applicant_detail/', applicant_detail, name='applicant_detail'),
    path('roHome/applicant_from_detail/<int:id>/', applicant_form_detail, name='applicant_form_detail'),
    path('roHome/after_verify_applicant_checklist_ro/<int:id>/',
         after_verify_applicant_checklist_ro, name='after_verify_applicant_checklist_ro'),
    path('roHome/approve_and_issue_certificate_to_applicant/',
         approve_and_issue_certificate_to_applicant, name='approve_and_issue_certificate_to_applicant'),

    # ---------------------------------Inspection---------------------------------------------------
    path('inspectionHome/', inspectionHome, name='inspectionHome'),
    path('inspectionPendingList/', inspectionPendingList, name='inspectionPendingList'),
    path('inspectionHome/inspectionPendingListJson/', inspectionPendingListJson.as_view(), name='inspectionPendingListJson'),
    path('inspectionHome/applicant_from_detail/<int:id>/', applicant_form_detail_inspection, name='applicant_form_detail_inspection'),
    path('inspectionHome/verify_applicant_checklist_inspection/<int:id>/', verify_applicant_checklist_inspection, name='verify_applicant_checklist_inspection'),
    path('inspectionHome/after_verify_applicant_checklist_inspection/<int:id>/', after_verify_applicant_checklist_inspection, name='after_verify_applicant_checklist_inspection'),

    path('inspectionHome/submit_checklist_applicant/', submit_checklist_applicant, name='submit_checklist_applicant'),

    path('inspectionHome/inspectionApprovedList/', inspectionApprovedList, name='inspectionApprovedList'),
    path('inspectionHome/inspectionApproveListJson/', inspectionApproveListJson.as_view(), name='inspectionApproveListJson'),


# UPDATE
    path('CheckListOtherDetailsApiView/', CheckListOtherDetailsApiView, name='CheckListOtherDetailsApiView'),
    path('CampusDetailsApiView/', CampusDetailsApiView, name='CampusDetailsApiView'),
# END UPDATE
# 15-03-2021 UPDATE
    path('applicantProfile/',applicantProfile,name='applicantProfile'),
    path('applicantChangesPasswordApiView/',applicantChangesPasswordApiView,name='applicantChangesPasswordApiView'),
]