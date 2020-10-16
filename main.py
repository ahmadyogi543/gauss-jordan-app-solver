"""
import tkinter
from random import randint

root = tkinter.Tk()
root.title("Love Calculator")

def create_label(text, row, column):
	label = tkinter.Label(root,text = text)
	#label.pack()
	label.grid(row = row, column = column)
	return label

def create_entry(row, column):
	entry = tkinter.Entry(root)
	entry.grid(row = row, column = column)
	return entry

def calculating():
	#ynl is the length of your name and cnl is the length of your crush name
	#To determine if you and your crush is a match, we have the variable res which is hold the value of
	#ynl + cnl and then multiplying it with a random number from 1 to 10
	#and then we're going to check if res is an even number, it's a match and if is an odd number, then no :(
	#So because we are trying to add length of you and your crush name, we are going determine the posibilities
	#let say ynl and cnl are even number, and then if an even number add by also an even number, the result will also be an even number
	#And then we are going to multiply our sum to a random number from 0 to 10
	#There is 5 posibilities of multiplying the sum by an even number and also 5 posilibities of multiplying it by an odd number.
	#even: 5/10 odd: 5/10
	ynl = len(your_entry.get())
	cnl = len(crush_entry.get())
	res = (ynl + cnl)*randint(0,10)
	if res % 2 == 0:
		result["text"] = "result: Yes, you guys a cool couple"
	else:
		result["text"] = "result: Sorry, you guys are not going together :("

def clean():
	pass

#Label
your_name = create_label("Your name:", 0, 0)
crush_name = create_label("Your crush name:", 1, 0)
result = create_label("result: ",2, 0)

#Entry
your_entry = create_entry(0, 1)
crush_entry = create_entry(1, 1)

#Calculate
calculate = tkinter.Button(root, text = "Calculate", command = calculating)
calculate.grid(row = 2,  column = 1)
root.mainloop()

"""
import tkinter

root = tkinter.Tk()
root.title("Gaus-Jordan Elimination")

def create_label(text,row,column):
	label = tkinter.Label(root, text = text)
	label.grid(row = row,column = column)
	return label

def create_entry(row,column):
	entry = tkinter.Entry(root)
	entry.grid(row = row,column = column)
	return entry

def create_button(text,row,column, command):
	button = tkinter.Button(root, text = text, command = command)
	button.grid(row = row, column = column)
	return button

#ax + bx = c
class Equation:
	def __init__(self,row):
		self.entry_a = create_entry(row,0)
		self.entry_b = create_entry(row,1)
		self.entry_c = create_entry(row,2)

	def get_values(self):
		a = int(self.entry_a.get())
		b = int(self.entry_b.get())
		c = int(self.entry_c.get())
		return [a,b,c]

	def get_entries(self):
		return [self.entry_a,self.entry_b,self.entry_c]

#masih belum bisa pivot 0(belum bisa swap)
#masih perlu dicek
def eliminating(column,eq1,eq2):
	cmpd = []
	if eq1[column] != eq2[column]:
		scl_eq1 = eq1[column]
		scl_eq2 = eq2[column]
		for i in range(len(eq1)):
			if eq1[i]*eq2[i] > 0 or eq1[i]*eq2[i] < 0:
				cmpd.append(-scl_eq2*eq1[i] + scl_eq1*eq2[i])
			else:
				cmpd.append(scl_eq2*eq1[i] + scl_eq1*eq2[i])
		return cmpd
	else:
		for i in range(len(eq1)):
			if eq1[i]*eq2[i] > 0 or eq1[i]*eq2[i] < 0:
				cmpd.append(-eq1[i] + eq2[i])
			else:
				cmpd.append(eq1[i] + eq2[i])
		return cmpd

def make_pivot(column,eq):
	pivot_coef = eq[column]
	if pivot_coef != 0:
		for i in range(len(eq)):
			eq[i] /= pivot_coef

def put_on_the_screen(eq_ori, eq_new):
	for i in range(len(eq_ori)):
		eq_ori[i].delete(0,tkinter.END)
		eq_ori[i].insert(0, eq_new[i])

def reseting():
	for entry in eq_one.get_entries():
		entry.delete(0, tkinter.END)
	for entry in eq_two.get_entries():
		entry.delete(0, tkinter.END)

def exiting():
	pass

def gj_eliminate():
	e1 = eq_one.get_values()
	e2 = eq_two.get_values()

	e2 = eliminating(0,e1,e2)
	e1 = eliminating(1,e2,e1)
	make_pivot(0,e1)
	make_pivot(1,e2)

	eo = eq_one.get_entries()
	put_on_the_screen(eo,e1)
	et = eq_two.get_entries()
	put_on_the_screen(et,e2)
	

#main program
eq_one = Equation(0)
eq_two = Equation(1)

reset = create_button("Reset", 3, 0, reseting)
eliminate = create_button("Eliminate", 3,1, gj_eliminate)
exit = create_button("Exit", 3, 2, exiting)

root.mainloop()

