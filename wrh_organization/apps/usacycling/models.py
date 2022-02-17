from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import JSONField


class Address(models.Model):
    street = models.CharField(max_length=200, null=True, blank=True)
    street2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    postal = models.CharField(max_length=200, null=True, blank=True)
    friendly_address = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.CharField(max_length=200, null=True, blank=True)
    longitude = models.CharField(max_length=200, null=True, blank=True)


class Dates(models.Model):
    event_date_id = models.CharField(max_length=200, null=True, blank=True)
    event_date_description = models.CharField(max_length=200, null=True, blank=True)
    event_date_start = models.DateField()
    event_date_end = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Links(models.Model):
    logo_url = models.CharField(max_length=200, null=True, blank=True)
    badge_url = models.CharField(max_length=200, null=True, blank=True)
    register_url = models.CharField(max_length=200, null=True, blank=True)
    website_url = models.CharField(max_length=200, null=True, blank=True)
    social_urls = ArrayField(
        models.CharField(max_length=200, null=True, blank=True),
        size=50,
        null=True,
        blank=True
    )


class USAEvent(models.Model):
    event_id = models.BigIntegerField()
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    dates = models.ForeignKey(Dates, on_delete=models.CASCADE, null=True)
    is_featured = models.BooleanField()
    is_weekend = models.BooleanField()
    is_multiday = models.BooleanField()
    is_usac_sanctioned = models.BooleanField()
    event_organizer_email = models.CharField(max_length=300, null=True, blank=True)
    event_status = models.CharField(max_length=300)
    permit = models.CharField(max_length=300, null=True, blank=True)
    labels = ArrayField(
        models.CharField(max_length=100),
        size=50,
        null=True
    )
    tags = ArrayField(
        ArrayField(
            models.CharField(max_length=50, blank=True),
            size=50,
        ),
        size=50,
        null=True,
        blank=True
    )
    links = models.ForeignKey(Links, on_delete=models.CASCADE, null=True, blank=True)
    data_source = models.CharField(max_length=300)
    created_at = models.DateField()
    updated_at = models.DateField()


class USACyclingClubTeams(models.Model):
    team_id = models.BigIntegerField()
    team_name = models.CharField(max_length=200)
    team_club_id = models.IntegerField()
    women_only = models.IntegerField()
    masters_only = models.IntegerField()
    juniors_only = models.IntegerField()
    d_elite = models.IntegerField()
    team_legacy_id = models.IntegerField()


class USACyclingClubs(models.Model):
    club_id = models.BigIntegerField()
    club_name = models.CharField(max_length=200, null=True, blank=True)
    club_org_id = models.CharField(max_length=100, null=True, blank=True)
    club_ncaa_id = models.CharField(max_length=100, null=True, blank=True)
    club_updated_by_user = models.CharField(max_length=100, null=True, blank=True)
    club_aff_type_id = models.IntegerField()
    club_type_id = models.IntegerField()
    club_legacy_id = models.IntegerField()
    club_disciplines = models.CharField(max_length=100, null=True, blank=True)
    club_aff_type = JSONField()
    is_active = models.BooleanField()
    club_teams = models.ManyToManyField(USACyclingClubTeams, related_name='clubteam')
    expiration_date = models.DateField()


class USARider(models.Model):
    license = models.IntegerField(primary_key=True)
    suspension = models.IntegerField(blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    racingage = models.IntegerField(blank=True, null=True)
    expdateroad = models.IntegerField(blank=True, null=True)
    expdatemtn = models.IntegerField(blank=True, null=True)
    rdclub = models.CharField(max_length=255, blank=True, null=True)
    rdteam = models.CharField(max_length=255, blank=True, null=True)
    trackclub = models.CharField(max_length=255, blank=True, null=True)
    trackteam = models.CharField(max_length=255, blank=True, null=True)
    cxclub = models.CharField(max_length=255, blank=True, null=True)
    cxteam = models.CharField(max_length=255, blank=True, null=True)
    mtnclub = models.CharField(max_length=255, blank=True, null=True)
    mtnteam = models.CharField(max_length=255, blank=True, null=True)
    intlteam = models.CharField(max_length=255, blank=True, null=True)
    nccaclub = models.CharField(max_length=255, blank=True, null=True)
    roadcat = models.CharField(max_length=20, blank=True, null=True)
    trackcat = models.CharField(max_length=20, blank=True, null=True)
    crosscat = models.CharField(max_length=20, blank=True, null=True)
    downhillcat = models.CharField(max_length=20, blank=True, null=True)
    mxcat = models.CharField(max_length=20, blank=True, null=True)
    xccat = models.CharField(max_length=20, blank=True, null=True)
    otcat = models.CharField(max_length=20, blank=True, null=True)
    cxcat = models.CharField(max_length=20, blank=True, null=True)
    citizen = models.IntegerField(blank=True, null=True)
    emergencycontact = models.CharField(max_length=255, blank=True, null=True)
    econtactphone = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    foreignteam = models.CharField(max_length=200, blank=True, null=True)
    ucicode = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=200, blank=True, null=True)
    collclub = models.CharField(max_length=200, blank=True, null=True)
    rdclubid = models.IntegerField(blank=True, null=True)
    rdteamid = models.IntegerField(blank=True, null=True)
    trackclubid = models.IntegerField(blank=True, null=True)
    trackteamid = models.IntegerField(blank=True, null=True)
    mtnclubid = models.IntegerField(blank=True, null=True)
    mtnteamid = models.IntegerField(blank=True, null=True)
    cxclubid = models.IntegerField(blank=True, null=True)
    cxteamid = models.IntegerField(blank=True, null=True)
    collclubid = models.IntegerField(blank=True, null=True)
    cxrank = models.FloatField(blank=True, null=True)
    dhcat = models.CharField(max_length=20, blank=True, null=True)
    hsclub = models.CharField(max_length=255, blank=True, null=True)
