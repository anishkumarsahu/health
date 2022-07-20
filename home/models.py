from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AdminUser(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    userType = models.CharField(max_length=200, blank=True, null=True)
    phoneNumber = models.CharField(max_length=200, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)



class ApplicantLoginDetail(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    phoneNumber = models.CharField(max_length=200, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class Applicant(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    applicantUserID = models.ForeignKey(ApplicantLoginDetail, blank=True, null=True, on_delete=models.CASCADE)
    addressOfApplicant = models.TextField(blank=True, null=True)
    phoneNumberOfApplicant = models.CharField(max_length=200, blank=True, null=True)  # Changes
    addressProofFile = models.FileField(upload_to='AddressProof', blank=True, null=True)
    professionalOrTechnicalQualification = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    addressOfOffice = models.TextField(blank=True, null=True)
    phoneNumberOfOffice = models.CharField(blank=True, null=True, max_length=200)  # changes
    nameAndOtherParticularRegisterFor = models.TextField(blank=True, null=True)  # changes
    AddressWhereNursingSituated = models.TextField(blank=True, null=True)  # changes
    typeOfApplicationCategory = models.CharField(max_length=200, blank=True, null=True)
    typeOfApplicationSubCategory = models.CharField(max_length=200, blank=True, null=True)
    anyOtherBusinessInSameResidence = models.CharField(max_length=200, blank=True, null=True)
    accommodationAvailableFloorSpace = models.TextField(blank=True, null=True)
    accommodationAvailableNumberOfBed = models.TextField(blank=True, null=True)
    accommodationAvailableToiletWash = models.TextField(blank=True, null=True)
    accommodationAvailableDrugsLinenFurniture = models.TextField(blank=True, null=True)
    accommodationAvailableForTransportation = models.TextField(blank=True, null=True)
    accommodationAvailableForKitchenStall = models.TextField(blank=True, null=True)
    noOfBedForMaternity = models.IntegerField(default=0)
    noOfBedForPatient = models.IntegerField(default=0)
    placeWhereTheNursingStaffAccommodated = models.TextField(blank=True, null=True)
    numberOfHoursInAWeekToWork = models.FloatField(default=0.0)
    arrangementForBlood = models.CharField(max_length=100, blank=True, null=True)
    arrangementForPathology = models.CharField(max_length=100, blank=True, null=True)
    arrangementForMicrobiology = models.CharField(max_length=100, blank=True, null=True)
    arrangementForRadiology = models.CharField(max_length=100, blank=True, null=True)
    feesFile = models.FileField(upload_to='Fees', blank=True, null=True)
    provisionForPoor = models.CharField(max_length=100, blank=True, null=True)
    otherBusinessOrNursingHome = models.CharField(max_length=100, blank=True, null=True)
    provisionForLifeSavingAndEmergencyDrug = models.CharField(max_length=100, blank=True, null=True)
    provisionForEmergency = models.CharField(max_length=100, blank=True, null=True)
    registrationNumber = models.CharField(max_length=100, blank=True, null=True)
    registrationYear = models.CharField(max_length=100, blank=True, null=True)
    expiryDate = models.DateField(blank=True, null=True)
    isPaymentDone = models.BooleanField(default=False)
    enrollmentNumber = models.CharField(max_length=100, blank=True, null=True)
    isDetailCompletelySubmitted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)
    isCheckedByInspector = models.BooleanField(default=False)
    isApproved = models.BooleanField(default=False)
    checkedBy = models.ForeignKey(AdminUser, blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='ByInspector')
    approvedBy = models.ForeignKey(AdminUser, blank=True, null=True, on_delete=models.CASCADE, related_name='ByRO')
    payableAmount = models.FloatField(default=0.0)
    applicationStatus = models.CharField(max_length=200,blank=True, null=True, default="Pending" )



class ApplicationTransactionDetail(models.Model):
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100, blank=True, null=True)
    transactionID = models.CharField(max_length=100, blank=True, null=True)
    transactionDate = models.CharField(max_length=100, blank=True, null=True)
    receiptFile = models.FileField(upload_to='TransactionReceipt', blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class ApplicantPersonEmployed(models.Model):
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    qualificationFile = models.FileField(upload_to='Qualification', blank=True, null=True)
    experienceFile = models.FileField(upload_to='Experience', blank=True, null=True)
    appointmentOrderFile = models.FileField(upload_to='Appointment', blank=True, null=True)
    acceptanceFile = models.FileField(upload_to='AcceptanceLetter', blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class ApplicantDoctorStaff(models.Model):
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    qualificationFile = models.FileField(upload_to='Qualification', blank=True, null=True)
    experienceFile = models.FileField(upload_to='Experience', blank=True, null=True)
    appointmentOrderFile = models.FileField(upload_to='Appointment', blank=True, null=True)
    acceptanceFile = models.FileField(upload_to='AcceptanceLetter', blank=True, null=True)
    mmcFile = models.FileField(upload_to='MMC', blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class ApplicantNurseStaff(models.Model):
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    qualificationFile = models.FileField(upload_to='Qualification', blank=True, null=True)
    experienceFile = models.FileField(upload_to='Experience', blank=True, null=True)
    appointmentOrderFile = models.FileField(upload_to='Appointment', blank=True, null=True)
    acceptanceFile = models.FileField(upload_to='AcceptanceLetter', blank=True, null=True)
    mncFile = models.FileField(upload_to='MNC', blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


# class ApplicantTransactionDetail(models.Model):
#     applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
#     datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
#     modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
#     isDeleted = models.BooleanField(default=False)


class ApplicantCheckList(models.Model):
    forwardingLetter = models.BooleanField(default=False)
    formA = models.BooleanField(default=False)
    campus = models.BooleanField(default=False)
    stafflist = models.BooleanField(default=False)
    certificates = models.BooleanField(default=False)
    ratesOrTraffic = models.BooleanField(default=False)
    rentCopy = models.BooleanField(default=False)
    appointmentOrder = models.BooleanField(default=False)
    acceptanceCertificate = models.BooleanField(default=False)
    methodOfWasteDisposal = models.BooleanField(default=False)
    mpcb = models.BooleanField(default=False)
    aerb = models.BooleanField(default=False)
    pndt = models.BooleanField(default=False)
    beds = models.BooleanField(default=False)
    epf = models.BooleanField(default=False)
    certifcateOfStaff = models.BooleanField(default=False)
    fire = models.BooleanField(default=False)
    operationTheater = models.BooleanField(default=False)
    equipments = models.BooleanField(default=False)
    emergencyMedicines = models.BooleanField(default=False)
    chemistShop = models.BooleanField(default=False)
    professionalTax = models.BooleanField(default=False)
    remarkByInspection = models.TextField(blank=True, null=True)
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    verifiedBy = models.ForeignKey(AdminUser, blank=True, null=True, on_delete=models.CASCADE,
                                   related_name='Inspection')
    approvedBy = models.ForeignKey(AdminUser, blank=True, null=True, on_delete=models.CASCADE, related_name='Ro')
    remarkByRo = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class Campus(models.Model):  # new
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    parkingSpace = models.TextField(blank=True, null=True)  # new
    buildingStructure = models.CharField(max_length=200, blank=True, null=True)  # new
    noOfFloor = models.CharField(max_length=200, blank=True, null=True)  # new
    noOfRooms = models.CharField(max_length=200, blank=True, null=True)  # new
    areaOfRooms = models.CharField(max_length=200, blank=True, null=True)  # new
    schematicDiagram = models.CharField(max_length=200, blank=True, null=True)  # new
    schematicDiagramFile = models.FileField(upload_to='schematicDiagram', blank=True, null=True)  # new
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)  # new
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)  # new
    isDeleted = models.BooleanField(default=False)  # new


class CheckListOtherDetails(models.Model):  # new
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    methodOfBioMedicalWasteFile = models.FileField(upload_to='BMW', blank=True, null=True)  # new
    MPCBFile = models.FileField(upload_to='MPCB', blank=True, null=True)  # new
    AERBFile = models.FileField(upload_to='AERB', blank=True, null=True)  # new
    PNDTFile = models.FileField(upload_to='PNDT', blank=True, null=True)  # new
    EPF = models.CharField(max_length=200, blank=True, null=True)  # new
    NonForfeitureFile = models.FileField(upload_to='NFF', blank=True, null=True)  # new
    FireSafetySystemFile = models.FileField(upload_to='FSS', blank=True, null=True)  # new
    operationTheatre = models.CharField(max_length=200, blank=True, null=True)  # new
    outlay = models.CharField(max_length=200, blank=True, null=True)  # new
    zones = models.CharField(max_length=200, blank=True, null=True)  # new
    number = models.CharField(max_length=200, blank=True, null=True)  # new
    majorMinor = models.CharField(max_length=200, blank=True, null=True)  # new
    OTEquipmentFile = models.FileField(upload_to='OTE', blank=True, null=True)  # new
    specialtiesEquipmentFile = models.FileField(upload_to='SEF', blank=True, null=True)  # new
    emergencyMedicines = models.CharField(max_length=200, blank=True, null=True)  # new
    clockChemistShop = models.CharField(max_length=200, blank=True, null=True)  # new
    professionalTaxFile = models.FileField(upload_to='PTF', null=True, blank=True)  # new
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class Status(models.Model):
    status = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class ApplicationStatus(models.Model):
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    statusID = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    applicant_remark = models.TextField(blank=True, null=True)
    admin_remark = models.TextField(blank=True, null=True)
    createdBy = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class Certificate(models.Model):
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    approvedBy = models.ForeignKey(AdminUser, blank=True, null=True, on_delete=models.CASCADE,
                                   related_name='ByROCertificate')
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    remark = models.TextField(blank=True, null=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)


class Facilities(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ApplicantFacilities(models.Model):
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    facilitiesID = models.ForeignKey(Facilities, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.applicantID.name



class ApplicationRenewalTransactionDetail(models.Model):
    applicantID = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100, blank=True, null=True)
    transactionID = models.CharField(max_length=100, blank=True, null=True)
    transactionDate = models.CharField(max_length=100, blank=True, null=True)
    receiptFile = models.FileField(upload_to='TransactionReceipt', blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    isDeleted = models.BooleanField(default=False)
