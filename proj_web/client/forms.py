from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(max_length=30)
    code = forms.EmailField(max_length=254)


class SubjectForm(forms.Form):
    name = forms.CharField(max_length=30)
    code = forms.EmailField(max_length=254)
    course  =  forms.ChoiceField()
