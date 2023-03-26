from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

from blog.models import BlogPost



# imports for REST API
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import Account
from account.serializers import AccountSerializer
from django.http.response import JsonResponse
from django.http import HttpResponse




def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            # account = authenticate(email=email, password=password1)
            login(request, account)
            # ! mysite urls.py name=home redirects to home page
            return redirect('home')
        else:
            context['registration_form'] = form
    else: # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

# ! logout
def logout_view(request):
    logout(request)
    return redirect('home')




# ! login
def login_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)

# ! edit account
def account_view(request):

    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial= {
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts


    return render(request, 'account/account.html', context)
    

def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})







# REST API

# GET all accounts
@api_view(['GET'])
def getAccounts(request):
    account = Account.objects.all()
    serializer = AccountSerializer(account, many=True)

    return Response(serializer.data)

# GET one account (e.g account/id)
@api_view(['GET'])
def getAccount(request, slug):
    account = Account.objects.get(pk=slug)
    serializer = AccountSerializer(account, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def addAccount(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Successfully POST")
    return HttpResponse("Couldn't POST")

@api_view(['PUT'])
def updateAccount(request, slug):
    account = Account.objects.get(pk=slug)
    serializer = AccountSerializer(account, many=False, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Successfully PUT")
    return HttpResponse("Couldn't PUT")


@api_view(['DELETE'])
def deleteAccount(request, slug):
    if Account.objects.get(pk=slug).delete():
        return HttpResponse("Successfully DELETE")
    return HttpResponse("Couldn't DELETE")
