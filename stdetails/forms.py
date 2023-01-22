from django import forms

class registerform(forms.Form):
    Fristname = forms.CharField(max_length=50,required=True,widget = forms.TextInput
                                        (attrs={'placeholder':'Fristname'}))
    Lastname = forms.CharField(max_length=50,required=True,widget = forms.TextInput
                                        (attrs={'placeholder':'Lastname'}))
    Pin_no = forms.CharField(max_length=50,required=True,widget = forms.TextInput
                                        (attrs={'placeholder':'Pin_no'}))
    Password = forms.CharField(max_length=50,required=True,widget = forms.TextInput
                                        (attrs={'placeholder':'Password'}))
    confirm_password = forms.CharField(max_length=50,required=True,widget = forms.TextInput
                                        (attrs={'placeholder':'confirm_password'}))
                                    

class Loginform(forms.Form):
    Username = forms.CharField(max_length=50,required=True,widget = forms.TextInput
                                        (attrs={'placeholder':'Username'}))

    Password = forms.CharField( max_length=50, required=True,widget= forms.TextInput
                                        (attrs={'placeholder':'Password'}))
