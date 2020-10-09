from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom


class Plat(models.Model):
    """Model definition for Plat."""

    # TODO: Define fields here
    categorie = models.ForeignKey(Categorie, related_name="catPlat", on_delete=models.CASCADE)
    nom = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/plat")
    description = models.TextField()
    prix = models.IntegerField()

    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Plat."""

        verbose_name = 'Plat'
        verbose_name_plural = 'Plats'

    def __str__(self):
        """Unicode representation of Plat."""
        return self.nom




class Testimony(models.Model):
    """Model definition for Testimony."""

    # TODO: Define fields here
    image = models.ImageField(upload_to="images/testimony")
    nom = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    description = models.TextField()
    fb = models.URLField(max_length=200)
    tweet = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)

    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)


    class Meta:
        """Meta definition for Testimony."""

        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonys'

    def __str__(self):
        """Unicode representation of Testimony."""
        return self.nom




class Reservation(models.Model):
    """Model definition for Reservation."""

    # TODO: Define fields here
    user = models.ForeignKey(User, related_name="userReserve", on_delete=models.CASCADE)
    nombre_personne = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    heure = models.TimeField(auto_now=False, auto_now_add=True)

    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)



    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        """Unicode representation of Reservation."""
        return self.user.username



class Service(models.Model):
    """Model definition for Service."""

    # TODO: Define fields here
    icon = models.CharField(max_length=250)
    titre = models.CharField(max_length=250)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Nos Services'
        verbose_name_plural = 'Nos Services'

    def __str__(self):
        """Unicode representation of Service."""
        return self.titre
