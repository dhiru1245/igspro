from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Enter Your  Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }
        )
    )

    add = forms.CharField(
        label='Enter Your  Address',
        widget=forms.TextInput(
            attrs={
                 'class': 'form-control',
                'placeholder': 'Address'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Customer Email ID',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email ID'
            }
        )
    )

    mob = forms.IntegerField(
        label='Enter Your Contac No',
        widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contact No'
        }
        )
    )




class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    rating = forms.IntegerField(
        label='Enter Rating:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter Your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )