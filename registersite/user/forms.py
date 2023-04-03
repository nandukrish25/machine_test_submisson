from django import forms






class registrationform(forms.Form):
    name=forms.CharField(max_length=100)
    country=forms.CharField(max_length=100)
    nationality=forms.CharField(max_length=100)
    mobile=forms.CharField(max_length=100)
    role=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=100)
    password=forms.CharField(max_length=100)


class loginform(forms.Form):
   
    email=forms.EmailField(max_length=100)
    password=forms.CharField(max_length=100)    
                              