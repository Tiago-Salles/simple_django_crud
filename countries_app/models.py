from django.db import models

class CountryManager(models.Manager):
  
  def create_country(self, country_name, language):
   country = self.create(country_name=country_name, language=language)
   return country

  def get_all_countries(self):
   countries = self.all()
   return countries
 
  def country_details(self, name):
    country = self.filter(country_name=name).first()
    return country
 
class Country(models.Model):
  country_name = models.CharField(max_length=50)
  language = models.CharField(max_length=50)
  
  manager = CountryManager()