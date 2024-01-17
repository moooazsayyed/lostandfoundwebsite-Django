from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/listings/images', default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cmss.gov.in%2Fgoverning-body%2F&psig=AOvVaw2Ghh0fc_OSZbjB5p8PvfSJ&ust=1696328331081000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLi-v8-R14EDFQAAAAAdAAAAABAJ')
    description = models.CharField(max_length=500)
    categorie = models.CharField(
        max_length=50,
        choices=[
            ('mobile', 'Mobile'),
            ('people', 'People'),
            ('pets', 'Pets'),
        ]
    )
    state = models.CharField(
        max_length=50,
        choices=[
            ('andhra_pradesh', 'Andhra Pradesh'),
            ('arunachal_pradesh', 'Arunachal Pradesh'),
            ('assam', 'Assam'),
            ('bihar', 'Bihar'),
            ('chhattisgarh', 'Chhattisgarh'),
            ('goa', 'Goa'),
            ('gujarat', 'Gujarat'),
            ('haryana', 'Haryana'),
            ('himachal_pradesh', 'Himachal Pradesh'),
            ('jammu_kashmir', 'Jammu and Kashmir'),
            ('jharkhand', 'Jharkhand'),
            ('karnataka', 'Karnataka'),
            ('kerala', 'Kerala'),
            ('madhya_pradesh', 'Madhya Pradesh'),
            ('maharashtra', 'Maharashtra'),
            ('manipur', 'Manipur'),
            ('meghalaya', 'Meghalaya'),
            ('mizoram', 'Mizoram'),
            ('nagaland', 'Nagaland'),
            ('odisha', 'Odisha'),
            ('punjab', 'Punjab'),
            ('rajasthan', 'Rajasthan'),
            ('sikkim', 'Sikkim'),
            ('tamil_nadu', 'Tamil Nadu'),
            ('telangana', 'Telangana'),
            ('tripura', 'Tripura'),
            ('uttar_pradesh', 'Uttar Pradesh'),
            ('uttarakhand', 'Uttarakhand'),
            ('west_bengal', 'West Bengal'),
            ('andaman_nicobar', 'Andaman and Nicobar Islands'),
            ('chandigarh', 'Chandigarh'),
            ('dadra_nagar_haveli', 'Dadra and Nagar Haveli'),
            ('daman_diu', 'Daman and Diu'),
            ('delhi', 'Delhi'),
            ('lakshadweep', 'Lakshadweep'),
            ('puducherry', 'Puducherry'),
        ]
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, help_text="Enter phone number in format: +1234567890")



class Listing_mobile(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/listings/images', default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cmss.gov.in%2Fgoverning-body%2F&psig=AOvVaw2Ghh0fc_OSZbjB5p8PvfSJ&ust=1696328331081000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLi-v8-R14EDFQAAAAAdAAAAABAJ')
    description = models.CharField(max_length=500)
    categorie = models.CharField(
        max_length=50,
        choices=[
            ('mobile', 'Mobile'),
            ('people', 'People'),
            ('pets', 'Pets'),
        ]
    )
    state = models.CharField(
        max_length=50,
        choices=[
            ('andhra_pradesh', 'Andhra Pradesh'),
            ('arunachal_pradesh', 'Arunachal Pradesh'),
            ('assam', 'Assam'),
            ('bihar', 'Bihar'),
            ('chhattisgarh', 'Chhattisgarh'),
            ('goa', 'Goa'),
            ('gujarat', 'Gujarat'),
            ('haryana', 'Haryana'),
            ('himachal_pradesh', 'Himachal Pradesh'),
            ('jammu_kashmir', 'Jammu and Kashmir'),
            ('jharkhand', 'Jharkhand'),
            ('karnataka', 'Karnataka'),
            ('kerala', 'Kerala'),
            ('madhya_pradesh', 'Madhya Pradesh'),
            ('maharashtra', 'Maharashtra'),
            ('manipur', 'Manipur'),
            ('meghalaya', 'Meghalaya'),
            ('mizoram', 'Mizoram'),
            ('nagaland', 'Nagaland'),
            ('odisha', 'Odisha'),
            ('punjab', 'Punjab'),
            ('rajasthan', 'Rajasthan'),
            ('sikkim', 'Sikkim'),
            ('tamil_nadu', 'Tamil Nadu'),
            ('telangana', 'Telangana'),
            ('tripura', 'Tripura'),
            ('uttar_pradesh', 'Uttar Pradesh'),
            ('uttarakhand', 'Uttarakhand'),
            ('west_bengal', 'West Bengal'),
            ('andaman_nicobar', 'Andaman and Nicobar Islands'),
            ('chandigarh', 'Chandigarh'),
            ('dadra_nagar_haveli', 'Dadra and Nagar Haveli'),
            ('daman_diu', 'Daman and Diu'),
            ('delhi', 'Delhi'),
            ('lakshadweep', 'Lakshadweep'),
            ('puducherry', 'Puducherry'),
        ]
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, help_text="Enter phone number in format: +1234567890")

