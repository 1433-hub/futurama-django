from django.db import models
from django.urls import reverse

class Home(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    slogan = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="home")
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="project")

    def __str__(self):
        return self.title    

class ProjectName(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="project_name")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Visiting(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="visiting")
    

    def __str(self):
        return self.title

class VisitingName(models.Model):
    ONGOING_STATUS = (
        ('Upcoming','Upcoming'),
        ('We are here','We are here'),
        ('Happening','Happening'),
        ('Wrapped Up','Wrapped Up'),
    )

    NUMBER_STATUS = (
        ('25','25'),
        ('50','50'),
        ('75','75'),
        ('100','100'),
    )
    
    title = models.CharField(max_length=200, blank=True, null=True)
    ongoing = models.CharField(max_length=200, choices=ONGOING_STATUS, default="Upcoming")
    number = models.CharField(max_length=200, choices=NUMBER_STATUS, default="25")
    visiting_name = models.ForeignKey(Visiting, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

class Resource(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class ResourceName(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Branding(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class BrandingName(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    branding = models.ForeignKey(Branding, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class EventManagement(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    experience = models.PositiveSmallIntegerField()
    student_number = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title 

class OperationInCharge(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="eventmanager")
    operationincharge = models.ForeignKey(EventManagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Testimonials(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="testimonials")

    def __str__(self):
        return self.title

class GetTestimonials(models.Model):
    name = models.CharField(max_length=200, blank=True, null=False)
    description = models.TextField()
    designation = models.CharField(max_length=200, blank=True, null=False, default="None")
    image = models.ImageField(upload_to="testimonials_student", default="default.png")
    get_testimonials = models.ForeignKey(Testimonials, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MyWeapon(models.Model):
    title = models.CharField(max_length=200, blank=True, null=False)
    description = models.TextField()
    def __str__(self):
        return self.title    
    
class FavoriteTools(models.Model):
    ANIMATION = (
        ('bounceIn','bounceIn'),
        ('fadeInDown','fadeInDown'),
        ('fadeInUp','fadeInUp'),
        ('fadeInRight','fadeInRight'),
        ('fadeInLeft','fadeInLeft'),
    )
    title = models.CharField(max_length=200, blank=True, null=False)
    image = models.ImageField(upload_to="favorite_tools")
    give_number = models.CharField(max_length=150, default="one")
    animation = models.CharField(max_length=200, choices=ANIMATION, default='bounceIn')
    tools = models.ForeignKey(MyWeapon, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    title = models.CharField(max_length=200, blank=True, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to="contact")

    def __str__(self):
        return self.title
    
class Message(models.Model):
    name = models.CharField(max_length=200, blank=True, null=False)
    email = models.EmailField(max_length=200, unique=True)
    feedback = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("contact")
    
    
    
class Footer(models.Model):
    country = models.CharField(max_length=200, default="Nepal")
    email = models.EmailField()
    phone_number = models.PositiveBigIntegerField()
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    tiktok_url = models.URLField()
    image = models.ImageField(upload_to="footer")

    def __str__(self):
        return self.email
    


