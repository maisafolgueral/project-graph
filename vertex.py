'''
NOME - TIA
Filipe Costa Pereira - 32106521
Guilherme Guimarães Chiarelli - 32036647
Maisa Folgueral - 32121385

This file implements vertex class.
It is used to store all vertex data.

History
Date: 2023-09-21
Author: Filipe, Guilherme
Description: Added fields

Date: 2023-10-11
Author: Filipe, Maisa
Description: Added more fields
'''

class Vertex:

  def __init__(self, name, iso_code, population, area, population_density, coastline, gdp):
    self.name = name # country name
    self.iso_code = iso_code # ISO 3166 country codes
    self.population = population
    self.area = area
    self.population_density = population_density
    self.coastline = coastline
    self.gdp = gdp # PIB