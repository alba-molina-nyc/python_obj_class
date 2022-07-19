#Imagine you're writing an exercise-tracking app like Fitbit
#or MyFitnessPal. Part of your app is that a user can log an
#exercise session by naming the exercise, the intensity, and
#the duration.

#Write a class called ExerciseSession. 
# ExerciseSession should have a constructor that requires two strings and an integer: the strings represent the exercise name and the
#exercise intensity, which will be "Low", "Moderate", or "High". The integer will represent the length of the exercise session in minutes. 
# These should be saved in the instance of the class.
class ExerciseSession:
    def __init__(self, exercise_name, intensity, duration):
        self.exercise_name = exercise_name
        self.intensity = intensity
        self.duration = duration
   
    def get_exercise(self):
        exercise_name = self.exercise_name
        
        return exercise_name
    
  
    def get_intensity(self):
        intensity = self.intensity 
        return intensity

    
    def get_duration(self):
        duration = self.get_duration  
        return duration
    
    
    def set_exercise(self, new_exercise_name):
       print("EXERCISE changed from", self.exercise_name, "to", new_exercise_name, 'line59')
       self.exercise_name = new_exercise_name
        
    def set_intensity(self, new_intensity):
       print("INTENSITY changed from", self.intensity, "to",  new_intensity, 'line63')
       self.intensity =  new_intensity
        
           
    def set_duration(self, new_duration):
       print("DURATION changed from", self.duration, "to", new_duration, 'line59')
       self.duration = new_duration
        










#The setters should be named set_exercise, set_intensity, and set_duration. Each should have one parameter (besides self), which should be stored as the new value of exercise, intensity, or duration. You may assume only
#valid values will be passed in.
#
#HINT: You don't have to do any logging like you saw inthe video! That was just an example of one benefit of using getters and setters, but this problem does not ask you to do that.


#Add your code here!
#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#Running
#Low
#60
#Swimming
#High
#30

# -----------------------
# new_exercise = ExerciseSession("Running", "Low", 60)
# print(new_exercise.get_exercise())
# print(new_exercise.get_intensity())
# print(new_exercise.get_duration())
# new_exercise.set_exercise("Swimming")
# new_exercise.set_intensity("High")
# new_exercise.set_duration(30)
# print(new_exercise.get_exercise())
# print(new_exercise.get_intensity())
# print(new_exercise.get_duration())





#Previously, you wrote a class called ExerciseSession that
#had three attributes: an exercise name, an intensity, and a
#duration.
#
#Add a new method to that class called calories_burned.
#calories_burned should have no parameters (besides self, as
#every method in a class has). It should return an integer
#representing the number of calories burned according to the
#following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Medium", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
#You may copy your class from the previous exercise and just
#add to it.


#Add your code here!



#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#240
#360
class ExerciseSession:      
    def __init__(self, exercise_name, intensity, duration):
        self.exercise_name = exercise_name
        self.intensity = intensity
        self.duration = duration
   
    def get_exercise(self):
        exercise_name = self.exercise_name
        
        return exercise_name
    
  
    def get_intensity(self):
        intensity = self.intensity 
        return intensity

    
    def get_duration(self):
        duration = self.get_duration  
        return duration
    
    
    def set_exercise(self, new_exercise_name):
       self.exercise_name = new_exercise_name
        
    def set_intensity(self, new_intensity):
       self.intensity =  new_intensity
        
           
    def set_duration(self, new_duration):
       self.duration = new_duration
   

    def calories_burned(self):
        calories_burned = 0
        if self.intensity is "Low":
            calories_burned = min * 4
        elif self.intensity is "Med":
            calories_burned = min * 8
        elif self.intensity is "High":
            calories_burned = min * 12
   
        return calories_burned
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())

#   def set_calories_burned(self, new_duration):
#         self.duration = new_duration
#     def get_calories_burned(self):
#         calories_burned = 0
#         if self.intensity is "Low":
#             calories_burned = self.duration * 4
#         if self.intensity is "Med":
#             calories_burned = self.duration * 8
#         elif self.intensity is "High":
#             calories_burned = self.duration * 12
#         return calories_burned






