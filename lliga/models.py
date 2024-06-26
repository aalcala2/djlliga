from django.db import models

# Create your models here.
class Lliga(models.Model):
    nom = models.CharField(max_length=100)
    temporada = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    

class Equip(models.Model):
    nom = models.CharField(max_length=100)
    lliga = models.ForeignKey(Lliga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Jugador(models.Model):
    nom = models.CharField(max_length=100)
    posicio = models.CharField(max_length=50)
    edat = models.IntegerField()
    equip = models.ForeignKey(Equip, related_name='equips', on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.nombre

class Partit(models.Model):
    lliga = models.ForeignKey(Lliga, related_name='lliga', on_delete=models.CASCADE)
    data = models.DateField()
    equip_local = models.ForeignKey(Equip, related_name='equip_local', on_delete=models.CASCADE)
    equip_visitant = models.ForeignKey(Equip, related_name='equip_visitant', on_delete=models.CASCADE)
    gols_local = models.IntegerField()
    gols_visitant = models.IntegerField()
    

    def __str__(self):
        return f"{self.equip_local} vs {self.equip_visitant} - {self.data}"