'''glass_slides.py
Description: (will determine if, at the given speed, the glass will slide on the table)
Args: glass_info, speed
Return: slides(0/1)
'''
import math.pi as pi

def main(glass_info,speed):
	'''Calculates if the glass slides at given speed.

	 Args:
	 	glass_info : dictionary of information about glass_info
	 	speed : speed in radians per second

	 Returns:
	 	result: 0: if glass does not slide
	 			1: if glass does slide
	 '''

	 # Calulate the mass of the glass and water
	 inside_glass_vol = (1/3)*pi*(b_radius**2 + b_radius*t_radius + t_radius**2)*height
	 outside_glass_vol = (1/3)*pi*((b_radius+thickness)**2
	 					+ (b_radius+thickness)*(t_radius+thickness) 
	 					+ (t_radius+thickness)**2)*height
	 glass_vol = outside_glass_vol - inside_glass_vol 	# m^3
	 water_vol = inside_glass_vol * percent_full 		# m^3
	 mass_glass = density * glass_vol 					# kg
	 mass_water = 1000 * water_vol 						# kg
	 total_mass = mass_glass + mass_water

	 # Calculate the centrifugal force at the give speed
	 # M * w^2 * r
	 centrifugal_force = total_mass * (speed**2) * start_radius # N
	 normal_force = total_mass * 9.8							# N

	 if centrifugal_force > normal_force * c_f:
	 	return 1
	 else:
	 	return 0
