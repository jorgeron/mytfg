from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django import forms
from embed_video.fields import EmbedVideoField
from datetime import datetime

# Create your models here.
class Actor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    foto_perfil = models.ImageField(null=True, blank=True, upload_to='imagenes/perfil_img/%Y-%m-%d/', verbose_name=_('Foto de perfil'))
    foto_cabecera = models.ImageField(null=True, blank=True, upload_to='imagenes/cabecera_img/%Y-%m-%d/', verbose_name=_('Foto de cabecera'))
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    telefono_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("El teléfono debe tener el siguiente formato: '+999999999'. Permitidos hasta 15 dígitos."))
    telefono = models.CharField(validators=[telefono_regex], blank=True, max_length=15,verbose_name=_("Teléfono")) # validators should be a list   
    descripcion = models.TextField(max_length=500, blank=True, null= True)
    
    def __unicode__(self):
        return self.user.username

    class Meta:
        abstract = True

class Administrador(Actor):
	class Meta:
		verbose_name= _('Administrador')
		verbose_name_plural = _('Administradores')
	def __unicode__(self):
		return self.nombre

class Jugador(Actor):
	SEXOS = (
		('H', 'Hombre'),
		('M', 'Mujer'),
	)

	apellidos = models.CharField(max_length=200, verbose_name=_("Apellidos"))
	fecha_nacimiento = models.DateField(verbose_name=_("Fecha de nacimiento"))
	sexo = models.CharField(max_length=1, choices=SEXOS)
	localidad = models.CharField(max_length=50, verbose_name=_('Localidad'))

	#atributos derivados de valoraciones
	nivel_juego = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
	fiabilidad_reserva = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
	sociabilidad = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
	valoracion_total = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)

	#atributos derivados de partidos
	partidos_jugados = models.DecimalField(max_digits=4, decimal_places=0, default=0)
	partidos_ganados = models.DecimalField(max_digits=4, decimal_places=0, default=0)
	rating_victorias = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)

	class Meta:
		verbose_name = _('Jugador')
		verbose_name_plural = _('Jugadores')

	def __unicode__(self):
		return self.nombre +' '+ self.apellidos

	def __str__(self):
		return self.nombre +' '+ self.apellidos


class Empresa(Actor):
	direccion = models.CharField(max_length=200, verbose_name=_("Dirección"))
	paypalMail = models.EmailField(verbose_name=_("PayPal e-mail"))

	#atributos derivados de valoraciones
	calidad_precio = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
	personal = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
	limpieza = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
	valoracion_total = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre


class Pista(models.Model):
	
	TIPOS_SUPERFICIES = (
		('CESPED', 'Césped artificial'),
		('HORMIGON', 'Hormigón poroso'),
		('MOQUETA', 'Moqueta'),
	)

	TIPOS_PARED = (
		('METACRILATO', 'Metacrilato'),
		('CEMENTO', 'Cemento'),
	)

	empresa = models.ForeignKey(Empresa)

	nombre = models.CharField(max_length=20)
	tipo_superficie = models.CharField(max_length=20, choices=TIPOS_SUPERFICIES, default='CESPED')
	tipo_pared = models.CharField(max_length=20, choices=TIPOS_PARED, default='METACRILATO')
	cubierta = models.BooleanField(default=False)
	descripcion = models.TextField(blank=True, null=True)
	foto = models.ImageField(null=True, blank=True, upload_to='images/pistas/%Y-%m-%d/', verbose_name=_('Foto de pista'))
	visible = models.BooleanField(default=True)

	#atributos derivados de valoraciones
	estado = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
	iluminacion = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
	valoracion_total = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)

	def __str__(self):
		return self.nombre


class Horario(models.Model):
	empresa = models.ForeignKey(Empresa)

	nombre = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre


class DiaAsignacionHorario(models.Model):
	pista = models.ForeignKey(Pista)

	dia = models.DateField(auto_now=False ,verbose_name=_("Día"))
	class Meta:
		unique_together = (('pista','dia'),)

