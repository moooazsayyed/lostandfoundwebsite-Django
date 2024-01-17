from django.shortcuts import render, HttpResponse,  redirect
from .models import Listing, Listing_mobile,Listing_people,Listing_pets
from .forms import UploadImg
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
     listings = Listing.objects.all()
     listings = list(listings)
     return render(request, 'index.html', {'listings': listings})
    
def category(request):
    return HttpResponse("Welcome to the web page")

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method=='POST':
     uname=request.POST.get('username')
     pass1=request.POST.get('password1')
     user=authenticate(request,username=uname,password=pass1)
     if user is not None:
        login(request,user)
        return render(request,'index.htm')
     else:
        return render(request,'index.html')
    return render(request,'login.html')

def form(request):
    if request.method == 'POST':
        form = UploadImg(request.POST, request.FILES)
        if form.is_valid():
            # Create an instance of Listing and populate it with form data
            listing = Listing(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                state=form.cleaned_data['state'],
                categorie=form.cleaned_data['categorie'],
                image=form.cleaned_data['image'],
            )
            listing.save()

            category = form.cleaned_data['categorie']  # Get the category from the form

            # Check the category and create an instance in the corresponding table
            if category == 'mobile':
                listing_mobile = Listing_mobile(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    state=form.cleaned_data['state'],
                    categorie=category,
                    image=form.cleaned_data['image'],
                )
                listing_mobile.save()
            elif category == 'people':
                listing_people = Listing_people(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    state=form.cleaned_data['state'],
                    categorie=category,
                    image=form.cleaned_data['image'],
                )
                listing_people.save()
            elif category == 'pets':
                listing_pets = Listing_pets(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['state'],
                    state=form.cleaned_data['state'],
                    categorie=category,
                    image=form.cleaned_data['image'],
                )
                listing_pets.save()

        listings = Listing.objects.all()
        return render(request, 'index.html', {'listings': listings})
    else:
        form = UploadImg()
    return render(request, 'form.html', {'form': form})


def Register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return render(request, 'register.html')
        
        my_user=user.objects.create_user(uname,email,pass1)
        my_user.save()
        return render(request,'login.html')
        print(uname,email,pass1,pass2)
    return render(request,'register.html')

def contact(request):
    return render(request,'contactus.html')

def categories(request):
   return render(request,'categories.html')

def privacy(request):
    return render(request,'privacy.html')

def view(request):
    id = request.GET.get('id')
    listing = Listing.objects.filter(id=id)
    
    if listing:
        data = listing.first()  # Assuming you want to retrieve the first matching listing
    else:
        data = None  # Set data to None if not found
    
    return render(request, 'fulldetail.html', { 'data': data })

def fulldetail(request):
    listings = Listing.objects.all()
    listings = list(listings)
    return render(request, 'fulldetail.html', {'listings': listings})

def mobile(request):
    listing_mobiles = Listing_mobile.objects.all()
    listing_mobiles = list(listing_mobiles)
    return render(request, 'mobile.html', {'listing_mobiles': listing_mobiles})

def people(request):
    listing_peoples = Listing_people.objects.all()
    listing_peoples = list(listing_peoples)
    return render(request, 'people.html', {'listing_peoples': listing_peoples})


def mobile(request):
    listing_mobiles = Listing_mobile.objects.all()
    listing_mobiles = list(listing_mobiles)
    return render(request, 'mobile.html', {'listing_mobiles': listing_mobiles})

def pets(request):
    listing_petss = Listing_pets.objects.all()
    listing_petss = list(listing_petss)
    return render(request, 'pets.html', {'listing_petss': listing_petss})