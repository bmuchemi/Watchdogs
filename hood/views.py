from django.shortcuts import render,redirect,get_object_or_404
from .models import Neighbourhood,Buisness,Post,Profile
from .forms import UploadNewNeighbourhood,UploadNewBuisness,PostForm,UserRegisterForm,  ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def uploadNeighbourhood(request):
    form=UploadNewNeighbourhood()
    current_user=request.user

    if request.method =="POST":
        form=UploadNewNeighbourhood(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood=form.save(commit=False)
            neighbourhood.user=current_user
            neighbourhood.save()

        return redirect('viewHood')

    else:
        form=UploadNewNeighbourhood()

    return render(request, 'upload_hood.html', {"form":form})

@login_required
def viewHood(request):
    
    hoods = Neighbourhood.objects.all()
    context = {
       
        'hoods':hoods
      }

    return render(request,'hood.html', context)

@login_required
def hood(request,pk):
    hood=Neighbourhood.objects.filter(id=pk)
    current_user=request.user


    return render(request, 'viewHood.html', {"hood":hood})

@login_required
def uploadBuisness(request):
    form=UploadNewBuisness()
    current_user=request.user

    if request.method =="POST":
        form=UploadNewBuisness(request.POST, request.FILES)
        if form.is_valid():
            bizna=form.save(commit=False)
            bizna.user=current_user
            bizna.save()

        return redirect('business')

    else:
        form=UploadNewBuisness()

    return render(request, 'upload_buisness.html', {"form":form})




@login_required
def viewBizna(request):
    
    bizna = Buisness.objects.all()
    context = {
       
        'bizna':bizna
      }

    return render(request,'business.html', context)


@login_required
def bizna(request,pk):
    bizna=Buisness.objects.filter(id=pk)
    current_user=request.user
    return render(request, 'view_business.html', {"bizna":bizna})


    
@login_required
def create_post(request):
    form=PostForm
    current_user=request.user

    if request.method =="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()

        return redirect('viewHood')

    else:
        form=PostForm()

    return render(request, 'post.html', {"form":form})



@login_required
def viewPost(request):
    
    posts = Post.objects.all()
    context = {
       
        'posts':posts
      }

    return render(request,'posts.html', context)


@login_required
def searchBizna(request):
    
    if 'bizna' in request.GET and request.GET['bizna']:
        search_term=request.GET.get('bizna')
        searched_buisnesses=Buisness.search_by_name(search_term)
        message=f"{search_term}"

        return render(request, "searchb.html", {"bizna":searched_buisnesses, "message":message})
    else:
        message="You have not searched for any buissness"
        return render(request, "searchb.html")

@login_required
def searchHood(request):
    
    if 'hood' in request.GET and request.GET['hood']:
        search_term=request.GET.get('hood')
        searched_hoods=Neighbourhood.search_by_hood(search_term)
        message=f"{search_term}"

        return render(request, "searchh.html", {"hood":searched_hoods, "message":message})
    else:
        message="You have not searched for any hoods"
        return render(request, "searchh.html")

def join_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.hood = neighbourhood
    request.user.profile.save()
    return redirect('viewHood')


def leave_neighbourhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.hood = None
    request.user.profile.save()
    return redirect('viewHood')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'django_registration/registration.html', {"form":form})


def profile(request):
    profile = Profile.objects.get_or_create(name=request.user)
    if request.method =='POST':
        profile_update_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('profile')
    else:
        profile_update_form = ProfileUpdateForm()

    context = {
        'profile_update_form': profile_update_form,
       
    }
    return render(request, 'profile.html', context)

