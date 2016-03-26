'''glass_slides.py
Description: (will determine if, at the given speed, the glass will slide on the table)
Args: glass_info, speed
Return: slides(0/1)
'''

def main(glass_info,speed):
	'''Calculates if the glass slides at given speed.

	 Args:
	 	glass_info : dictionary of information about glass_info
	 	speed : speed in radians per second

	 Returns:
	 	result: 0: if glass does not slide
	 			1: if glass does slide
	 '''

	 # Calculate the centrifugal force at the give speed
	 # M * w^2 * r
	centrifugal_force = glass_info['total_mass'] * (speed**2) * glass_info['start_radius']
	normal_force = glass_info['total_mass'] * 9.8

	if centrifugal_force > normal_force * glass_info['c_f']:
		return 1
	else:
		return 0
