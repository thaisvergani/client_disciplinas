from django import forms


class SubjectForm(forms.Form):
    nome = forms.CharField(max_length=30)
    codigo = forms.IntegerField( label="Código")
    cargaHoraria = forms.IntegerField(label="Carga Horária")
    curso = forms.ChoiceField()
    area = forms.ChoiceField(label="Área")

    def __init__(self, courses=[], areas= [], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['curso'].choices =courses
        self.fields['area'].choices =areas


