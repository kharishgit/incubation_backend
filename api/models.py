from django.db import models

# Create your models here.

class RegisterCompany(models.Model):
    name            = models.CharField(max_length=20)
    address         = models.CharField(max_length=30)
    city            = models.CharField(max_length=20)
    email           = models.EmailField(max_length=50)
    # phone           = models.IntegerField()
    company_name    = models.CharField(max_length=30)
    describe_your_team_and_background   = models.CharField(max_length=100)
    describe_your_company_and_product   = models.CharField(max_length=100)
    what_is_unique_about_your_solution  = models.CharField(max_length=100)
    what_is_your_value_proposition_for_the_customer  = models.CharField(max_length=100)
    who_are_your_competetitors_and_what_is_your_competative_advantage = models.CharField(max_length=100)
    explain_your_revenue_model = models.CharField(max_length=100)
    what_is_the_potential_market_size_of_the_product = models.CharField(max_length=100)
    how_do_you_market = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Booking(models.Model):
    time = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    section = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    company = models.ForeignKey(RegisterCompany, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.date


