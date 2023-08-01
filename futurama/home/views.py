from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import MessageForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home = Home.objects.all().order_by("-id")
        context["home"] = home
        return context

class ProjectView(TemplateView):
    template_name = 'project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_name = ProjectName.objects.all().order_by("-id")
        project = Project.objects.all().order_by("-id")
        context["project"] = project
        context["project_name"] = project_name
        return context

class VisitingView(TemplateView):
    template_name = 'visiting.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visiting_name = VisitingName.objects.all().order_by("-id")
        visiting = Visiting.objects.all().order_by("-id")
        context["visiting"] = visiting
        context["visiting_name"] = visiting_name
        return context

class OperationView(TemplateView):
    template_name = 'operation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resource_name = ResourceName.objects.all().order_by("-id")
        resource = Resource.objects.all().order_by("-id")
        branding_name = BrandingName.objects.all().order_by("-id")
        branding = Branding.objects.all().order_by("-id")
        context["resource"] = resource
        context["resource_name"] = resource_name
        context["branding"] = branding
        context["branding_name"] = branding_name
        return context

class EventManagementView(TemplateView):
    template_name = 'eventmanagement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        operation_in_charge = OperationInCharge.objects.all().order_by("-id")
        event_management = EventManagement.objects.all().order_by("-id")
        context["event_management"] = event_management
        context["oic"] = operation_in_charge
        return context

class TestimonialsView(TemplateView):
    template_name = 'testimonials.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_testimonials = GetTestimonials.objects.all().order_by("-id")
        testimonials = Testimonials.objects.all().order_by("-id")
        context["get_testimonials"] = get_testimonials
        context["testimonials"] = testimonials
        return context   

class MyWeaponsView(TemplateView):
    template_name = 'myweapons.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_tools = FavoriteTools.objects.all().order_by("-id")
        my_weapon = MyWeapon.objects.all().order_by("-id")
        context["favorite_tools"] = favorite_tools
        context["my_weapon"] = my_weapon
        return context  

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = Contact.objects.all().order_by("-id")
        footer = Footer.objects.all().order_by("-id")
        context["contact"] = contact
        context["footer"] = footer
        return context  
    
    def post(self, request, *args, **kwargs):
        messageForm = MessageForm(request.POST)
        if messageForm.is_valid():
            username = request.POST.get('name')
            email = request.POST.get('email')
            feedback = request.POST.get('feedback')
            try:
                validate_email(email)
                if username and not email and not feedback:
                    messages.add_message(request, messages.WARNING, 'Please enter the required field!')
                    return render(request, self.template_name)
                else:
                    messageObject = Message.objects.create(
                        name = username,
                        email = email,
                        feedback = feedback
                    )
                    messageObject.save()
                    messages.add_message(request, messages.INFO, 'Thank you for your feedback!')
                    return render(request, self.template_name)
            except ValidationError as e:
                print(e)