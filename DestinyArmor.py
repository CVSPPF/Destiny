#!/usr/bin/env/python

import Tkinter

# The function that adjusts stats returning a list of the two final stats
def AdjustStats(stat1, stat2, light0, light1):
	final1 = stat1*light1/light0
	final2 = stat2*light1/light0
	final = [final1, final2]
	return final

# Based on type of equipment it will return the value of the bonus stat from a node
# This is entirely based off of tables rather than a mathematical calculation
def BonusStat(light, type):
	if type == 1: # helm
		if light < 291:
			return 15
		elif light < 307:
			return 16
		elif light < 319:
			return 17
		else:
			return 18
			
	if type == 2: # gloves
		if light < 287:
			return 13
		elif light < 305:
			return 14
		elif light < 319:
			return 15
		else:
			return 16
			
	if type == 3: # chest
		if light < 287:
			return 20
		elif light < 299:
			return 21
		elif light < 310:
			return 22
		elif light < 319:
			return 23
		else:
			return 24
			
	if type == 4: # boots
		if light < 284:
			return 18
		elif light < 298:
			return 19
		elif light < 309:
			return 20
		elif light < 319:
			return 21
		else:
			return 22
			
	if type == 5: # class
		if light < 295:
			return 8
		elif light < 319:
			return 9
		else:
			return 10
			
	if type == 6: # artifact
		if light < 287:
			return 34
		elif light < 295:
			return 35
		elif light < 302:
			return 36
		elif light < 308:
			return 37
		elif light < 314:
			return 38
		elif light < 319:
			return 39
		else:
			return 40
			
	if type == 7: # ghost
		if light < 295:
			return 8
		elif light < 319:
			return 9
		else:
			return 10
	



# Get the whole thing started
top = Tkinter.Tk()

# This lets people know I made it.  If you want to modify it and make it better please do
# but also keep this in because it would be a nice thing to do. I have no recourse, but
# I am a nice guy who is just trying to help us Guardians out.
me = Tkinter.StringVar()
melabel = Tkinter.Label(top, textvariable = me)
me.set("Originally created by CVSPPF")
melabel.pack()

# Get labels with boxes to enter the attributes and pack them
label1 = Tkinter.StringVar()
lightlevellabel = Tkinter.Label(top, textvariable = label1)
label1.set("Enter current Light Level")
lightlevellabel.pack()

lightlevel0 = Tkinter.Entry(top, bd = 10)
lightlevel0.pack()

label2 = Tkinter.StringVar()
finallevellabel = Tkinter.Label(top, textvariable = label2)
label2.set("Enter final Light Level")
finallevellabel.pack()

lightlevel1 = Tkinter.Entry(top, bd = 10)
lightlevel1.pack()


label3 = Tkinter.StringVar()
stat1label = Tkinter.Label(top, textvariable = label3)
label3.set("Enter current first base stat")
stat1label.pack()


stat1level = Tkinter.Entry(top, bd = 10)
stat1level.pack()

label4 = Tkinter.StringVar()
stat2label = Tkinter.Label(top, textvariable = label4)
label4.set("Enter current second base stat")
stat2label.pack()


stat2level = Tkinter.Entry(top, bd = 10)
stat2level.pack()

label5 = Tkinter.StringVar()
typelabel = Tkinter.Label(top, textvariable = label5)
label5.set("Pick type of equipment")
typelabel.pack()

answer = Tkinter.StringVar()
answerlabel = Tkinter.Label(top, textvariable = answer)
answer.set("Not calculated yet")

answer2 = Tkinter.StringVar()
answer2label = Tkinter.Label(top, textvariable = answer2)
answer2.set("Not calculated yet")

type = Tkinter.IntVar()

def Calculate():
    a = float(stat1level.get())
    b = float(stat2level.get())
    c = float(lightlevel0.get())
    d = float(lightlevel1.get())
    e = int(type.get())
    bonus = BonusStat(d, e)
    adjusted = AdjustStats(a, b, c, d)
    answer.set(
    	"Final stats are:\n Stat1: %f\n Stat2: %f\n Bonus stat: %d"
    	% (adjusted[0], adjusted[1], bonus))
    answer2.set(
        "Final total stat value is %f" % (adjusted[0] + adjusted[1] + bonus))

# make radiobuttons corresponding to type of armor
# when clicked they Calculate() based off of what is in the boxes at the time

R1 = Tkinter.Radiobutton(top, text = "Helm", variable = type, value = 1,
                          command = Calculate)
R2 = Tkinter.Radiobutton(top, text = "Gloves", variable = type, value = 2,
						  command = Calculate)
R3 = Tkinter.Radiobutton(top, text = "Chest", variable = type, value = 3,
						  command = Calculate)
R4 = Tkinter.Radiobutton(top, text = "Boots", variable = type, value = 4,
						  command = Calculate)
R5 = Tkinter.Radiobutton(top, text = "Class", variable = type, value = 5,
						  command = Calculate)
R6 = Tkinter.Radiobutton(top, text = "Artifact", variable = type, value = 6,
						  command = Calculate)
R7 = Tkinter.Radiobutton(top, text = "Ghost", variable = type, value = 7,
						  command = Calculate)

R1.pack(side=Tkinter.LEFT)
R2.pack(side=Tkinter.LEFT)
R3.pack(side=Tkinter.LEFT)
R4.pack(side=Tkinter.LEFT)
R5.pack(side=Tkinter.LEFT)
R6.pack(side=Tkinter.LEFT)
R7.pack(side=Tkinter.LEFT)


answerlabel.pack(side = Tkinter.TOP)
answer2label.pack(side = Tkinter.TOP)
top.mainloop()