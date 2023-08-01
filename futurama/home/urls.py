from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('project/', ProjectView.as_view(), name='project'),
    path('visiting/', VisitingView.as_view(), name='visiting'),
    path('operation/', OperationView.as_view(), name='operation'),
    path('event-management/', EventManagementView.as_view(), name='event-management'),
    path('testimonials/', TestimonialsView.as_view(), name='testimonials'),
    path('my-weapons/', MyWeaponsView.as_view(), name='my-weapons'),
    path('contact-us/', ContactView.as_view(), name='contact'),
]