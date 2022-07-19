class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
        

#Write your code here!

artist_1 = Artist('Taylor Swift', 'Big Machine Records, LLC')
artist_2 = Artist('Up We Go', 'Warner Bros. Records Inc.')

song_1 = Song('You Belong with Me', 'Fearless', '2008', artist_1.name)
song_2 = Song('All Too Well', 'Red', '2012', artist_1.name)
song_3 = Song('Up We Go', 'Midnight Machines', '2016', artist_2.name)

#Feel free to add code to test your code below.




# Instances as Arguments (5.1.5.3)


#Below are the two class definitions we supplied previously:
#Artist and Song.
#
#Write a function called "get_song_string". It should accept
#one argument which will be a Song object. It should return
#a string in the following format:
#
# "<song name>" - <artist name> (<song year>)
# e.g: 
# "You Belong With Me" - Taylor Swift (2008)
#
#The quotation marks around the song title should be *part*
#of the string.
#
#Hint: You're writing a function, not a method. That means
#the function get_song_string should not be inside either
#of these classes.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist


        

def get_song_string(song):
    
    new_song = str(song.name) + ' - ' + str(song.artist.name) + ' - ' + ' (' + str(song.year) + ') '
    print(new_song)
    return new_song


#song.name 
    #song.artist
    #song.year


#new_song = Song.name + '-' + Song.artist + '-' + Song.year


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "You Belong With Me" -Taylor Swift (2008)
new_artist = Artist("Taylor Swift", "Big Machine Records, LLC")
new_song = Song("You Belong With Me", "Fearless", 2008, new_artist)
print(get_song_string(new_song))




# Making Actual Copies (5.1.5.4)
class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
myPerson2 = myPerson1
myPerson2.eyecolor = "blue"
print("myPerson1's eyecolor: " + myPerson1.eyecolor)
print("myPerson2's eyecolor: " + myPerson2.eyecolor)


