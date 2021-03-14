from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from .models import *
from home.models import *


@csrf_exempt
def ApplicantBasicApiView(request):
    if request.method == 'POST':
        try:
            fullNameApplicant = request.POST.get('fullNameApplicant')
            addressApplicant = request.POST.get('addressApplicant')
            phoneNumberApplicant = request.POST.get('phoneNumberApplicant')
            addressProofFile = request.FILES['addressProofFile']
            appicantQualificationTextField = request.POST.get('appicantQualificationTextField')
            applicantNationality = request.POST.get('applicantNationality')
            addressOfOffice = request.POST.get('addressOfOffice')
            phoneNoOfOffice = request.POST.get('phoneNoOfOffice')
            nameAndOtherParticularRegisterFor = request.POST.get('nameAndOtherParticularRegisterFor')
            AddressWhereNursingSituated = request.POST.get('AddressWhereNursingSituated')
            typeOfApplicationCategory = request.POST.get('typeOfApplicationCategory')
            typeOfApplicationSubCategory = request.POST.get('typeOfApplicationSubCategory')
            anyOtherBusinessInSameResidence = request.POST.get('anyOtherBusinessInSameResidence')
            accommodationAvailableFloorSpace = request.POST.get('accommodationAvailableFloorSpace')
            accommodationAvailableNumberOfBed = request.POST.get('accommodationAvailableNumberOfBed')
            accommodationAvailableToiletWash = request.POST.get('accommodationAvailableToiletWash')
            accommodationAvailableDrugsLinenFurniture = request.POST.get('accommodationAvailableDrugsLinenFurniture')
            accommodationAvailableForTransportation = request.POST.get('accommodationAvailableForTransportation')
            accommodationAvailableForKitchenStall = request.POST.get('accommodationAvailableForKitchenStall')
            noOfBedForMaternity = request.POST.get('noOfBedForMaternity')
            noOfBedForPatient = request.POST.get('noOfBedForPatient')
            placeWhereTheNursingStaffAccommodated = request.POST.get('placeWhereTheNursingStaffAccommodated')
            numberOfHoursInAWeekToWork = request.POST.get('numberOfHoursInAWeekToWork')
            arrangementForBlood = request.POST.get('arrangementForBlood')
            arrangementForPathology = request.POST.get('arrangementForPathology')
            arrangementForMicrobiology = request.POST.get('arrangementForMicrobiology')
            arrangementForRadiology = request.POST.get('arrangementForRadiology')
            feesFile = request.FILES['feesFile']
            provisionForPoor = request.POST.get('provisionForPoor')
            otherBusinessOrNursingHome = request.POST.get('otherBusinessOrNursingHome')
            provisionForLifeSavingAndEmergencyDrug = request.POST.get('provisionForLifeSavingAndEmergencyDrug')
            provisionForEmergency = request.POST.get('provisionForEmergency')
            registrationNumber = request.POST.get('registrationNumber')
            registrationYear = request.POST.get('registrationYear')


            ApplicantDB = Applicant.objects.get(applicantUserID__userID_id=request.user.pk)
            ApplicantDB.name = fullNameApplicant
            ApplicantDB.addressOfApplicant = addressApplicant
            ApplicantDB.phoneNumberOfApplicant = phoneNumberApplicant
            ApplicantDB.addressProofFile = addressProofFile
            ApplicantDB.professionalOrTechnicalQualification = appicantQualificationTextField
            ApplicantDB.nationality = applicantNationality
            ApplicantDB.addressOfOffice = addressOfOffice
            ApplicantDB.phoneNumberOfOffice = phoneNoOfOffice
            ApplicantDB.nameAndOtherParticularRegisterFor = nameAndOtherParticularRegisterFor
            ApplicantDB.AddressWhereNursingSituated = AddressWhereNursingSituated
            ApplicantDB.typeOfApplicationCategory = typeOfApplicationCategory
            ApplicantDB.typeOfApplicationSubCategory = typeOfApplicationSubCategory
            ApplicantDB.anyOtherBusinessInSameResidence = anyOtherBusinessInSameResidence
            ApplicantDB.accommodationAvailableFloorSpace = accommodationAvailableFloorSpace
            ApplicantDB.accommodationAvailableNumberOfBed = accommodationAvailableNumberOfBed
            ApplicantDB.accommodationAvailableToiletWash = accommodationAvailableToiletWash
            ApplicantDB.accommodationAvailableDrugsLinenFurniture = accommodationAvailableDrugsLinenFurniture
            ApplicantDB.accommodationAvailableForTransportation = accommodationAvailableForTransportation
            ApplicantDB.accommodationAvailableForKitchenStall = accommodationAvailableForKitchenStall
            ApplicantDB.noOfBedForMaternity = noOfBedForMaternity
            ApplicantDB.noOfBedForPatient = noOfBedForPatient
            ApplicantDB.placeWhereTheNursingStaffAccommodated = placeWhereTheNursingStaffAccommodated
            ApplicantDB.numberOfHoursInAWeekToWork = numberOfHoursInAWeekToWork
            ApplicantDB.arrangementForBlood = arrangementForBlood
            ApplicantDB.arrangementForPathology = arrangementForPathology
            ApplicantDB.arrangementForMicrobiology = arrangementForMicrobiology
            ApplicantDB.arrangementForRadiology = arrangementForRadiology
            ApplicantDB.feesFile = feesFile
            ApplicantDB.provisionForPoor = provisionForPoor
            ApplicantDB.otherBusinessOrNursingHome = otherBusinessOrNursingHome
            ApplicantDB.provisionForLifeSavingAndEmergencyDrug = provisionForLifeSavingAndEmergencyDrug
            ApplicantDB.provisionForEmergency = provisionForEmergency
            ApplicantDB.registrationNumber = registrationNumber
            ApplicantDB.registrationYear = registrationYear
            ApplicantDB.save()
            return JsonResponse({'message': 'success'}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)



