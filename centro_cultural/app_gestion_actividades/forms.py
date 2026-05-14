from django import forms
from .models import Usuario,Monitor,Sala,Actividad,Inscripcion,ResponsableSala


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

class MonitorForm(forms.ModelForm):

    class Meta:
        model = Monitor
        fields = '__all__'

class ResponsableSalaForm(forms.ModelForm):

    class Meta:
        model = ResponsableSala
        fields = '__all__'



class SalaForm(forms.ModelForm):

    class Meta:
        model = Sala
        fields = '__all__'

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
        widgets = {
            'horario': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),

            'descripcion': forms.Textarea(
                attrs={'rows': 4}
            ),

            'salas_secundarias': forms.CheckboxSelectMultiple()
        }

class InscripcionForm(forms.ModelForm):

    class Meta:
        model = Inscripcion
        fields = '__all__'