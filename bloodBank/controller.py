from ninja import Router, Schema
from typing import List

from account.authorization import GlobalAuth
from bloodBank.models import KarekhBanks, RassafaBanks, Volunteers
from bloodBank.schema import BloodBanksOut, VolunteersOut, MessageOut, VolunteersIn
from django.shortcuts import get_object_or_404

bloodBank_controller = Router(tags=['Banks'])


@bloodBank_controller.get('banks/{location}/{type}', response={200: List[BloodBanksOut]})
def get_all_Banks(request, location, type):
    if location == 'Karekh':
        bloodBanks = KarekhBanks.objects.filter(bloodType__exact=type)
        return 200, bloodBanks
    elif location == 'Rassafa':
        bloodBanks = RassafaBanks.objects.filter(bloodType__exact=type)
        return 200, bloodBanks
    else:
        return 404, "not found"


@bloodBank_controller.get('banksOnType/{location}/{type}', response={200: List[BloodBanksOut]})
def get_all_Banks(request, location, type):
    if location == 'Karekh':
        if type == 'AB+':
            bloodBanks = KarekhBanks.objects.all()
            return 200, bloodBanks
        elif type == 'AB-':
            bloodBanks = KarekhBanks.objects.filter(bloodType__in=['O-', 'B-', 'AB-', 'A-'])

            return 200, bloodBanks
        elif type == 'B+':
            bloodBanks = KarekhBanks.objects.filter(bloodType__in=['O-', 'O+', 'B+', 'B-'])
            return 200, bloodBanks
        elif type == 'B-':
            bloodBanks = KarekhBanks.objects.filter(bloodType__in=['O-', 'B-'])
            return 200, bloodBanks
        elif type == 'A+':
            bloodBanks = KarekhBanks.objects.filter(bloodType__in=['O-', 'O+', 'A-', 'A+'])
            return 200, bloodBanks
        elif type == 'A-':
            bloodBanks = KarekhBanks.objects.filter(bloodType__in=['O-', 'A-'])
            return 200, bloodBanks
        elif type == 'O+':
            bloodBanks = KarekhBanks.objects.filter(bloodType__in=['O-', 'O+'])
            return 200, bloodBanks
        elif type == 'O-':
            bloodBanks = KarekhBanks.objects.filter(bloodType__exact='O-')
            return 200, bloodBanks


    elif location == 'Rassafa':
        if type == 'AB+':
            bloodBanks = RassafaBanks.objects.all()
            return 200, bloodBanks
        elif type == 'AB-':
            bloodBanks = RassafaBanks.objects.filter(bloodType__in=['O-', 'B-', 'AB-', 'A-'])
            return 200, bloodBanks
        elif type == 'B+':
            bloodBanks = RassafaBanks.objects.filter(bloodType__in=['O-', 'O+', 'B+', 'B-'])
            return 200, bloodBanks
        elif type == 'B-':
            bloodBanks = RassafaBanks.objects.filter(bloodType__in=['O-', 'B-'])
            return 200, bloodBanks
        elif type == 'A+':
            bloodBanks = RassafaBanks.objects.filter(bloodType__in=['O-', 'O+', 'A-', 'A+'])
            return 200, bloodBanks
        elif type == 'A-':
            bloodBanks = RassafaBanks.objects.filter(bloodType__in=['O-', 'A-'])
            return 200, bloodBanks
        elif type == 'O+':
            bloodBanks = RassafaBanks.objects.filter(bloodType__in=['O-', 'O+'])
            return 200, bloodBanks
        elif type == 'O-':
            bloodBanks = RassafaBanks.objects.filter(bloodType__exact='O-')
            return 200, bloodBanks

    else:
        return 404, "not found"


@bloodBank_controller.get('volunteers', response={200: List[VolunteersOut]})
def get_all_volunteers(request):
    volunteers = Volunteers.objects.all()
    return 200, volunteers


@bloodBank_controller.post(

    'volunteer', response={
        201: VolunteersOut,
        400: MessageOut,
    },auth=GlobalAuth(),
)
def add_volunteer(request, payload: VolunteersIn):
    try:
        volunteer = Volunteers.objects.create(**payload.dict())

    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, volunteer
