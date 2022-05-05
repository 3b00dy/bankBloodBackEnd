from django.contrib import admin
from bloodBank.models import KarekhBanks, RassafaBanks, Volunteers

# Register your models here.

admin.site.register(RassafaBanks)
admin.site.register(KarekhBanks)
admin.site.register(Volunteers)


