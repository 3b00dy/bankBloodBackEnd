from django.db import models

import uuid


class KarekhBanks(models.Model):
    id = models.UUIDField("id", default=uuid.uuid4, primary_key=True, editable=False)
    hospitalName = models.CharField("hospitalName", max_length=250, null=True)
    hospitalAddress = models.CharField("hospitalAddress", max_length=255, null=True)
    bloodType = models.CharField("bloodType", max_length=3, null=True)
    availableBottles = models.IntegerField("availableBottles", null=True)
    hospitalNumber = models.IntegerField("hospitalNumber", null=True)

    def __str__(self):
        return self.hospitalName


class RassafaBanks(models.Model):
    id = models.UUIDField("id", default=uuid.uuid4, primary_key=True, editable=False)
    hospitalName = models.CharField("hospitalName", max_length=250, null=True)
    hospitalAddress = models.CharField("hospitalAddress", max_length=255, null=True)
    bloodType = models.CharField("bloodType", max_length=3, null=True)
    availableBottles = models.IntegerField("availableBottles", null=True)
    hospitalNumber = models.IntegerField("hospitalNumber", null=True)

    def __str__(self):
        return self.hospitalName


class Volunteers(models.Model):
    id = models.UUIDField("id", default=uuid.uuid4, primary_key=True, editable=False)
    volunteerName = models.CharField("volunteerName", max_length=250, null=True)
    volunteerAge = models.IntegerField("volunteerAge",  null=True)
    volunteerAddress = models.CharField("volunteerAddress", max_length=255, null=True)
    volunteerBloodType = models.CharField("volunteerBloodType", max_length=3, null=True)
    volunteerPhoneNumber = models.IntegerField("volunteerPhoneNumber", null=True)
    def __str__(self):
        return self.volunteerName

