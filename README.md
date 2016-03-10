Spinning Glass Calc / Sim
=========================

The goal of this project is to create a tool for solving the following problem:

You have a glass of water on revolving tray, such as a lazy Susan. The tray slowly
begins to rotate. As the tray rotates faster and faster, what happens first?
1. The glass slides off the tray
2. The glass tips over
3. The water in the glass is flung out of the glass (without the glass falling over)

(acceleration is slow. assume steady state)

File Structure
-data.py (store the physical variables)
	Args: None
	Return: None

-main.py (will run the simulation, increaseing spinning speed until failture)
	Args: glass size, amount of water, distance from center, friction
	Return: what failed, at what speed

-glass_slides.py (calc force on glass, is it enough to slide?)
	Args: physical variables, speed
	Return: slide?(T/F)

-water_shape.py (where the water is in the glass, where the CG of the water is, does it reach the brim?)
	Args: physical variables, speed
	Return: brim?(T/F), delta_water_CG

-glass_tips.py (moment on glass (given water CG), enough to tip?)
	Args: physical variables, speed, delta_water_CG
	Return: tips?(T/F)

Physical Variables
- Volume of water
- Height of glass
- Bottom radius of glass
- Top radius of glass
- Thickness of glass
- Glass density
- Cf of friction
- Distance from center of rotating tray
