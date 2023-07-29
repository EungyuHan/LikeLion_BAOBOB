from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserBassForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'id', 'is_superuser']