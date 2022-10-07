class dog:
	"""A simple class to model a dog"""

	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age
	
	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(f"\n{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate a dog rolling over in response to a command"""
		print(f"\n{self.name} rolled over!")


my_dog = dog('Steven', 6)
your_dog = dog('Putti', 2)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

my_dog.sit()
your_dog.roll_over()


