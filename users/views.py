from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django import forms
from users.forms import UserForm, UserProfileForm

# Create your views here.
@login_required 
def user_logout(request):
	logout(request)
	#return HttpResponseRedirect('/home/') 
	return render(request, 'index.html') 

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return render(request, 'index.html')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render_to_response('users/login.html',{},RequestContext(request))

@login_required
def user_update_info(request):
	return render(request, 'users/showUserInfo.html') 
    

def register(request):

	Context = RequestContext(request)

	if request.method == 'POST': #user bilgilerini girmis kayit ol butonuna basmis.
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
            #registered = True

			profile = profile_form.save(commit = False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			return render(request, 'users/register_success.html')

		else:
			print user_form.errors, profile_form.errors

	else: # henuz yeni register ekrani goren user icin
		user_form = UserForm()
		profile_form = UserProfileForm()
        
        return render_to_response(
		'users/registration.html',
		{'user_form':user_form, 'profile_form':profile_form}, Context)
