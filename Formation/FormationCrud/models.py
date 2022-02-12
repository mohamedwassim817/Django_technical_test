from django.db import models

class Formation (models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(type='web')
        def get_querymobile(self):
            return super().get_queryset().filter(type='mobile')
        def get_querycloud(self):
            return super().get_queryset().filter(type='cloud')
    appli = (
     ('web', 'Web'),
     ('mobile','Mobile'),
     ('cloud','Cloud'),
     )
    etats = (
      ('active', 'Active'),
      ('non', 'Desactive'),
    )
    titre = models.CharField(max_length=255)
    logo = models.ImageField(null=True, blank=True, upload_to='images/')
    type = models.CharField(max_length=10, choices=appli, default='web')
    etat =models.CharField(max_length=10, choices=etats ,default='active')
    objects = models.Manager()
    newmanager = NewManager()

    def __str__(self):
        return self.titre