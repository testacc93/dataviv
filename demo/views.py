from django.shortcuts import render, HttpResponse, redirect
from .models import Cities
from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import  status
from .models import Cities, Demography,Graduates, Population,Literates,Population0To6, Literates,Ratio,LiteracyRate
from .serializers import MalepopSerializers,FemalepopSerializers,TotalpopSerializers,ZeroToSixpopSerializers,ZeroToSixMalepopSerializers,ZeroToSixFemalepopSerializers,LiteratesSerializers,MaleliteratesSerializers,FemaleliteratesSerializers, SexratioSerializers,ChildsexratioSerializers,EffectiveliteracyratetotalSerializers,EffectiveliteracyratemaleSerializers,EffectiveliteracyratefemaleSerializers,TotalgraduatesSerializers,MalegraduatesSerializers,FemalegraduatesSerializers,LocationSerializers
from .forms import DataForm,CitiesForm,GraduatesForm,LiteracyRateForm,LiteratesForm,PopulationForm,Population0To6Form,RatioForm

class Male_pop(APIView):

    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        all_population = Population.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = MalepopSerializers(all_population, many=True)
        return Response(serializer.data)

class Female_pop(APIView):

    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        all_population = Population.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = FemalepopSerializers(all_population, many=True)
        return Response(serializer.data)

class Total_pop(APIView):

    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        all_population = Population.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = TotalpopSerializers(all_population, many=True)
        return Response(serializer.data)

