from django import forms
from django.forms import ModelForm
from .models import Customer,ServiceStation,Service, Fueltype ,Supplier, Fueltype ,Fuel , Machine , Tanker , admincustomer
from django.contrib.auth import get_user_model

#for User model
User = get_user_model

#CustomerRegistration form
class CustomerRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

#CustomerInfo form
class CustomerInfoForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    cust_phone = forms.CharField(widget=forms.TextInput(),label='PhoneNumber')
    address = forms.CharField(widget=forms.Textarea(),label='Address')

#ServiceStationRegistration form
class ServiceStationRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

#ServiceStationInfo form
class ServiceStationInfoForm(forms.Form):
    station_name = forms.CharField(widget=forms.TextInput(), label='ServiceCenter Name')
    email = forms.CharField(widget=forms.TextInput())
    ss_phone = forms.CharField(widget=forms.TextInput(),label='PhoneNumber')
    address = forms.CharField(widget=forms.Textarea(),label='Address')

# CustomerLogin form
class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

#ServiceStationLogin form
class ServiceStationLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

#Booking form
class VBooking(forms.Form):
    choice = (('Car','Car'),('Bike','Bike'),('Scooter','Scooter'))
    schoice = (('Wash','Wash'),('Denting','Denting'),('Full Service','Full Service'))
    vehicle_reg_no = forms.CharField(widget=forms.TextInput())
    vehicle_name = forms.CharField(widget=forms.TextInput())
    vehicle_type = forms.CharField(widget=forms.TextInput())
    type_of_service = forms.CharField(widget=forms.TextInput())
    service_desc = forms.CharField(widget=forms.TextInput())



#supplierform

class SupplierForm(forms.ModelForm): 
    class Meta: 
        model = Supplier
        fields = ['name', 'email', 'phone']


class FueltypeForm(forms.ModelForm): 
    class Meta: 
        model = Fueltype
        fields = ['fueltype']

class FuelForm(forms.ModelForm): 
    class Meta: 
        model = Fuel
        fields = ['fueltype','price']    

class MachineForm(forms.ModelForm): 
    class Meta: 
        model = Machine
        fields = ['fueltype', 'machine_no', 'company_name','machine_des']


class TankerForm(forms.ModelForm): 
    class Meta: 
        model = Tanker
        fields = ['supplier', 'fueltype', 'tanker_no','tanker_date','quantity','tanker_des']
      


 #Booking form
class FuelBooking(forms.Form):
    choice = (('Car','Car'),('Bike','Bike'),('Scooter','Scooter'))
    schoice = (('Wash','Wash'),('Denting','Denting'),('Full Service','Full Service'))
    vehicle_reg_no = forms.CharField(widget=forms.TextInput())
    vehicle_name = forms.CharField(widget=forms.TextInput())
    vehicle_type = forms.CharField(widget=forms.TextInput())
    type_of_fuel = forms.CharField(widget=forms.TextInput())
    fuel_qua = forms.CharField()

#contactus
#
#     
class AdmincustomerForm(forms.ModelForm):
    class Meta:
        model = admincustomer
        fields = ['customer','supplier','tanker','fueltype','fuelquantity','remarks']