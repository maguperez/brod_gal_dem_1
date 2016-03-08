# coding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from empresa.models import Empresa
from .utils import anos_nacimiento, meses_del_ano, dias_del_mes
import datetime

class CuentaCrearForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name' ]


    def clean_email(self):
        email = self.cleaned_data["email"]
        if email is None or email == '':
            raise forms.ValidationError('Email es obligatorio')
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        #raise forms.ValidationError(self.error_messages['duplicate_email'])
        raise forms.ValidationError('Email ya esta registrado')


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contraseña', 'type':'password', 'class': 'form-control'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

class UniqueUserEmailField(forms.EmailField):
    """
    An EmailField which only is valid if no User has that email.
    """
    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email = value)
            raise forms.ValidationError("Email ya esta registrado")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Email ya esta registrado")
        except User.DoesNotExist:
            pass

class RegisterForm(UserCreationForm):

    items_anos = anos_nacimiento()
    items_meses = meses_del_ano()
    items_dias = dias_del_mes()

     #Carga items a Grado de Estudio
    empresas= []
    for e in Empresa.objects.all():
        empresas.append((e.id, e.nombre))
    items_empresa =[('','Empresa')] + empresas


    username = forms.CharField(required = False, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}))
    email = UniqueUserEmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Nombres', 'class': 'form-control'}))
    last_name = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'class': 'form-control'}))
    password1 = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Contraseña', 'type':'password', 'class': 'form-control'}))
    password2 = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Confirmar Contraseña', 'type':'password', 'class': 'form-control'}))
    fecha_nacimiento = forms.DateField(required=False)
    ano = forms.ChoiceField(choices=items_anos, required = False, widget=forms.Select(attrs={'class': 'cumpleanos form-control', }))
    mes = forms.ChoiceField(choices=items_meses, required = False, widget=forms.Select(attrs={'class': 'cumpleanos form-control'}))
    dia = forms.ChoiceField(choices=items_dias, required = False, widget=forms.Select(attrs={'class': 'cumpleanos form-control'}))
    telefono = forms.CharField(required = False, max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'Numero telefonico', 'class': 'form-control'}))
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), empty_label="Empresa",  required = False, widget=forms.Select(attrs={'class': 'form-control', 'title': 'Recuerda que debes usar el correo de la compañía para registrarte', 'data-placement': 'right'}))

    def __init__(self, *args, **kwargs):
        """
        Changes the order of fields, and removes the username field.
        """
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['email', 'first_name', 'last_name',
                                'password1', 'password2']


    def __generate_username(self, email):
        # TODO: Something more efficient?
        highest_user_id = User.objects.all().order_by('-id')[0].id
        leading_part_of_email = email.split('@',1)[0]
        # leading_part_of_email = re.sub(r'[^a-zA-Z0-9+]', '',
        #                               leading_part_of_email)
        truncated_part_of_email = leading_part_of_email[:3] \
                                  + leading_part_of_email[-3:]
        derived_username = truncated_part_of_email + str(highest_user_id+1)
        return derived_username

    def clean(self, *args, **kwargs):
        """
        Normal cleanup + username generation.
        """
        cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
        if cleaned_data.has_key('email'):
            cleaned_data['username'] = self.__generate_username(
                                                        cleaned_data['email'])
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        #raise forms.ValidationError(self.error_messages['duplicate_email'])
        raise forms.ValidationError('duplicate_email')

    def save(self, commit=True):
        """
        Saves the email, first_name and last_name properties, after the normal
        save behavior is complete.
        """
        user = super(UserCreationForm, self).save(commit)
        if user:
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
        return user

class RegistroRepresentanteForm(UserCreationForm):

    username = forms.CharField(required = False, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = UniqueUserEmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Nombres'}))
    last_name = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    password1 = forms.CharField(required = True, max_length = 10, widget=forms.TextInput(attrs={'placeholder': 'Contraseña', 'type':'password'}))
    password2 = forms.CharField(required = True, max_length = 10, widget=forms.TextInput(attrs={'placeholder': 'Confirmar Contraseña', 'type':'password'}))
    telefono = forms.CharField(required = False, max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'Numero telefonico'}))
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), empty_label="Empresa",  required = False)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['email', 'first_name', 'last_name',
                                'password1', 'password2']


    def __generate_username(self, email):
        # TODO: Something more efficient?
        highest_user_id = User.objects.all().order_by('-id')[0].id
        leading_part_of_email = email.split('@',1)[0]
        truncated_part_of_email = leading_part_of_email[:3] \
                                  + leading_part_of_email[-3:]
        derived_username = truncated_part_of_email + str(highest_user_id+1)
        return derived_username

    def clean(self, *args, **kwargs):
        cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
        if cleaned_data.has_key('email'):
            cleaned_data['username'] = self.__generate_username(
                                                        cleaned_data['email'])
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate_email')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit)
        if user:
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
        return user

class EditarUsuarioForm( PasswordChangeForm ):

    new_password1 = forms.CharField(required = True, max_length = 10, widget=forms.TextInput(attrs={'placeholder': 'Escriba su nueva Contraseña', 'type':'password', 'class':'half'}))
    new_password2 = forms.CharField(required = True, max_length = 10, widget=forms.TextInput(attrs={'placeholder': 'Escriba otra vez su nueva contraseña', 'type':'password', 'class':'half'}))
    old_password = forms.CharField(required = True, max_length = 10, widget=forms.TextInput(attrs={'placeholder': 'Escriba su contraseña actual', 'type':'password', 'class':'half'}))

class CuentaEditarForm(forms.Form):
    first_name = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Nombres'}))
    last_name = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    telefono = forms.CharField(required = False, max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'Numero telefonico'}))

class ContrasenaRestaurarForm(forms.Form):
    email_or_username = forms.CharField(label=("Correo"), widget=forms.TextInput(attrs={'placeholder': 'Nombres',
                                                                                        'class': 'form-control'}), max_length=254)