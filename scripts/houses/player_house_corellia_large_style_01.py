import sys
from services.housing import HouseTemplate
from engine.resources.scene import Point3D

def setup(housingTemplates):
	houseTemplate = HouseTemplate("object/tangible/deed/player_house_deed/shared_corellia_house_large_deed.iff", "object/building/player/shared_player_house_corellia_large_style_01.iff", 2)
	
	houseTemplate.addBuildingSign("object/tangible/sign/player/shared_house_address.iff", Point3D(float(6), float(3), float(13.4)))
	houseTemplate.addPlaceablePlanet("corellia")
	houseTemplate.addPlaceablePlanet("talus")
	houseTemplate.setDefaultItemLimit(500)
	houseTemplate.setBaseMaintenanceRate(26)
	
	housingTemplates.put(houseTemplate.getDeedTemplate(), houseTemplate)
	return