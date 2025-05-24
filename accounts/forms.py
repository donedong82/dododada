from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일'}))
    phone = forms.CharField(max_length=11, min_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '전화번호', 'pattern': '[0-9]{11}', 'title': '숫자 11자리만 입력해주세요', 'maxlength': '11'}))
    birth_year = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '출생년도', 'min': '1900', 'max': '2024'}))
    birth_month = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '출생월', 'min': '1', 'max': '12'}))
    birth_day = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '출생일', 'min': '1', 'max': '31'}))
    gender = forms.ChoiceField(choices=User.GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '주소'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone', 'birth_year', 'birth_month', 'birth_day', 'gender', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': '비밀번호를 입력하세요'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': '비밀번호를 다시 입력하세요'})
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다. 다시 확인해주세요.", code='password_mismatch')
        return password2
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            return phone
            
        phone_digits = ''.join(filter(str.isdigit, phone))
        
        if not phone_digits:
            raise forms.ValidationError("전화번호는 숫자만 입력해주세요.", code='invalid_phone')
        
        if len(phone_digits) != 11:
            raise forms.ValidationError("전화번호는 정확히 11자리여야 합니다.", code='invalid_phone_length')
            
        return phone_digits
    
    def clean(self):
        cleaned_data = super().clean()
        
        birth_year = cleaned_data.get('birth_year')
        birth_month = cleaned_data.get('birth_month')
        birth_day = cleaned_data.get('birth_day')
        
        if birth_year and birth_month and birth_day:
            if birth_year < 1900 or birth_year > 2024:
                self.add_error('birth_year', "출생년도는 1900년부터 2024년 사이여야 합니다.")
                
            if birth_month < 1 or birth_month > 12:
                self.add_error('birth_month', "출생월은 1월부터 12월 사이여야 합니다.")
                
            days_in_month = {
                1: 31, 2: 29 if (birth_year % 4 == 0 and birth_year % 100 != 0) or birth_year % 400 == 0 else 28,
                3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }
            
            if birth_day < 1 or (birth_month in days_in_month and birth_day > days_in_month[birth_month]):
                self.add_error('birth_day', f"{birth_month}월은 {days_in_month.get(birth_month, 31)}일까지 있습니다.")
        
        return cleaned_data
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("이미 사용 중인 아이디입니다. 다른 아이디를 사용해주세요.", code='duplicate_username')
        return username
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("이메일은 필수 입력 항목입니다.", code='required')
        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 사용 중인 이메일입니다. 다른 이메일을 사용해주세요.", code='duplicate_email')
        return email

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone', 'birth_year', 'birth_month', 'birth_day', 'gender', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '전화번호', 'pattern': '[0-9]{11}', 'title': '숫자 11자리만 입력해주세요', 'maxlength': '11'}),
            'birth_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '출생년도', 'min': '1900', 'max': '2024'}),
            'birth_month': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '출생월', 'min': '1', 'max': '12'}),
            'birth_day': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '출생일', 'min': '1', 'max': '31'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '주소'}),
        }
        
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            return phone
            
        phone_digits = ''.join(filter(str.isdigit, phone))
        
        if not phone_digits:
            raise forms.ValidationError("전화번호는 숫자만 입력해주세요.", code='invalid_phone')
        
        if len(phone_digits) != 11:
            raise forms.ValidationError("전화번호는 정확히 11자리여야 합니다.", code='invalid_phone_length')
            
        return phone_digits
    
    def clean(self):
        cleaned_data = super().clean()
        
        birth_year = cleaned_data.get('birth_year')
        birth_month = cleaned_data.get('birth_month')
        birth_day = cleaned_data.get('birth_day')
        
        if birth_year and birth_month and birth_day:
            if birth_year < 1900 or birth_year > 2024:
                self.add_error('birth_year', "출생년도는 1900년부터 2024년 사이여야 합니다.")
                
            if birth_month < 1 or birth_month > 12:
                self.add_error('birth_month', "출생월은 1월부터 12월 사이여야 합니다.")
                
            days_in_month = {
                1: 31, 2: 29 if (birth_year % 4 == 0 and birth_year % 100 != 0) or birth_year % 400 == 0 else 28,
                3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }
            
            if birth_day < 1 or (birth_month in days_in_month and birth_day > days_in_month[birth_month]):
                self.add_error('birth_day', f"{birth_month}월은 {days_in_month.get(birth_month, 31)}일까지 있습니다.")
        
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username != self.instance.username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("이미 사용 중인 아이디입니다. 다른 아이디를 사용해주세요.", code='duplicate_username')
        return username