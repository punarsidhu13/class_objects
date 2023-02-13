#first example

class human:
    eyes=2
    arms=2
    def speak(self):
        print("i can speak")


punar = human()
punar.speak()

print(human.arms)

human.speak(punar)
 
#Second Example

class mountains():
    peaks = "many"
    trees = "too many"
    def scene(self):
        print("very scenic")

everest = mountains()

everest.scene()

print(mountains.peaks)
print(mountains.trees)
mountains.scene(everest)


# Third Example

class building():
    rooms = 8
    windows = 14
    def accomodate(self):
        print("place To-Let available")

netsolutions = building()

print(building.windows) 
netsolutions.accomodate()
building.accomodate(netsolutions)
print(building.rooms)


# Fourth Example

class football():
    teams =2 
    players_team1=11

    def goals(self):
        print("GOAAALLLLL!!!!")

messi = football()
ronaldo = football()


ronaldo.goals()
messi.goals()

print(football.teams)
print(football.players_team1)

football.goals(messi)


# Fifth Example'

class planets():
    planets = 8
    orbit= "elliptical"
    def solarsys(self):
        print("All planets revolve around the sun")
earth= planets()

print(planets.planets)
print(planets.orbit)
planets.solarsys(earth)
earth.solarsys()




