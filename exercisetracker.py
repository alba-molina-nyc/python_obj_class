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
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())




