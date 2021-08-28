from django import forms
from django.core import validators

class contact_form(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"type":"text", "placeholder":"Name", "class":"contact__input"}),
        label=False,
        validators=[
            validators.MaxLengthValidator(50, 'Your first and last name can not be more than 50 characters')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={"type":"mail", "placeholder":"Email", "class":"contact__input"}),
        label=False,
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"name":"", "id":"", "cols":"0", "rows":"10", "class":"contact__input"}),
        label=False
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@" not in email:
            raise forms.ValidationError("Enter a valid email address")
        if ".com" not in email:
            raise forms.ValidationError("Enter a valid email address")
        if  len(email) > 100:
            raise forms.ValidationError("Your email could not be longer than 100 characters")
        return email