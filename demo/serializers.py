from rest_framework import serializers
from .models import Cities,Population,Population0To6,Literates, Ratio,LiteracyRate,Graduates

class MalepopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Population
        fields = ('population_male','city')

class FemalepopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Population
        fields = ('population_female','city')

class TotalpopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Population
        fields = ('population_total','city')

class ZeroToSixpopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Population0To6
        fields = ('population_total0to6','city')

class ZeroToSixMalepopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Population0To6
        fields = ('population_male0to6','city')

class ZeroToSixFemalepopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Population0To6
        fields = ('population_female0to6','city')

class LiteratesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Literates
        fields = ('literates_total','city')

class MaleliteratesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Literates
        fields = ('literates_male','city')

class FemaleliteratesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Literates
        fields = ('literates_female','city')

class SexratioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ratio
        fields = ('sex_ratio','city')

class ChildsexratioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ratio
        fields = ('child_sex_ratio','city')

class EffectiveliteracyratetotalSerializers(serializers.ModelSerializer):
    class Meta:
        model = LiteracyRate
        fields = ('effective_literacy_rate_total','city')


class EffectiveliteracyratemaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = LiteracyRate
        fields = ('effective_literacy_rate_male','city')

class EffectiveliteracyratefemaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = LiteracyRate
        fields = ('effective_literacy_rate_female','city')

class TotalgraduatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Graduates
        fields = ('total_graduates','city')

class MalegraduatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Graduates
        fields = ('male_graduates','city')

class FemalegraduatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Graduates
        fields = ('female_graduates','city')

class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('location','name_of_city')















# class PopSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Cities
#         # fields = ('name_of_city', 'state_code')
#         fields = ('population_total','state_name')
#
# class femalepopSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Cities
#         # fields = ('name_of_city', 'state_code')
#         fields = ('population_female','state_name')
#
# class Zero_to_sixSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cities
#         # fields = ('name_of_city', 'state_code')
#         fields = ('population_total_0to6','state_name')
#
# class Zero_to_six_maleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cities
#         # fields = ('name_of_city', 'state_code')
#         fields = ('population_male_0to6','state_name')
#
