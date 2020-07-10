from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class organization(models.Model):
    company_size = [('Small',"Small Company"), ("Medium", "Medium Company"), ('Large', "Large Company")]
    types_of_industry = [
        ("Automotive industry","Automotive Industry"),
        ("Chemical industry","Chemical Industry"),
        ('Construction industry', 'Construction industry'),
        ('Dairy industry', 'Dairy industry'),
        ('Defence industry', 'Defence industry'),
        ('Electronics industry', 'Electronics industry'),
        ('Film industry', 'Film industry'),
        ('Food processing industry', 'Food processing industry'),
        ('Jewellery industry', 'Jewellery industry'),
        ('Jute industry', 'Jute industry'),
        ('Indian leather industry', 'Indian leather industry'),
        ('Printing', 'Printing'),
        ('Metallurgical industry', 'Metallurgical industry'),
        ('Mining', 'Mining'),
        ('Petroleum industry', 'Petroleum industry'),
        ('Pharmaceutical industry', 'Pharmaceutical industry'),
        ('Plastics industry', 'Plastics industry'),
        ('Pulp and paper industry', 'Pulp and paper industry'),
        ('Salt industry', 'Salt industry'), ('Software industry', 'Software industry'),
        ('Steel industry', 'Steel industry'),
        ('Indian sugar industry', 'Indian sugar industry'),
        ('Indian trucking industry', 'Indian trucking industry'),
        ('Tea Industry', 'Tea Industry'),
        ('Textile industry', 'Textile industry')]
    size = models.CharField(choices=company_size,max_length=20)
    industry_type = models.CharField(choices=types_of_industry,max_length=50)
    controls_around_infrastructure_governance_itfacilities = models.TextField()
    number_of_locations = models.IntegerField(default=0)
    employee_strength= models.IntegerField(default=0)
    vendors_and_thirdparties = models.TextField()
    legal_and_compliance_obligations = models.TextField()
    existing_certifications_and_compliance = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.industry_type+"  "+str(self.user)