class Listing_people(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/listings/images', default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cmss.gov.in%2Fgoverning-body%2F&psig=AOvVaw2Ghh0fc_OSZbjB5p8PvfSJ&ust=1696328331081000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLi-v8-R14EDFQAAAAAdAAAAABAJ')
    description = models.CharField(max_length=500)
    categorie = models.CharField(
        max_length=50,
        choices=[
            ('mobile', 'Mobile'),
            ('people', 'People'),
            ('pets', 'Pets'),
        ]
    )
    state = models.CharField(
        max_length=50,
        choices=[
            ('andhra_pradesh', 'Andhra Pradesh'),
            ('arunachal_pradesh', 'Arunachal Pradesh'),
            ('assam', 'Assam'),
            ('bihar', 'Bihar'),
            ('chhattisgarh', 'Chhattisgarh'),
            ('goa', 'Goa'),
            ('gujarat', 'Gujarat'),
            ('haryana', 'Haryana'),
            ('himachal_pradesh', 'Himachal Pradesh'),
            ('jammu_kashmir', 'Jammu and Kashmir'),
            ('jharkhand', 'Jharkhand'),
            ('karnataka', 'Karnataka'),
            ('kerala', 'Kerala'),
            ('madhya_pradesh', 'Madhya Pradesh'),
            ('maharashtra', 'Maharashtra'),
            ('manipur', 'Manipur'),
            ('meghalaya', 'Meghalaya'),
            ('mizoram', 'Mizoram'),
            ('nagaland', 'Nagaland'),
            ('odisha', 'Odisha'),
            ('punjab', 'Punjab'),
            ('rajasthan', 'Rajasthan'),
            ('sikkim', 'Sikkim'),
            ('tamil_nadu', 'Tamil Nadu'),
            ('telangana', 'Telangana'),
            ('tripura', 'Tripura'),
            ('uttar_pradesh', 'Uttar Pradesh'),
            ('uttarakhand', 'Uttarakhand'),
            ('west_bengal', 'West Bengal'),
            ('andaman_nicobar', 'Andaman and Nicobar Islands'),
            ('chandigarh', 'Chandigarh'),
            ('dadra_nagar_haveli', 'Dadra and Nagar Haveli'),
            ('daman_diu', 'Daman and Diu'),
            ('delhi', 'Delhi'),
            ('lakshadweep', 'Lakshadweep'),
            ('puducherry', 'Puducherry'),
        ]
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, help_text="Enter phone number in format: +1234567890")

class Listing_pets(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/listings/images', default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cmss.gov.in%2Fgoverning-body%2F&psig=AOvVaw2Ghh0fc_OSZbjB5p8PvfSJ&ust=1696328331081000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLi-v8-R14EDFQAAAAAdAAAAABAJ')
    description = models.CharField(max_length=500)
    categorie = models.CharField(
        max_length=50,
        choices=[
            ('mobile', 'Mobile'),
            ('people', 'People'),
            ('pets', 'Pets'),
        ]
    )
    state = models.CharField(
        max_length=50,
        choices=[
            ('andhra_pradesh', 'Andhra Pradesh'),
            ('arunachal_pradesh', 'Arunachal Pradesh'),
            ('assam', 'Assam'),
            ('bihar', 'Bihar'),
            ('chhattisgarh', 'Chhattisgarh'),
            ('goa', 'Goa'),
            ('gujarat', 'Gujarat'),
            ('haryana', 'Haryana'),
            ('himachal_pradesh', 'Himachal Pradesh'),
            ('jammu_kashmir', 'Jammu and Kashmir'),
            ('jharkhand', 'Jharkhand'),
            ('karnataka', 'Karnataka'),
            ('kerala', 'Kerala'),
            ('madhya_pradesh', 'Madhya Pradesh'),
            ('maharashtra', 'Maharashtra'),
            ('manipur', 'Manipur'),
            ('meghalaya', 'Meghalaya'),
            ('mizoram', 'Mizoram'),
            ('nagaland', 'Nagaland'),
            ('odisha', 'Odisha'),
            ('punjab', 'Punjab'),
            ('rajasthan', 'Rajasthan'),
            ('sikkim', 'Sikkim'),
            ('tamil_nadu', 'Tamil Nadu'),
            ('telangana', 'Telangana'),
            ('tripura', 'Tripura'),
            ('uttar_pradesh', 'Uttar Pradesh'),
            ('uttarakhand', 'Uttarakhand'),
            ('west_bengal', 'West Bengal'),
            ('andaman_nicobar', 'Andaman and Nicobar Islands'),
            ('chandigarh', 'Chandigarh'),
            ('dadra_nagar_haveli', 'Dadra and Nagar Haveli'),
            ('daman_diu', 'Daman and Diu'),
            ('delhi', 'Delhi'),
            ('lakshadweep', 'Lakshadweep'),
            ('puducherry', 'Puducherry'),
        ]
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, help_text="Enter phone number in format: +1234567890")

class Contactus(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, help_text="Enter phone number in format: +1234567890")
    email = models.EmailField()
    messeage = models.CharField(max_length=500)