@csrf_exempt
def ApplicantPersonEmployeeApiView(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            age = request.POST.get('age')
            qualification = request.POST.get('qualification')
            experience = request.POST.get('experience')
            appointmentCert = request.FILES['appointmentCert']
            qualificationCert = request.FILES['qualificationCert']
            experienceCert = request.FILES['experienceCert']
            acceptanceCert = request.FILES['acceptanceCert']

            ApplicantDB = Applicant.objects.get(applicantUserID__userID_id=request.user.pk)
            ap = ApplicantPersonEmployed()
            ap.applicantID_id = ApplicantDB.pk
            ap.name = name
            ap.age = age
            ap.qualification = qualification
            ap.experience = experience
            ap.appointmentOrderFile = appointmentCert
            ap.qualificationFile = qualificationCert
            ap.experienceFile = experienceCert
            ap.acceptanceFile = acceptanceCert
            ap.save()


            ApplicantDB.save()
            return JsonResponse({'message': 'success','id':ap.pk}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)


@csrf_exempt
def DeleteApplicantPersonEmployeeApiView(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            ap = ApplicantPersonEmployed.objects.get(applicantID__applicantUserID__userID_id=request.user.pk, pk = int(id))
            ap.delete()
            return JsonResponse({'message': 'success'}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)


@csrf_exempt
def DeleteApplicantDoctorApiView(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            ap = ApplicantDoctorStaff.objects.get(applicantID__applicantUserID__userID_id=request.user.pk, pk = int(id))
            ap.delete()
            return JsonResponse({'message': 'success'}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)

@csrf_exempt
def DeleteApplicantNurseApiView(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            ap = ApplicantNurseStaff.objects.get(applicantID__applicantUserID__userID_id=request.user.pk, pk = int(id))
            ap.delete()
            return JsonResponse({'message': 'success'}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)


@csrf_exempt
def ApplicantDoctorStaffApiView(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            age = request.POST.get('age')
            qualification = request.POST.get('qualification')
            experience = request.POST.get('experience')
            appointmentCert = request.FILES['appointmentCert']
            qualificationCert = request.FILES['qualificationCert']
            experienceCert = request.FILES['experienceCert']
            acceptanceCert = request.FILES['acceptanceCert']
            mmcCert = request.FILES['mmcCert']

            ApplicantDB = Applicant.objects.get(applicantUserID__userID_id=request.user.pk)
            ap = ApplicantDoctorStaff()
            ap.applicantID_id = ApplicantDB.pk
            ap.name = name
            ap.age = age
            ap.qualification = qualification
            ap.experience = experience
            ap.appointmentOrderFile = appointmentCert
            ap.qualificationFile = qualificationCert
            ap.experienceFile = experienceCert
            ap.acceptanceFile = acceptanceCert
            ap.mmcFile = mmcCert
            ap.save()


            ApplicantDB.save()
            return JsonResponse({'message': 'success','id':ap.pk}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)

@csrf_exempt
def ApplicantNurseStaffApiView(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            age = request.POST.get('age')
            qualification = request.POST.get('qualification')
            experience = request.POST.get('experience')
            appointmentCert = request.FILES['appointmentCert']
            qualificationCert = request.FILES['qualificationCert']
            experienceCert = request.FILES['experienceCert']
            acceptanceCert = request.FILES['acceptanceCert']
            mmcCert = request.FILES['mmcCert']

            ApplicantDB = Applicant.objects.get(applicantUserID__userID_id=request.user.pk)
            ap = ApplicantNurseStaff()
            ap.applicantID_id = ApplicantDB.pk
            ap.name = name
            ap.age = age
            ap.qualification = qualification
            ap.experience = experience
            ap.appointmentOrderFile = appointmentCert
            ap.qualificationFile = qualificationCert
            ap.experienceFile = experienceCert
            ap.acceptanceFile = acceptanceCert
            ap.mncFile = mmcCert
            ap.save()


            ApplicantDB.save()
            return JsonResponse({'message': 'success','id':ap.pk}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)



    # Update
@csrf_exempt
def CheckListOtherDetailsApiView(request):
    if request.method == 'POST':
        try:
            methodOfBioMedicalWasteFile = request.FILES['methodOfBioMedicalWasteFile']
            MPCBFile = request.FILES['MPCBFile']
            AERBFile = request.FILES['AERBFile']
            PNDTFile = request.FILES['PNDTFile']
            EPF = request.POST.get('EPF')
            NonForfeitureFile = request.FILES['NonForfeitureFile']
            FireSafetySystemFile = request.FILES['FireSafetySystemFile']
            operationTheatre = request.POST.get('operationTheatre')
            outlay = request.POST.get('outlay')
            zones = request.POST.get('zones')
            number = request.POST.get('number')
            majorMinor = request.POST.get('majorMinor')
            OTEquipmentFile = request.FILES['OTEquipmentFile']
            specialtiesEquipmentFile = request.FILES['specialtiesEquipmentFile']
            emergencyMedicines = request.POST.get('emergencyMedicines')
            clockChemistShop = request.POST.get('clockChemistShop')
            professionalTaxFile = request.FILES['professionalTaxFile']
            ApplicantDB = Applicant.objects.get(applicantUserID__userID_id=request.user.pk)
            CheckListOtherDetailsDB = CheckListOtherDetails()
            CheckListOtherDetailsDB.applicantID_id = ApplicantDB.pk
            CheckListOtherDetailsDB.methodOfBioMedicalWasteFile = methodOfBioMedicalWasteFile
            CheckListOtherDetailsDB.MPCBFile = MPCBFile
            CheckListOtherDetailsDB.AERBFile = AERBFile
            CheckListOtherDetailsDB.PNDTFile = PNDTFile
            CheckListOtherDetailsDB.EPF = EPF
            CheckListOtherDetailsDB.NonForfeitureFile = NonForfeitureFile
            CheckListOtherDetailsDB.FireSafetySystemFile = FireSafetySystemFile
            CheckListOtherDetailsDB.operationTheatre = operationTheatre
            CheckListOtherDetailsDB.outlay = outlay
            CheckListOtherDetailsDB.zones = zones
            CheckListOtherDetailsDB.number = number
            CheckListOtherDetailsDB.majorMinor = majorMinor
            CheckListOtherDetailsDB.OTEquipmentFile = OTEquipmentFile
            CheckListOtherDetailsDB.specialtiesEquipmentFile = specialtiesEquipmentFile
            CheckListOtherDetailsDB.emergencyMedicines = emergencyMedicines
            CheckListOtherDetailsDB.clockChemistShop = clockChemistShop
            CheckListOtherDetailsDB.professionalTaxFile = professionalTaxFile
            CheckListOtherDetailsDB.save()
            return JsonResponse({'message': 'success'}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)

@csrf_exempt
def CampusDetailsApiView(request):
    if request.method == 'POST':
        try:
            parkingSpace = request.POST.get('parkingSpace')
            buildingStructure = request.POST.get('buildingStructure')
            noOfFloor = request.POST.get('noOfFloor')
            schematicDiagram = request.POST.get('schematicDiagram')
            schematicDiagramFile = request.FILES['schematicDiagramFile']
            noOfRooms = request.POST.get('noOfRooms')
            areaOfRooms = request.POST.get('areaOfRooms')
            ApplicantDB = Applicant.objects.get(applicantUserID__userID_id=request.user.pk)
            CampusDetailsDB = Campus()
            CampusDetailsDB.applicantID_id = ApplicantDB.pk
            CampusDetailsDB.parkingSpace = parkingSpace
            CampusDetailsDB.buildingStructure = buildingStructure
            CampusDetailsDB.noOfFloor = noOfFloor
            CampusDetailsDB.schematicDiagram = schematicDiagram
            CampusDetailsDB.schematicDiagramFile = schematicDiagramFile
            CampusDetailsDB.noOfRooms = noOfRooms
            CampusDetailsDB.areaOfRooms = areaOfRooms
            CampusDetailsDB.save()
            return JsonResponse({'message': 'success'}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)

@csrf_exempt
def RequestForApplicantApprovalApiView(request):
    if request.method == 'POST':
        try:
            ap = Applicant.objects.get(applicantUserID__userID_id=request.user.pk)
            ap.isDetailCompletelySubmitted = True
            ap.save()
            return JsonResponse({'message': 'success'}, safe=False)
        except:
            return JsonResponse({'message': 'error'}, safe=False)

