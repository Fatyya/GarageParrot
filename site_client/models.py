from django.db import models

# Create your models here.
class SiteInfoManager(models.Manager):
    def get_singleton(self):
        return self.first()

class SiteInfo(models.Model):
    nom_site = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    address = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()
    numero_telephone = models.CharField(max_length=20)

    objects = SiteInfoManager()

    def __str__(self):
        return self.nom_site

    class Meta:
        verbose_name = 'Site Information'
        verbose_name_plural = 'Site Information'


class Slider(models.Model):
    image = models.ImageField(upload_to='slider/')
    caption = models.CharField(max_length=200)
    link = models.URLField(default="/")

    def __str__(self):
        return self.caption

class Service(models.Model):
    nom_service = models.CharField(max_length=255)
    description = models.TextField()
    icon_service = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom_service

class Testimonial(models.Model):
    nom_client = models.CharField(max_length=100)
    temoinages_content = models.TextField()
    avatar_image = models.ImageField(upload_to='testimonials_avatars/', null=True, blank=True)

    def __str__(self):
        return self.nom_client



class Car(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    annee = models.PositiveIntegerField()
    kilometres = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images_voitures/')
  