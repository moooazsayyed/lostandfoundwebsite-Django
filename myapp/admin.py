from django.contrib import admin
from .models import Listing, Listing_mobile,Listing_people,Listing_pets
from .models import Contactus

admin.site.register (Listing)
admin.site.register (Listing_mobile)
admin.site.register (Listing_people)
admin.site.register (Listing_pets)
admin.site.register (Contactus)
