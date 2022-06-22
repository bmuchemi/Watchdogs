from .models import Neighbourhood,Buisness,Post,Profile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UploadNewNeighbourhood(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        exclude=['occupant_count','admin']
        fields=['hood','location','pic','description','hospital_num','police_num']

class UploadNewBuisness(forms.ModelForm):
    class Meta:
        model=Buisness
        fields=['name','owner','hood','image','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pic', 'bio', 'hood', 'id_number','number', 'email']