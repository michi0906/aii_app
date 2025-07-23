from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(
    widget=forms.ClearableFileInput(attrs={'id': 'id_image'})
)
