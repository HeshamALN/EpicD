from django import forms

def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=80)
    phone = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea, required=True)
    forcefield = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave Empty", validators=[should_be_empty])