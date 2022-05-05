import datetime

from ninja import Schema
from pydantic import UUID4


class MessageOut(Schema):
    detail: str


class BloodBanksOut(Schema):
    hospitalName: str
    hospitalAddress: str
    bloodType: str
    availableBottles: int
    hospitalNumber: int


class VolunteersOut(Schema):
    id: UUID4
    volunteerName: str
    volunteerAge: str
    volunteerAddress: str
    volunteerBloodType: str
    volunteerPhoneNumber: int


class VolunteersIn(Schema):
    volunteerName: str
    volunteerAge: int
    volunteerAddress: str
    volunteerBloodType: str
    volunteerPhoneNumber: int
