from django.forms import ModelForm
from .models import Demography,Cities,Graduates,LiteracyRate,Literates,Population,Population0To6,Ratio

class DataForm(ModelForm):
    class Meta:
        model = Demography
        fields = '__all__'

class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        fields = '__all__'

class GraduatesForm(ModelForm):
    class Meta:
        model = Graduates
        fields = '__all__'

class LiteracyRateForm(ModelForm):
    class Meta:
        model = LiteracyRate
        fields = '__all__'

class LiteratesForm(ModelForm):
    class Meta:
        model = Literates
        fields = '__all__'

class PopulationForm(ModelForm):
    class Meta:
        model = Population
        fields = '__all__'

class Population0To6Form(ModelForm):
    class Meta:
        model = Population0To6
        fields = '__all__'

class RatioForm(ModelForm):
    class Meta:
        model = Ratio
        fields = '__all__'