# Generated by Django 4.1.7 on 2023-04-03 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Femast",
            fields=[
                (
                    "f_id",
                    models.IntegerField(
                        blank=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("fe_type", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "fe_key",
                    models.CharField(blank=True, max_length=50, null=True, unique=True),
                ),
                ("fe_desc", models.CharField(blank=True, max_length=200, null=True)),
                ("vet_flag", models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={"verbose_name_plural": "All Tags",},
        ),
        migrations.CreateModel(
            name="OEMProvider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "manufacturer",
                    models.CharField(
                        choices=[
                            ("GE", "GE"),
                            ("RELIANCE", "RELIANCE"),
                            ("BALDOR", "BALDOR"),
                            ("CHROMALOX", "CHROMALOX"),
                            ("VA TECH ELIN", "VA TECH ELIN"),
                            ("ALSTOM", "ALSTOM"),
                            ("ABB", "ABB"),
                            ("CEMP S.P.A", "CEMP S.P.A"),
                            ("SAFT NIFE", "SAFT NIFE"),
                        ],
                        max_length=255,
                    ),
                ),
                ("contact", models.IntegerField()),
                ("mail_address", models.EmailField(max_length=254)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={"verbose_name_plural": "OEM Provider",},
        ),
        migrations.CreateModel(
            name="SMEFocal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action_owner",
                    models.CharField(
                        choices=[
                            ("pee/11 & pee/5", "PEE/11 & PEE/5"),
                            ("pma/elec & pee/5", "PMA/ELEC & PEE/5"),
                            ("pmt-ele & pma-ele", "PMT-ELE & PMA-ELE"),
                        ],
                        max_length=55,
                    ),
                ),
                ("ext", models.IntegerField()),
                ("mail_address", models.EmailField(max_length=254)),
                ("department", models.CharField(blank=True, max_length=255, null=True)),
                ("reference", models.CharField(max_length=255)),
            ],
            options={"verbose_name_plural": "SME Focal",},
        ),
        migrations.CreateModel(
            name="ObselescenceData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        choices=[
                            ("Area A-GTG", "AREA A GTG"),
                            ("Area B-Storage-Loading", "AREA B STORAGE AND LOADING"),
                            ("Area C-General-Facilities", "Area C GENERAL FACILITIES"),
                            ("Area D-Train-123", "Area D TRAIN 1, 2, 3"),
                            ("Area E-Train-456", "Area D TRAIN 4, 5, 6"),
                            ("Offplot", "OFFPLOT"),
                        ],
                        max_length=50,
                    ),
                ),
                ("description", models.TextField()),
                ("rating", models.CharField(blank=True, max_length=255, null=True)),
                ("no_of_oem_sources", models.IntegerField()),
                (
                    "stock_available_vs_consumption_rate",
                    models.CharField(
                        choices=[("low", "L"), ("medium", "M"), ("high", "H")],
                        max_length=55,
                    ),
                ),
                ("year_of_manufacture", models.DateField()),
                ("year_in_operation", models.DateField()),
                ("design_End_of_life_years", models.IntegerField()),
                ("year_to_design_end_of_life", models.IntegerField()),
                (
                    "current_status",
                    models.CharField(
                        choices=[("active", "ACTIVE"), ("obsolete", "OBSOLETE")],
                        max_length=55,
                    ),
                ),
                (
                    "probability",
                    models.CharField(
                        choices=[("low", "L"), ("medium", "M"), ("high", "H")],
                        max_length=12,
                    ),
                ),
                (
                    "operational_impact_criticality",
                    models.CharField(
                        choices=[
                            ("pc", "PC"),
                            ("sc", "SC"),
                            ("low", "NON(L)"),
                            ("none", "NONE"),
                        ],
                        max_length=55,
                    ),
                ),
                (
                    "potential_risk",
                    models.CharField(
                        choices=[
                            ("4c", "4C"),
                            ("1e", "1E"),
                            ("4d", "4D"),
                            ("2b", "2B"),
                            ("3b", "3B"),
                            ("2c", "2C"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "obsolescence_risk",
                    models.CharField(
                        choices=[("low", "L"), ("medium", "M"), ("high", "H")],
                        max_length=12,
                    ),
                ),
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("new technology", "New Technology"),
                            ("general ageing", "General Ageing"),
                            ("hse", "HSE"),
                            ("obsoleteness", "Obsoleteness"),
                            ("nr", "NR"),
                        ],
                        max_length=55,
                    ),
                ),
                ("recommended_obsolescence_strategy", models.TextField()),
                ("recommended_life_extension_strategy", models.TextField()),
                (
                    "equipment_type",
                    models.CharField(
                        choices=[
                            ("generator", "GENERATOR"),
                            ("electric motors", "ELECTRIC MOTORS"),
                            ("electric heaters", "ELECTRIC HEATERS"),
                            ("ups", "UPS"),
                            ("battery", "BATTERY"),
                            ("control panel", "CONTROL PANEL"),
                        ],
                        max_length=55,
                    ),
                ),
                ("unit", models.IntegerField()),
                (
                    "discipline",
                    models.CharField(
                        choices=[
                            ("rotating", "ROTATING"),
                            ("electrical", "ELECTRICAL"),
                            ("instrument", "INSTRUMENT"),
                        ],
                        max_length=55,
                    ),
                ),
                (
                    "area",
                    models.CharField(
                        choices=[
                            ("Area A", "AREA A"),
                            ("Area B", "AREA B"),
                            ("Area C", "Area C"),
                            ("Area D", "Area D"),
                            ("Area E", "Area D"),
                            ("Offplot", "OFFPLOT"),
                        ],
                        max_length=55,
                    ),
                ),
                (
                    "action_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="eqms.smefocal"
                    ),
                ),
                ("manufacturer", models.ManyToManyField(to="eqms.oemprovider")),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="eqms.femast"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Equpiment Obsolescence Data",},
        ),
    ]