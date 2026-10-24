#how we draw a plot
# x ya horizental value is a input while y ya vartical value is a output value
# now we draw a basic plot
#now we enter days of work
from matplotlib import pyplot as plt
from matplotlib.pyplot import xlabel

x=['Mon','Thu','Wed','THRUSDAY','Fri']
# now we enter sales per day
y=[20,34,25,15,5]
# now we plot a simple graph
# there is a many types of colors,linestyle,marker
plt.plot(x, y, color='red', linestyle='dashed', marker='o', label='Daily Cake Sales')

# aghar ham chiya to yaha per bi plot show karva sakty ha liken ha professionals ki tara kam karay ga
# now we make some modification in our graph
# now we enter title in the graph
plt.title("cake sale graph")
# now we enter labels .there are two type of labels xlabel,ylabel
plt.xlabel("weakend day")
plt.ylabel("sales")
#now we enter the grid .grid hamara plot ki bakend per lines bana data ha yaha diffrent type ki line style bi ha.
# ham colour bi add kar sakty ha
plt.grid(linestyle='--',color='green')
# now we  add legend function in our plot
# ya hamra plot ma iak small sa box bana da ga go ya bata ga ka iak line,spot kea reprent kar raha ha
plt.legend()
plt.show()
