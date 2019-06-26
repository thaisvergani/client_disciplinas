from django import forms


class CourseForm(forms.Form):
    nome = forms.CharField(max_length=30)
    codigo = forms.IntegerField()
