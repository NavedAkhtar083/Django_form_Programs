from django import forms
class studentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField( label=('password(again)'),widget=forms.PasswordInput)
    
    
    def clean(self):
        cleaned_data=super().clean()
        valpass=self.cleaned_data['password']
        valrepass=self.cleaned_data['repassword']
        
        if valpass!=valrepass:
            raise forms.ValidationError('password not match')
        