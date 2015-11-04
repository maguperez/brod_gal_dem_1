from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForam(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombres'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    email = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Contrase&ntildea'}))
    password2 = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Confirmar Contrase&ntildea'}))
    fecha_nacimiento = forms.DateField(required=False)


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contrase&ntildea', 'type':'password'}))


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
    """
    Extends the built in UserCreationForm in several ways:

    * Adds an email field, which uses the custom UniqueUserEmailField,
      that is, the form does not validate if the email address already exists
      in the User table.
    * The username field is generated based on the email, and isn't visible.
    * first_name and last_name fields are added.
    * Data not saved by the default behavior of UserCreationForm is saved.
    """

    username = forms.CharField(required = False, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = UniqueUserEmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Nombres'}))
    last_name = forms.CharField(required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    password1 = forms.CharField(required = True, max_length = 10, widget=forms.TextInput(attrs={'placeholder': 'Contrase&ntildea', 'type':'password'}))
    password2 = forms.CharField(required = True, max_length = 10, widget=forms.TextInput(attrs={'placeholder': 'Confirmar Contrase&ntildea', 'type':'password'}))
    fecha_nacimiento = forms.DateField(required=False)

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
