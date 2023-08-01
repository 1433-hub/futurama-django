from django.contrib import admin
from .models import *

class HomeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Home, HomeAdmin)

class ProjectNameInLine(admin.StackedInline):
    model = ProjectName

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectNameInLine,
    ]
admin.site.register(Project, ProjectAdmin)

class VisitingNameInLine(admin.StackedInline):
    model = VisitingName

class VisitingAdmin(admin.ModelAdmin):
    inlines = [
        VisitingNameInLine,
    ]
admin.site.register(Visiting, VisitingAdmin)

class ResourceNameInLine(admin.StackedInline):
    model = ResourceName

class ResourceAdmin(admin.ModelAdmin):
    inlines = [
        ResourceNameInLine,
    ]
admin.site.register(Resource, ResourceAdmin)

class BrandingNameInLine(admin.StackedInline):
    model = BrandingName

class BrandingAdmin(admin.ModelAdmin):
    inlines = [
        BrandingNameInLine,
    ]
admin.site.register(Branding, BrandingAdmin)

class OeprationInChargeInLine(admin.StackedInline):
    model = OperationInCharge

class EventManagementAdmin(admin.ModelAdmin):
    inlines = [
        OeprationInChargeInLine,
    ]
admin.site.register(EventManagement, EventManagementAdmin)

class GetTestimonialsInLine(admin.StackedInline):
    model = GetTestimonials

class TestimonialsAdmin(admin.ModelAdmin):
    inlines = [
        GetTestimonialsInLine,
    ]
admin.site.register(Testimonials, TestimonialsAdmin)

class FavoriteToolsInLine(admin.StackedInline):
    model = FavoriteTools

class MyWeaponAdmin(admin.ModelAdmin):
    inlines = [
        FavoriteToolsInLine,
    ]
admin.site.register(MyWeapon, MyWeaponAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)

admin.site.register(Footer)