class Zero_to_six_populationtotal(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        zerotosix_pop_total = Population0To6.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = ZeroToSixpopSerializers(zerotosix_pop_total, many=True)
        return Response(serializer.data)

class Zero_to_six_malepopulationtotal(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        zerotosix_pop_male = Population0To6.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = ZeroToSixMalepopSerializers(zerotosix_pop_male, many=True)
        return Response(serializer.data)

class Zero_to_six_femalepopulationtotal(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        zerotosix_pop_female = Population0To6.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = ZeroToSixFemalepopSerializers(zerotosix_pop_female, many=True)
        return Response(serializer.data)

class Literatestotal(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        total_literates = Literates.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = LiteratesSerializers(total_literates, many=True)
        return Response(serializer.data)

class Maleliteratestotal(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        male_literates = Literates.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = MaleliteratesSerializers(male_literates, many=True)
        return Response(serializer.data)

class Femaleliteratestotal(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        female_literates = Literates.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = FemaleliteratesSerializers(female_literates, many=True)
        return Response(serializer.data)

class Sexratio(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        sex_ratio = Ratio.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = SexratioSerializers(sex_ratio, many=True)
        return Response(serializer.data)

class Childsexratio(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        child_sex_ratio = Ratio.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = ChildsexratioSerializers(child_sex_ratio, many=True)
        return Response(serializer.data)

class Effectiveliteracyratetotal(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        literacy_rate_total = LiteracyRate.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = EffectiveliteracyratetotalSerializers(literacy_rate_total, many=True)
        return Response(serializer.data)

class Effectiveliteracyratemale(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        literacy_rate_male = LiteracyRate.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = EffectiveliteracyratemaleSerializers(literacy_rate_male, many=True)
        return Response(serializer.data)

class Effectiveliteracyratefemale(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        literacy_rate_female = LiteracyRate.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = EffectiveliteracyratefemaleSerializers(literacy_rate_female, many=True)
        return Response(serializer.data)

class Totalgraduates(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        total_grads = Graduates.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = TotalgraduatesSerializers(total_grads, many=True)
        return Response(serializer.data)

class Malegraduates(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        male_grads = Graduates.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = MalegraduatesSerializers(male_grads, many=True)
        return Response(serializer.data)

class Femalegraduates(APIView):
    def get(self, request, cityname):
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        female_grads = Graduates.objects.filter(city=capitalized_city_name+empty_string).values()
        serializer = FemalegraduatesSerializers(female_grads, many=True)
        return Response(serializer.data)

class Location(APIView):
    def get(self, request, cityname):
        print("tyhe city is", cityname)
        capitalized_city_name = cityname.capitalize()
        empty_string = ' '
        location = Cities.objects.filter(name_of_city=capitalized_city_name+empty_string).values()
        serializer = LocationSerializers(location, many=True)
        return Response(serializer.data)

# class Edit_data():
def add_data(request):
    city_form = CitiesForm()
    grads_form = GraduatesForm()
    literacyrate_form = LiteracyRateForm()
    literates_form = LiteratesForm()
    population_form = PopulationForm()
    population0To6_form = Population0To6Form()
    ratio_form = RatioForm()
    if request.method == 'POST':
        form_city_data = request.POST
        form_grad_data = request.POST
        form_literacy_data = request.POST
        form_literates_data = request.POST
        form_population_data = request.POST
        form_populaton0to6_data = request.POST
        form_ratio_data = request.POST



        # print("printing post",form_data['name_of_city'])
        from .models import Cities
        form_cities = Cities(name_of_city=form_city_data['name_of_city'], state_code=form_city_data['state_code'], state_name=form_city_data['state_name'], dist_code=form_city_data['dist_code'],
                             location=form_city_data['location'])
        form_cities.save()

        form_graduates = Graduates(total_graduates=form_grad_data['total_graduates'], male_graduates=form_grad_data['male_graduates'], female_graduates=form_grad_data['female_graduates'], city=form_grad_data['name_of_city'])
        form_graduates.save()

        form_literacy_rate = LiteracyRate(effective_literacy_rate_total=form_literacy_data['effective_literacy_rate_total'], effective_literacy_rate_male=form_literacy_data['effective_literacy_rate_male'], effective_literacy_rate_female=form_literacy_data['effective_literacy_rate_female'], city=form_literacy_data['name_of_city'])
        form_literacy_rate.save()

        form_literates = Literates(literates_total=form_literates_data['literates_total'], literates_male=form_literates_data['literates_male'], literates_female=form_literates_data['literates_female'], city=form_literates_data['name_of_city'])
        form_literates.save()

        form_population = Population(population_total=form_population_data['population_total'], population_male=form_population_data['population_male'], population_female=form_population_data['population_female'], city=form_population_data['name_of_city'])
        form_population.save()

        form_population0to6 = Population0To6(population_total0to6=form_populaton0to6_data['population_total0to6'], population_male0to6=form_populaton0to6_data['population_male0to6'], population_female0to6=form_populaton0to6_data['population_female0to6'], city=form_populaton0to6_data['name_of_city'])
        form_population0to6.save()

        form_ratio = Ratio(sex_ratio=form_ratio_data['sex_ratio'], child_sex_ratio=form_ratio_data['child_sex_ratio'], city=form_ratio_data['name_of_city'])
        form_ratio.save()



    form = DataForm(request.POST)
        # if form.is_valid():
        #     print("printing post",request.POST)

    context = {
        'form':city_form,
        'formgrads':grads_form,
        'formliteracyrate':literacyrate_form,
        'formliterates':literates_form,
        'formpopulation':population_form,
        'formpopulation0to6':population0To6_form,
        'formratio':ratio_form,
    }
    return render(request, 'add_data.html', context)


def update_data(request, pk):
    from .models import Cities

    capitalized_city = pk.capitalize()
    empty_string = ' '
    try:
        city_data = Cities.objects.get(name_of_city=capitalized_city+empty_string)
        graduates_data = Graduates.objects.get(city=capitalized_city + empty_string)
        literacy_rate_date = LiteracyRate.objects.get(city=capitalized_city + empty_string)
        literates_data = Literates.objects.get(city=capitalized_city+empty_string)
        population_data = Population.objects.get(city=capitalized_city+empty_string)
        population0to6_data = Population0To6.objects.get(city=capitalized_city+empty_string)
        ratio_data = Ratio.objects.get(city=capitalized_city+empty_string)



    except:
        city_data = Cities.objects.get(name_of_city=capitalized_city)
        graduates_data = Graduates.objects.get(city=capitalized_city)
        literacy_rate_date = LiteracyRate.objects.get(city=capitalized_city)
        literates_data = Literates.objects.get(city=capitalized_city)
        population_data = Population.objects.get(city=capitalized_city)
        population0to6_data = Population0To6.objects.get(city=capitalized_city)
        ratio_data = Ratio.objects.get(city=capitalized_city)

    print(";jfwfn",city_data)

    ##### PREFILLS FORM ###########
    form = CitiesForm(instance=city_data)
    formgrads = GraduatesForm(instance=graduates_data)
    formliteracy_rate = LiteracyRateForm(instance=literacy_rate_date)
    formliterates = LiteratesForm(instance=literates_data)
    formpopulation = PopulationForm(instance=population_data)
    formpopulation0to6 = Population0To6Form(instance=population0to6_data)
    formratio = RatioForm(instance=ratio_data)




    # formgrads = GraduatesForm(instance=graduates_data)

    if request.method == 'POST':
        form_cities = CitiesForm(request.POST)
        form_graduates = GraduatesForm(request.POST)
        form_literacy_rate = LiteracyRateForm(request.POST)
        form_literates = LiteratesForm(request.POST)
        form_population = PopulationForm(request.POST)
        form_population0to6 = Population0To6Form(request.POST)
        form_ratio = RatioForm(request.POST)
        if form_cities.is_valid():
            form_cities.save()
        if form_graduates.is_valid():
            form_graduates.save()
        if form_literacy_rate.is_valid():
            form_literacy_rate.save()
        if form_literates.is_valid():
            form_literates.save()
        if form_population.is_valid():
            form_population.save()
        if form_population0to6.is_valid():
            form_population0to6.save()
        if form_ratio.is_valid():
            form_ratio.save()
        return  redirect('/')
        

    context={
        'form':form,
        'formgrads':formgrads,
        'formliteracyrate': formliteracy_rate,
        'formliterates':formliterates,
        'formpopulation':formpopulation,
        'formpopulation0to6':formpopulation0to6,
        'formratio':formratio,

    }

    return render(request, 'add_data.html', context)


# class test(APIView):
#     def get(self, request, cityname):
#         capitalized_city_name = cityname.capitalize()
#         empty_string = ' '
#         location = Cities.objects.filter(name_of_city=capitalized_city_name+empty_string).values()
#
#         serializer = LocationSerializers(location, many=True)
#         return Response(serializer.data)






# {
# "state name":
# "city name":
# "population":
# }
#
# {
#     "city name":"male population"
# }