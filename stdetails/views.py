from django.views.generic import TemplateView
from django.views.generic import FormView
from .forms import registerform,Loginform
from .models import Post,details
from .variables import Variables

class HomePageView(FormView):
    template_name = "home.html"
    form_class = Loginform
    success_url = 'details'
    def form_valid(self,form):
        #Post.objects.all().delete()
        #details.objects.all().delete()
        #A = Post(Username=form.cleaned_data['Username'])
        if Post.objects.filter(Username=form.cleaned_data['Username']).exists():
            Variables.currentUser = Username=form.cleaned_data['Username']
            return super().form_valid(form)
        else:
            #k = Post(Username=form.cleaned_data['Username'],password=form.cleaned_data['Password'])
            #k.save(self)
            print(Post.objects.all())
            return super().form_invalid(form)
            
class DetailsPageView(TemplateView):
    
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        context = super(DetailsPageView, self).get_context_data(**kwargs)
        if Post.objects.filter(Username=Variables.currentUser).exists():
            context['details'] = Post.objects.get(Username = Variables.currentUser) 
        return context
    

class RegisterPageView(FormView):
    template_name = "register.html"
    form_class = registerform
    success_url = '/'
    def form_valid(self,form):
        if not Post.objects.filter(Username = form.cleaned_data['Pin_no']).exists():
            if  form.cleaned_data['Password'] == form.cleaned_data['confirm_password']:
                a = Post(Username=form.cleaned_data['Pin_no'],password=form.cleaned_data['Password'])
                a.save()
                k = details(Fristname=form.cleaned_data['Fristname'],Lastname=form.cleaned_data['Lastname'],Pin_no=form.cleaned_data['Pin_no'])
                k.save()
                return super().form_valid(form)
        for M in Post.objects.all():
            print(M.Username)
            print(M.password)
        return super().form_invalid(form)
# Create your views here.

