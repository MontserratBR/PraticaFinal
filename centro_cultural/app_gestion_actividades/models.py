from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Monitor(models.Model):
    nombre = models.CharField(max_length=50)
    especializacion = models.CharField(max_length=100)

    @property
    def numero_actividades_asignadas(self):
        return self.actividades.count()
    
    def __str__(self):
        return self.nombre


class ResponsableSala(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Sala(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=150)

    responsable = models.OneToOneField(
        ResponsableSala,
        on_delete=models.CASCADE,
        related_name='sala'
    )

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    horario = models.DateTimeField()
    descripcion = models.TextField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    plazas_disponibles = models.IntegerField()

    monitor = models.ForeignKey(
        Monitor,
        on_delete=models.CASCADE,
        related_name='actividades'
    )

    sala_principal = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name='actividades_principales'
    )

    usuarios = models.ManyToManyField(
        Usuario,
        through='Inscripcion',
        related_name='actividades'
    )

    salas_secundarias = models.ManyToManyField(
        Sala,
        related_name='actividades_secundarias',
        blank=True
    )

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE
    )

    fecha_inscripcion = models.DateField(auto_now_add=True)
    asistencia = models.BooleanField(default=False)
    class Meta:
        unique_together = ('usuario', 'actividad')

    def __str__(self):
        return f"{self.usuario.nombre} - {self.actividad.nombre}"