from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('root')
        else:
            password_mismatch_added = False
            
            for field in form.errors:
                if 'class' not in form[field].field.widget.attrs:
                    form[field].field.widget.attrs['class'] = 'form-control is-invalid'
                else:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
                
                if field == 'password2':
                    for error in form.errors[field]:
                        if ("비밀번호가 일치하지 않습니다" in error or "The two password fields didn't match" in error) and not password_mismatch_added:
                            messages.error(request, "비밀번호가 일치하지 않습니다. 다시 확인해주세요.")
                            password_mismatch_added = True
                else:
                    for error in form.errors[field]:
                        messages.error(request, error)
        
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
        
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('root')
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, error)
            return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('root')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def profile_update(request):
    if request.method == 'GET':
        form = UserProfileUpdateForm(instance=request.user)
        return render(request, 'accounts/profile_update.html', {'form': form})
    else:
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 성공적으로 업데이트되었습니다.')
            return redirect('accounts:profile')
        else:
            for field in form.errors:
                if 'class' not in form[field].field.widget.attrs:
                    form[field].field.widget.attrs['class'] = 'form-control is-invalid'
                else:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
                
                for error in form[field].errors:
                    messages.error(request, error)
        return render(request, 'accounts/profile_update.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
        messages.success(request, '계정이 성공적으로 삭제되었습니다.')
        return redirect('root')
    return render(request, 'accounts/delete_account.html')