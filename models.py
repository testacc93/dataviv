# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cities(models.Model):
    name_of_city = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    state_name = models.CharField(max_length=50, blank=True, null=True)
    dist_code = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=-1, blank=True, null=True)
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'cities'


class Demography(models.Model):
    name_of_city = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    state_name = models.CharField(max_length=50, blank=True, null=True)
    dist_code = models.CharField(max_length=50, blank=True, null=True)
    population_total = models.CharField(max_length=50, blank=True, null=True)
    population_male = models.CharField(max_length=50, blank=True, null=True)
    population_female = models.CharField(max_length=50, blank=True, null=True)
    population_total0to6 = models.CharField(max_length=50, blank=True, null=True)
    population_male0to6 = models.CharField(max_length=50, blank=True, null=True)
    population_female0to6 = models.CharField(max_length=50, blank=True, null=True)
    literates_total = models.CharField(max_length=50, blank=True, null=True)
    literates_male = models.CharField(max_length=50, blank=True, null=True)
    literates_female = models.CharField(max_length=50, blank=True, null=True)
    sex_ratio = models.CharField(max_length=50, blank=True, null=True)
    child_sex_ratio = models.CharField(max_length=50, blank=True, null=True)
    effective_literacy_rate_total = models.CharField(max_length=50, blank=True, null=True)
    effective_literacy_rate_male = models.CharField(max_length=50, blank=True, null=True)
    effective_literacy_rate_female = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    total_graduates = models.CharField(max_length=50, blank=True, null=True)
    male_graduates = models.CharField(max_length=50, blank=True, null=True)
    female_graduates = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'demography'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Graduates(models.Model):
    total_graduates = models.CharField(max_length=50, blank=True, null=True)
    male_graduates = models.CharField(max_length=50, blank=True, null=True)
    female_graduates = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'graduates'


class LiteracyRate(models.Model):
    effective_literacy_rate_total = models.CharField(max_length=50, blank=True, null=True)
    effective_literacy_rate_male = models.CharField(max_length=50, blank=True, null=True)
    effective_literacy_rate_female = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'literacy_rate'


class Literates(models.Model):
    literates_total = models.CharField(max_length=50, blank=True, null=True)
    literates_male = models.CharField(max_length=50, blank=True, null=True)
    literates_female = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'literates'


class Population(models.Model):
    population_total = models.CharField(max_length=50, blank=True, null=True)
    population_male = models.CharField(max_length=50, blank=True, null=True)
    population_female = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'population'


class Population0To6(models.Model):
    population_total0to6 = models.CharField(max_length=50, blank=True, null=True)
    population_male0to6 = models.CharField(max_length=50, blank=True, null=True)
    population_female0to6 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'population0to6'


class Ratio(models.Model):
    sex_ratio = models.CharField(max_length=50, blank=True, null=True)
    child_sex_ratio = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratio'
