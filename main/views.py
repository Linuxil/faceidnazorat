from django.shortcuts import render
from django.utils.decorators import method_decorator
from .models import Users,Kelish,Ketish,Ish_vaqti
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,UpdateView,DeleteView
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Users
from .utils import compare_faces
from datetime import timedelta,datetime,time
from django.utils import timezone
import pytz

# Create your views here.

class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.username != 'admin':
            return redirect('mobile/')
        employees = Users.objects.exclude(username='admin')
        context = {'employees': employees}
        return render(request, 'index.html',context)
    def post(self,request):
        searchuser = request.POST.get('searchuser')
        employees = Users.objects.filter(
            Q(first_name=searchuser) |
            Q(last_name=searchuser) |
            Q(username=searchuser) |
            Q(position=searchuser)
            ).exclude(username='admin')
        users = Users.objects.exclude(username='admin')
        context = {'employees':employees,'users':users}
        return render(request, 'index.html',context)

def mobile(request):
    return render(request, 'mobile.html')

def kelish_ketish(request):
    return render(request,'kelish_ketish.html')

class LoginView(View):
    def get(self,request):
        return render(request, 'login2.html')
 
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not Users.objects.filter(username=username).exists():
            return redirect('/login')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            user = Users.objects.get(username=username)
            if user.position == "admin":
                return redirect('/')
            return redirect('/mobile')  
        message = "Login yoki parol xato"  
        context = {"message":message}
        return render(request,'login2.html',context)
    

@csrf_exempt
def capture_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # path = default_storage.save(os.path.join('images', image.name), ContentFile(image.read()))
        user = Users.objects.get(username=request.user.username)
        user_image = user.image
        
        if compare_faces(image,user_image) == "Success":
            print(user.first_name)
            kelish = Kelish.objects.create(user=user)
            kelish.save()

            # kelish_data = (Kelish.objects.get(user=user).date+timedelta(hours=5)).strftime("%H:%M:%S")
            message = "Siz autorizatiyadan o'tdingiz"
            context = {'message': message, }
            return JsonResponse({'status': 'success', 'redirect_url': '/kelish_ketish/'})
        else:
            context = {
                'status': 'failed',
                'redirect_url': '/capture/',
                'message': "Siz autorizatiyadan o`tmadingiz qayta urunib ko'ring"  # Message ma'lumoti
            }
            return JsonResponse(context)
    today = datetime.today()
    last_obj = Kelish.objects.filter(user=request.user)
    for i in last_obj:
        if  (i.date+timedelta(hours=5)).date() == today.date() and i.user == request.user:
            message = "Siz bugun kelish jadvaliga yozildingiz"
            context = {'message':message}
            return render(request, 'kelish_ketish.html',context)
    kelish = Kelish.objects.filter(user=request.user)
    ketish = Ketish.objects.filter(user=request.user)
    if kelish.count() != ketish.count():
        message = "Sizda tamomlanmagan ish kuni mavjud"
        context = {'message':message}
        return render(request, 'kelish_ketish.html',context)
    return render(request, 'kelish.html')

@csrf_exempt
def capture_view_ketish(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # path = default_storage.save(os.path.join('images', image.name), ContentFile(image.read()))
        user = Users.objects.get(username=request.user.username)
        user_image = user.image
    
        if compare_faces(image,user_image) == "Success":
            print(user.first_name)
            
            ketish = Ketish.objects.create(user=user)
            ketish.save()
            return JsonResponse({'status': 'success', 'redirect_url': '/kelish_ketish/'})
        else:
            context = {
                'status': 'failed',
                'redirect_url': '/capture/',
                'message': "Siz autorizatiyadan o`tmadingiz qayta urunib ko'ring"  # Message ma'lumoti
            }
            return JsonResponse(context)

    kelish = Kelish.objects.filter(user=request.user)
    ketish = Ketish.objects.filter(user=request.user)
    if kelish.count() == ketish.count():
        message = "Siz ketish jadvaliga allaqochon yozilgansiz yoki bugun kelish jadvaliga yozilmagansiz"
        context = {'message':message}
        return render(request, 'kelish_ketish.html',context)
    return render(request, 'ketish.html')


def nazorat_mobile(request):
    kelish = Kelish.objects.filter(user = request.user)
    sanalar = []
    for i in kelish:
        sanalar.append((i.date+timedelta(hours=5)).strftime("%d.%m.%Y"))

    print(sanalar)
  
    context = {"sanalar": sanalar}

    return render(request,'nazorat_jadvali.html',context)


def nazorat_jadvali_date(request, i):
    ish_vaqti = Ish_vaqti.objects.get()
    # kelishlar = []
    # ketishlar = []
    print(i)
    kelish = Kelish.objects.all()
    for j in kelish:
        if (j.date+timedelta(hours=5)).strftime("%d.%m.%Y") == i:
            kelishlar = (j.date+timedelta(hours=5)).strftime("%d.%m.%Y - %H:%M:%S") 
    print(kelishlar)
    ketish = Ketish.objects.all()
    for j in ketish:
        if (j.date+timedelta(hours=5)).strftime("%d.%m.%Y") == i:
            ketishlar = (j.date+timedelta(hours=5)).strftime("%d.%m.%Y - %H:%M:%S") 
    context = {"kelishlar":kelishlar,"ketishlar":ketishlar,"ish_vaqti":ish_vaqti}
    return render(request,'nazorat_jadvali_date.html',context)
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect( '/login')
    

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
  
class EmployeeDetailView(UpdateView):
    template_name = "update_employee.html"
    model = Users
    fields = ['first_name','last_name','position','username','phone','password']
    success_url = "/"

    def form_valid(self, form):
        form.instance.password = make_password(self.request.POST.get('password'))
        return super().form_valid(form)



class AddEmployeeView(CreateView):
    template_name = "update_employee.html"
    model = Users
    fields = ['first_name','last_name','position','username','password']
    success_url = "/"

    def form_valid(self, form):
        form.instance.password = make_password(self.request.POST.get('password'))
        return super().form_valid(form)


def delete_employee(request,pk):
    try:
        employee = get_object_or_404(Users,pk=pk ) 
    except:
        return JsonResponse({"status":"error"})
    else:
        employee.delete() 
          
        return redirect('/')   
    


# from .forms import YourModelForm

# def profil_setting(request, pk):
#     # Ma'lumotni olish
#     obj = get_object_or_404(Users, pk=pk)
    
#     if request.method == 'POST':
#         # Formani ma'lumot bilan to'ldirish
#         form = YourModelForm(request.POST, instance=obj)
#         if form.is_valid():
#             form.save()
#             return redirect('/mobile/')  # O'zingizning muvaffaqiyatli URLingizni qo'shing
#     else:
#         # Bo'sh formani ko'rsatish
#         form = YourModelForm(instance=obj)
    
#     context = {
#         'form': form
#     }
#     return render(request, 'profil_settings.html', context)

class EditProfilView(UpdateView):
    template_name = "profil_settings.html"
    model = Users
    fields = ("image","phone","first_name","last_name","username","password")
    success_url = "/mobile/"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form_title"] = "Mijoz ma'lumotlarini tahrirlash"
        context["button_title"] = "Saqlash"
        return context

class AdminProfilView(UpdateView):
    template_name = "admin_settings.html"
    model = Users
    fields = ("image","phone","first_name","last_name","username","password")
    success_url = "/"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form_title"] = "Mijoz ma'lumotlarini tahrirlash"
        context["button_title"] = "Saqlash"
        return context