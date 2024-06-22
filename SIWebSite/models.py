from django.db import models


class ImportFileModel (models.Model):
    date = models.DateTimeField()
    file = models.FileField(upload_to='Files/')
    activated = models.BooleanField(default=False)
    # desc = models.CharField (max_length=1024)

    def __str__(self):
        return f"File id:{self.id}"


class RIDModel(models.Model):
    Jour = models.DateField()
    Prefecture = models.CharField(max_length=100)
    csc = models.CharField(max_length=100)
    TYPE = models.CharField(max_length=100)
    RID_ID = models.CharField(max_length=100)
    STATUT_paquet = models.CharField(max_length=100)
    Commentaire = models.TextField()

    def __str__(self):
        return self.RID_ID
