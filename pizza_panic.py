from livewires import games,color
import pygame

import random
pygame.display.set_mode((640,480))

class Chef(games.Sprite):
	'''
	a chef which moves left and right, dropping pizzas.
	'''
	image = games.load_image('chef.bmp')

	def __init__(self,y =55,speed=2,odds_change=200):
		super(Chef,self).__init__(image=Chef.image,
		x = games.screen.width/2,
		y = y,
		dx = speed)

		self.odds_change = odds_change
		self.time_til_drop =0
	
	def update(self):
		'''
		determine if direction needs to be reversed 
		'''
		if self.left <0 or self.right >games.screen.width:
			self.dx = - self.dx
		elif random.randrange(self.odds_change) ==0:
			self.dx = -self.dx
		self.check_drop()
	
	def check_drop(self):
		'''
		decrease countdown or drop pizza and reset countdown
		'''
		if self.time_til_drop >0:
			self.time_til_drop -=1
		else:
			new_pizza = Pizza(x=self.x)
			games.screen.add(new_pizza)

			self.time_til_drop = int(new_pizza.height * 1.3/Pizza.speed) + 1

class Pizza(games.Sprite):
	''' a pizza which falls to the ground 
	'''
	image = games.load_image('pizza.bmp')
	speed =1 
	def __init__(self,x ,y =90):
		super(Pizza,self).__init__(image=Pizza.image,
		x=x,y=y,
		dy = Pizza.speed)

	def handle_collide(self):
		''' move to a random screen location'''
		self.x = random.randrange(games.screen.width)
		self.y = random.randrange(games.screen.height)

	def update(self):
		''' check if bottom edge has reached screen bottom '''
		if self.bottom > games.screen.height:
			self.end_game()
			self.destroy()
	
	def handle_caught(self):
		self.destroy()
	def end_game(self):
		end_message = games.Message(value='Game over',
		size =90,
		color = color.red,
		x = games.screen.width//2,
		y = games.screen.height//2,
		lifetime = 5 * games.screen.fps,
		after_death = games.screen.quit)
		games.screen.add(end_message)

class Pan(games.Sprite):
	'''
	a pan controlled by player to catch falling pizzas
	'''
	image = games.load_image('pan.bmp')
	def __init__(self):
		super(Pan,self).__init__(image=Pan.image,x = games.mouse.x,bottom = games.screen.height)

		self.score = games.Text(value=0,size=25,color=color.black,top = 5,right=games.screen.width -10)
		games.screen.add(self.score)

	def update(self):
		''' move to mouse coordinates '''
		self.x = games.mouse.x
		if self.left <0:
			self.left =0
		if self.right > games.screen.width:
			self.right = games.screen.width
		
		self.check_catch()
		#self.y = games.mouse.y
		#self.check_collide()
	
	def check_collide(self):
		''' check for collision with pizza'''
		for pizza in self.overlapping_sprites:
			pizza.handle_collide()
	def check_catch(self):
		''' check if catch pizzas'''

		for pizza in self.overlapping_sprites:
			self.score.value += 10
			self.score.right = games.screen.width -10
			pizza.handle_caught()

def main():
	games.init(screen_width=640,screen_height=480,fps=50)
	
	wall_image = games.load_image('wall.jpg',transparent=False)
	games.screen.background = wall_image
	
	the_chef = Chef()
	games.screen.add(the_chef)

	#pizza_image = games.load_image('pizza.bmp')
	#pizza_x = random.randrange(games.screen.width)
	#pizza_y = random.randrange(games.screen.height)
	#the_pizza = Pizza(image = pizza_image, x= pizza_x,y = pizza_y)
	#games.screen.add(the_pizza)

	#pan_image = games.load_image('pan.bmp')
	#the_pan = Pan(image=pan_image,
	#x=games.mouse.x,
	#y = games.mouse.y)
	the_pan = Pan()
	games.screen.add(the_pan)
	games.mouse.is_visible = False

	games.screen.event_grab = True

	games.screen.mainloop()


main()
