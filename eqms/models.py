from django.db import models



class Femast(models.Model):
    f_id = models.IntegerField(primary_key=True, unique=True, blank=True) #db_column='ID',
    fe_type = models.CharField(max_length=50, blank=True, null=True)
    fe_key = models.CharField(max_length=50, unique=True, blank=True, null=True) #db_column='FE_KEY',
    fe_desc = models.CharField(max_length=200, blank=True, null=True)
    vet_flag = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        # managed = False  
        # db_table = 'r_femast'
        verbose_name_plural = 'All Tags'

    def __str__(self):
        return self.fe_key


class ObselescenceData(models.Model):
    
    ASSET_CHOICES = (
        ('Area A-GTG', 'AREA A GTG'),
        ('Area B-Storage-Loading', 'AREA B STORAGE AND LOADING'),
        ('Area C-General-Facilities', 'Area C GENERAL FACILITIES'),
        ('Area D-Train-123', 'Area D TRAIN 1, 2, 3'),
        ('Area E-Train-456', 'Area D TRAIN 4, 5, 6'),
        ('Offplot', 'OFFPLOT')
    )
    
    STOCK_CHOICES = (
        ('low', 'L'),
        ('medium', 'M'),
        ('high', 'H')   
    )
    
    STATUS_CHOICES = (
        ('active', 'ACTIVE'),
        ('obsolete', 'OBSOLETE')
    )
    
    IMPACT_CHOICES = (
        ('pc', 'PC'),
        ('sc', 'SC'),
        ('low', 'NON(L)'),
        ('none', 'NONE')
    )
    
    RISK_CHOICES = (
        ('4c', '4C'),
        ('1e', '1E'),
        ('4d', '4D'),
        ('2b', '2B'),
        ('3b', '3B'),
        ('2c', '2C'),
        
    )
    
    REASON_CHOICES = (
        ('new technology', 'New Technology'),
        ('general ageing', 'General Ageing'),
        ('hse', 'HSE'),
        ('obsoleteness', 'Obsoleteness'),
        ('nr', 'NR')
    )
    
    EQUIPMENT_CHOICES = (
        ('generator', 'GENERATOR'),
        ('electric motors', 'ELECTRIC MOTORS'),
        ('electric heaters', 'ELECTRIC HEATERS'),
        ('ups', 'UPS'),
        ('battery', 'BATTERY'),
        ('control panel', 'CONTROL PANEL')
    )
    
    DISCIPLINE_CHOICES = (
        ('rotating', 'ROTATING'),
        ('electrical', 'ELECTRICAL'),
        ('instrument', 'INSTRUMENT')
    )
    
    AREA_CHOICES = (
        ('Area A', 'AREA A'),
        ('Area B', 'AREA B'),
        ('Area C', 'Area C'),
        ('Area D', 'Area D'),
        ('Area E', 'Area D'),
        ('Offplot', 'OFFPLOT')
    )
    
    location = models.CharField(max_length=50, choices=ASSET_CHOICES)
    tag = models.ForeignKey(Femast, on_delete=models.DO_NOTHING)
    description = models.TextField()
    rating = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.ManyToManyField('OEMProvider')
    serial_number = models.CharField(max_length=255)
    no_of_oem_sources = models.IntegerField()
    stock_available_vs_consumption_rate = models.CharField(max_length=55, choices=STOCK_CHOICES)
    year_of_manufacture = models.DateField()
    year_in_operation = models.DateField()
    design_End_of_life_years = models.IntegerField()
    year_to_design_end_of_life = models.IntegerField()
    current_status = models.CharField(max_length=55, choices=STATUS_CHOICES)
    probability = models.CharField(max_length=12, choices=STOCK_CHOICES)
    operational_impact_criticality = models.CharField(max_length=55, choices=IMPACT_CHOICES)
    potential_risk = models.CharField(max_length=5, choices=RISK_CHOICES)
    obsolescence_risk = models.CharField(max_length=12, choices=STOCK_CHOICES)
    reason = models.CharField(max_length=55, choices=REASON_CHOICES)
    recommended_obsolescence_strategy = models.TextField()
    recommended_life_extension_strategy = models.TextField()
    action_owner = models.ForeignKey('SMEFocal', on_delete=models.PROTECT)
    equipment_type = models.CharField(max_length=55, choices=EQUIPMENT_CHOICES)
    unit = models.IntegerField()
    discipline = models.CharField(max_length=55, choices=DISCIPLINE_CHOICES)
    area = models.CharField(max_length=55, choices=AREA_CHOICES)
    
    
    class Meta:
        verbose_name_plural = 'Equpiment Obsolescence Data'

    def __str__(self):
        return self.description
    


class OEMProvider(models.Model):
    
    OEM_CHOICES = (
        ('GE', 'GE'),
        ('RELIANCE', 'RELIANCE'),
        ('BALDOR', 'BALDOR'),
        ('CHROMALOX', 'CHROMALOX'),
        ('VA TECH ELIN', 'VA TECH ELIN'),
        ('ALSTOM', 'ALSTOM'),
        ('ABB', 'ABB'),
        ('CEMP S.P.A', 'CEMP S.P.A'),
        ('SAFT NIFE', 'SAFT NIFE')
    )
    
    manufacturer = models.CharField(max_length=255, choices=OEM_CHOICES)
    contact = models.IntegerField()
    mail_address = models.EmailField()
    location = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'OEM Provider'

    def __str__(self):
        return self.manufacturer


class SMEFocal(models.Model):
    
    OWNER_CHOICES = (
        ('pee/11 & pee/5', 'PEE/11 & PEE/5'),
        ('pma/elec & pee/5', 'PMA/ELEC & PEE/5'),
        ('pmt-ele & pma-ele', 'PMT-ELE & PMA-ELE')
    )
    
    action_owner = models.CharField(max_length=55, choices=OWNER_CHOICES)
    ext = models.IntegerField()
    mail_address = models.EmailField()
    department = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'SME Focal'

    def __str__(self):
        return self.action_owner