# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class DistrictCoords(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    gid_2 = models.CharField(max_length=80, blank=True, null=True)
    name_2 = models.CharField(max_length=80, blank=True, null=True)
    district = models.CharField(max_length=80, blank=True, null=True)
    engtype_2 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DISTRICT_COORDS'


class IndDistricts(models.Model):
    id = models.BigAutoField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    gid_2 = models.CharField(max_length=80, blank=True, null=True)
    name_2 = models.CharField(max_length=80, blank=True, null=True)
    district = models.CharField(max_length=80, blank=True, null=True)
    type_2 = models.CharField(max_length=80, blank=True, null=True)
    engtype_2 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IND_DISTRICTS'


class IndDistricts2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    gid_2 = models.CharField(max_length=80, blank=True, null=True)
    name_2 = models.CharField(max_length=80, blank=True, null=True)
    district = models.CharField(max_length=80, blank=True, null=True)
    engtype_2 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IND_DISTRICTS2'


class IndDistricts3(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    gid_2 = models.CharField(max_length=80, blank=True, null=True)
    name_2 = models.CharField(max_length=80, blank=True, null=True)
    district = models.CharField(max_length=80, blank=True, null=True)
    engtype_2 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IND_DISTRICTS3'


class IndStates(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    engtype_1 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IND_STATES'


class IndStates2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    engtype_1 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IND_STATES2'


class IndStates3(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    engtype_1 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IND_STATES3'


class StateCoords(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    engtype_1 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STATE_COORDS'


class TestCen(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    catid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=254, blank=True, null=True)
    cutdescription = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    street = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    zip = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    date = models.CharField(max_length=254, blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    gid_2 = models.CharField(max_length=80, blank=True, null=True)
    name_2 = models.CharField(max_length=80, blank=True, null=True)
    district = models.CharField(max_length=80, blank=True, null=True)
    engtype_2 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=3, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TEST_CEN'


class TestCen2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    catid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=254, blank=True, null=True)
    cutdescription = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    street = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    zip = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    date = models.CharField(max_length=254, blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    gid_2 = models.CharField(max_length=80, blank=True, null=True)
    name_2 = models.CharField(max_length=80, blank=True, null=True)
    district = models.CharField(max_length=80, blank=True, null=True)
    engtype_2 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=3, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TEST_CEN2'


class TestCen3(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    catid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=254, blank=True, null=True)
    cutdescription = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    street = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    zip = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    date = models.CharField(max_length=254, blank=True, null=True)
    gid_1 = models.CharField(max_length=80, blank=True, null=True)
    name_1 = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    gid_2 = models.CharField(max_length=80, blank=True, null=True)
    name_2 = models.CharField(max_length=80, blank=True, null=True)
    district = models.CharField(max_length=80, blank=True, null=True)
    engtype_2 = models.CharField(max_length=80, blank=True, null=True)
    statecode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TEST_CEN3'


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
