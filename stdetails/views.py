from django.views.generic import TemplateView
from django.views.generic import FormView
from .forms import registerform,Loginform
from .models import Post,details
from .variables import Variables

class HomePageView(FormView):
    template_name = "home.html"
    form_class = Loginform
    #Post.objects.all().delete()
    #details.objects.all().delete()
    success_url = 'details'
    def form_valid(self,form):
        #A = Post(Username=form.cleaned_data['Username'])
        if Post.objects.filter(Username=form.cleaned_data['Username']).exists():
            if Post.objects.get(Username=form.cleaned_data['Username']).password == form.cleaned_data['Password']:
                Variables.currentUser=form.cleaned_data['Username']
                return super().form_valid(form)
            else:
                print("worng password")
                return super().form_invalid(form)
        else:
            print("User doesnot exists")
            #k = Post(Username=form.cleaned_data['Username'],password=form.cleaned_data['Password'])
            #k.save(self)
            #print(Post.objects.all())
            return super().form_invalid(form)
            
class DetailsPageView(TemplateView):
    
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        #print(Variables.currentUser)
        if Post.objects.filter(Username=Variables.currentUser).exists():
            context = super(DetailsPageView, self).get_context_data(**kwargs)
            context['details'] = details.objects.get(Pin_no = Variables.currentUser)
         #   print(Post.objects.all())
            return context
    

class RegisterPageView(FormView):
    for M in Post.objects.all():
           print(M.Username)
           print(M.password)
    template_name = "register.html"
    form_class = registerform
    success_url = '/'
    def form_valid(self,form):
        if not Post.objects.filter(Username = form.cleaned_data['Pin_no']).exists() and form.cleaned_data['Password'] == form.cleaned_data['confirm_password']:
            a = Post(Username=form.cleaned_data['Pin_no'],password=form.cleaned_data['Password'])
            a.save()
            k = details(Fristname=form.cleaned_data['Fristname'],Lastname=form.cleaned_data['Lastname'],Pin_no=form.cleaned_data['Pin_no'])
            k.save()
            return super().form_valid(form)
        return super().form_invalid(form)
# Create your views here.

