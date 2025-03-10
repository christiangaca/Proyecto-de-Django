from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200) #Con esto, decimos que vamos a crear una nueva tabla llamada Project,
                                            #donde se van a recoger variables name de tipo texto, con una lonmgitud máxima de 200 caracteres
    def __str__(self):
        return self.name

class Task(models.Model): #Esta va a ser una nueva entrada a la tabla de Sqlite3
    title = models.CharField(max_length=200)
    description = models.TextField() #TextField es para textos mayores
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Esto es para decirle que esta tabla está relacionada con la tabla Project y el parámetro
    #on_delete es para decirle lo que tiene que hacer cuando se elimine un proyecto. En este caso, cuando se elimine un dato, se eliminarán en cascada, los que tengan relación con él
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + '-' + self.project.name #Para que se meustre el nombre de la tarea juunto al proyecto asociado