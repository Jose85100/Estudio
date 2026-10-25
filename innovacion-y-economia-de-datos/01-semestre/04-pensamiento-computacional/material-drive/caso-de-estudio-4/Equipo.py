import random

names = ['Real madrid', 'Barcelona',
'Manchester United','Juventus','Ac milan',
'Inter de Milan','Bayer Munich','Arsenal',
'Borussia Dortmund','Chelsea','Liverpool',
'Manchester city','Paris Saint-Germain',
'Valencia','Sevilla','As Roma', 'Tottenham',
'Everton', 'As monaco', 'Nápoles']
def selectRandom(names):
  return random.choice(names)

print("The name selected is: ", selectRandom(names))
