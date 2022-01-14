from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for  related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    hospital = forms.ModelChoiceField(queryset=models.Hospital.objects.all().filter(status='Approved'),empty_label="Hospital Name", to_field_name="user_id")
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']



class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    hospital = forms.ModelChoiceField(queryset=models.Hospital.objects.all().filter(status='Approved'),empty_label="Hospital Name", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic']



class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name", to_field_name="user_id")
    patient = forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name", to_field_name="user_id")
    
    class Meta:
        model=models.Appointment
        fields=['description']




#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



class HospitalUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class HospitalForm(forms.ModelForm):
    
    class Meta:
        model=models.Hospital
        fields=['address','mobile']


class ChangeHospitalForm(forms.ModelForm):
    hospital = forms.ModelChoiceField(queryset=models.Hospital.objects.all().filter(status='Approved'),empty_label="Hospital Name", to_field_name="user_id")
    patient = forms.ModelChoiceField(queryset=models.Patient.objects.all(),empty_label="Patient Name", to_field_name="user_id")
    class Meta:
        model=models.ChangeHospital
        fields=['patient']


class MinistryUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class MinistryForm(forms.ModelForm):
    class Meta:
        model=models.Ministry
        fields=['address','mobile']

       

class ReceptionistUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class ReceptionistForm(forms.ModelForm):
    hospital = forms.ModelChoiceField(queryset=models.Hospital.objects.all().filter(status='Approved'),empty_label="Hospital Name", to_field_name="user_id")
    class Meta:
        model=models.Receptionist
        fields=['address','mobile','status']
