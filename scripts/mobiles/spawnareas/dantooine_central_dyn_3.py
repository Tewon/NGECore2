# Spawn Area file created with PSWG Planetary Spawn Tool
import sys
from java.util import Vector

def addSpawnArea(core):
	dynamicGroups = Vector()
	dynamicGroups.add('mokk_group_1')
	dynamicGroups.add('bol_group_1')
	dynamicGroups.add('piket_longhorn_group_1')
	dynamicGroups.add('huurton_group_2')
	core.spawnService.addDynamicSpawnArea(dynamicGroups, -1320, -3981, 1843, 'dantooine')
	return
