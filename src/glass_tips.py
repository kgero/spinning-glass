'''
glass_tips.py

'''
import math

def main(glass_info, delta_water_cg, speed):
	'''Calculates if the glass tips at given speed.

	Args:
		glass_info : dictionary of information about glass_info
		delta_water_cg : the change in the center of gravity of the water
		speed : speed in radians per second

	Returns:
		result: 0: if glass does not tip
				1: if glass does tip
	'''

	# Calculate center of gravity (currently assume to be center of glass)
	cg_height =  glass_info['height']/2

	#Calculate the angle between the cg and the pivot edge
	angle_a = math.atan(glass_info['b_radius']/cg_height)
	angle_b = math.pi/2 - angle_a

	# Calc normal and centrifugal forces
	centrifugal_force = glass_info['total_mass'] * (speed**2) * glass_info['start_radius']
	normal_force = glass_info['total_mass'] * 9.8

	# Caclulate pivoting force
	pivot_force  = math.cos(angle_a)*centrifugal_force

	# Calculate return force
	return_force = math.cos(angle_b)*normal_force

	if pivot_force > return_force:
		return 1
	else:
		return 0