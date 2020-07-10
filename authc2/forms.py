from django import forms
from .models import organization

class OrganizationEnterForm(forms.ModelForm):
    class Meta:
        model=organization
        fields=['size',
    'industry_type' ,
    'controls_around_infrastructure_governance_itfacilities',
    'number_of_locations',
    'employee_strength',
    'vendors_and_thirdparties',
    'legal_and_compliance_obligations',
    'existing_certifications_and_compliance',
    ]