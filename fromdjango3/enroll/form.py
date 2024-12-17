from django import forms
class studentRegistration(forms.Form):
    name=forms.CharField(empty_value="sonam")
    age=forms.IntegerField()
    email=forms.EmailField()
    rollno=forms.IntegerField(min_value=5 ,max_value=20)
    
    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError("enter more than or equal to 4")
        return valname
    