class FranjaHoraria(models.Model):
	horario = models.ForeignKey(Horario)
	dia_asignacion = models.ForeignKey(DiaAsignacionHorario, blank=True, null=True)
	jugador = models.ForeignKey(Jugador, blank=True, null=True)

	hora_inicio = models.TimeField(auto_now=False, auto_now_add=False)
	hora_fin = models.TimeField(auto_now=False, auto_now_add=False)
	precio = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0.01)])
	disponible = models.BooleanField(default=True)
	asignada = models.BooleanField(default=False)

	@property
	def finalizada(self):
		fecha_fin_partido = datetime.combine(self.dia_asignacion.dia, self.hora_fin)
		return datetime.now() > fecha_fin_partido


class Post(models.Model):
	user = models.ForeignKey(User)

	texto = models.TextField(max_length=200, null=False)
	fecha_publicacion = models.DateTimeField(auto_now=True)
	foto = models.ImageField(null=True, blank=True, upload_to='post_pics/%Y-%m-%d/', verbose_name='Foto')
	video = EmbedVideoField(null=True, blank=True)

	def __unicode__(self):
		return self.texto

	class Meta:
		verbose_name='Post'
		verbose_name_plural='Posts'


class Seguimiento(models.Model):
    origen = models.ForeignKey(User, related_name="siguiendo")
    destino = models.ForeignKey(User, related_name="seguidores")
    class Meta:
        unique_together = (('origen','destino'))


class Propuesta(models.Model):

	TIPOS_PARTIDO = (
		('MASCULINO', 'Masculino'),
		('FEMENINO', 'Femenino'),
		('MIXTO', 'Mixto')
		)

	creador = models.ForeignKey(Jugador, related_name='creador')

	titulo = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=200, blank=True, null= True)
	fecha_publicacion = models.DateTimeField(auto_now=True)
	fecha_limite = models.DateTimeField(auto_now=False)
	fecha_partido = models.DateTimeField(auto_now=False)
	tipo_partido = models.CharField(max_length=9, choices=TIPOS_PARTIDO)
	sitio = models.CharField(max_length=20, blank=True, null= True)

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name='Propuesta'
		verbose_name_plural='Propuestas'


class Participante(models.Model):
    jugador = models.ForeignKey(Jugador)
    propuesta = models.ForeignKey(Propuesta)
    class Meta:
        unique_together = (('jugador','propuesta'))


class Comentario(models.Model):
	jugador = models.ForeignKey(Jugador)
	propuesta = models.ForeignKey(Propuesta)

	texto = models.TextField(max_length=200, null=False)
	fecha_publicacion = models.DateTimeField(auto_now=True)
	foto = models.ImageField(null=True, blank=True, upload_to='comentario_pics/%Y-%m-%d/', verbose_name='Foto')
	video = EmbedVideoField(null=True, blank=True)

	def __unicode__(self):
		return self.texto

	class Meta:
		verbose_name='Comentario'
		verbose_name_plural='Comentarios'


class Valoracion(models.Model):
	emisor = models.ForeignKey(User)

	opinion = models.TextField(max_length=200, null=True, blank=True)
	fecha_publicacion = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.opinion

	class Meta:
		verbose_name='Valoracion'
		verbose_name_plural='Valoraciones'


class ValoracionJugador(Valoracion):
	jugador = models.ForeignKey(Jugador)

	nivel_juego = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	fiabilidad_reserva = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	sociabilidad = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])


class ValoracionEmpresa(Valoracion):
	empresa = models.ForeignKey(Empresa)

	calidad_precio = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	personal = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	limpieza = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])


class ValoracionPista(Valoracion):
	pista = models.ForeignKey(Pista)

	estado = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	iluminacion = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])





class Resultado(models.Model):
	jugador1 = models.ForeignKey(Jugador, related_name='jugador1')
	jugador2 = models.ForeignKey(Jugador, related_name='jugador2')

	jugador3 = models.ForeignKey(Jugador, related_name='jugador3')
	jugador4 = models.ForeignKey(Jugador, related_name='jugador4')

	empresa = models.ForeignKey(Empresa, related_name='empresa')
	franja_horaria = models.ForeignKey(FranjaHoraria)

	pareja1set1 = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(7)])
	pareja2set1 = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(7)])
	
	pareja1set2 = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(7)])
	pareja2set2 = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(7)])
	
	pareja1set3 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(7)])
	pareja2set3 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(7)])

	pareja1totalSets = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
	pareja2totalSets = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(2)])

	fecha_partido = models.DateTimeField(auto_now=False)

	class Meta:
		verbose_name='Resultado'
		verbose_name_plural='Resultados'



