from django.contrib import admin
from import_export import resources
from .models import ObselescenceData, OEMProvider, SMEFocal, Femast


@admin.register(ObselescenceData)
class ObsolescenceDataAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_filter = ('tag',)
    
    
class ObselescenceResource(resources.ModelResource):

    class Meta:
        model = ObselescenceData
    

@admin.register(OEMProvider)
class OEMProviderAdmin(admin.ModelAdmin):
    list_display = ('manufacturer',)
    list_filter = ('manufacturer',)
    
@admin.register(SMEFocal)
class SMEFocalAdmin(admin.ModelAdmin):
    list_display = ('action_owner',)
    list_filter = ('action_owner',)
    

@admin.register(Femast)
class SMEFocalAdmin(admin.ModelAdmin):
    list_display = ('fe_key',)
    list_filter = ('fe_key',)