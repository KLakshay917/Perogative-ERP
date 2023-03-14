from django import forms
from .models import *
from crispy_forms import helper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)


class EnquiryForm(forms.ModelForm):
    dob = forms.DateField(label="Date Of Birth" ,localize=True,widget=forms.DateInput(attrs={'type': 'date','style':'color:grey; font-size:13.5px'}),)
    class Meta:
        model = StudentEnquiry
        fields ="__all__"
        labels={
            'FatherHusband_name':"Father's/Husband's Name",
            'mother_name':"Mother's Name",
            'dob':'Date Of Birth',
            'address':'Permanent Address',
            'ParentHusband_occupation':"Parent's/Husband's Occupation",
            'institute_knowing':'How do you get to know about PG Institute',
        }

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your name',
            'FatherHusband_name': "Enter Father's/Husband's name",
            'mother_name': "Enter Mother's name",
            'dob': 'DD/MM/YYYY',
            'gender': 'Gender',
            'email' :'Email',
            'address': 'Permanent Address',
            'mobile_number': 'Enter mobile number',
            'guardian_phone_number': 'Enter Guardian phone number',
            'ParentHusband_occupation': "Enter Parent's/Husband's occupation",
            'academic_qualification': 'Select academic qualification',
            'professional_qualification': 'Enter professional qualification',
            'institute_knowing': 'Select how you heard about the institute',
        }
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': placeholders.get(field, ''),
            })

#Adding Teacher
class AddTeacher(forms.ModelForm):
    dob = forms.DateField(label="Date Of Birth" ,localize=True,widget=forms.DateInput(format = '%d-%m-%Y',attrs={'type': 'date','format':format}),)
    course = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple())
    # staff_type = forms.ChoiceField(choices=choice)


    class Meta:        
        model = Teacher
        fields ="__all__"
        exclude=("teacher",)
        labels={
            'address':'Permanent Address',
        }
        
        

    def __init__(self, *args, **kwargs):
        super(AddTeacher, self).__init__(*args, **kwargs)
                 
        placeholders = {
            'name': 'Enter your name',
            'dob': 'DD/MM/YYYY',
            'gender': 'Gender',
            'email' :'Email',
            'address': 'Permanent Address',
            'academic_qualification': 'Select academic qualification',
            'professional_qualification': 'Enter professional qualification',
        }
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': placeholders.get(field, ''),
            })

#Caller
class AddCaller(forms.ModelForm):
    dob = forms.DateField(label="Date Of Birth" ,localize=True,widget=forms.DateInput(format = '%d-%m-%Y',attrs={'type': 'date','format':format}),)
    # staff_type = forms.ChoiceField(choices=choice)

    class Meta:        
        model = Caller
        fields ="__all__"
        exclude=("caller",)
        labels={
            'address':'Permanent Address',
        }
        
        

    def __init__(self, *args, **kwargs):
        super(AddCaller, self).__init__(*args, **kwargs)
                 
        placeholders = {
            'name': 'Enter your name',
            'dob': 'DD/MM/YYYY',
            'gender': 'Gender',
            'email' :'Email',
            'address': 'Permanent Address',
            'academic_qualification': 'Select academic qualification',
            'professional_qualification': 'Enter professional qualification',
        }
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': placeholders.get(field, ''),
            })

#adding Student
class AddStudent(forms.ModelForm):
    dob = forms.DateField(label="Date Of Birth" ,localize=True,widget=forms.DateInput(format = '%d-%m-%Y',attrs={'type': 'date','format':format}),)
    course_id= forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={'size': 10,'class': 'form-control chosen-select', 'multiple': True}),
        label='Select courses to enroll in',
        required=True
    )

    class Meta:        
        model = Student
        fields ="__all__"
        labels={
            'course_id':'Course Enrolled',
        }
        exclude=("student",)

    def __init__(self, *args, **kwargs):
        super(AddStudent, self).__init__(*args, **kwargs)
                 
        placeholders = {
            'name': 'Name',
            'FatherHusband_name': "Enter Father's/Husband's name",
            'mother_name': "Enter Mother's name",
            'dob': 'DD/MM/YYYY',
            'gender': 'Gender',
            'email' :'Email',
            'address': 'Permanent Address',
            'mobile_number': 'Enter mobile number',
            'guardian_phone_number': 'Enter Guardian phone number',
            'ParentHusband_occupation': "Enter Parent's/Husband's occupation",
            'academic_qualification': 'Select academic qualification',
            'professional_qualification': 'Enter professional qualification',
        }
        

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': placeholders.get(field, ''),
            })
            
class AddCourse(forms.ModelForm):
    class Meta:        
        model = Course
        fields ="__all__"
        labels={
            'name':'Course Name',
        }
        exclude=('no_of_students',)

