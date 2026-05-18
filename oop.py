DAY 1

#creating class 
class student:
  name="Rajesh G R"
#creating objects 
s1=student()
  print(s1.name)

class car:
  color="black"
  brand="merrcedes"
#this is objects
car1=car()#constructor
print(car1.color)
print(car1.brand)
#output 


#_ _init_ _ Function
#creating class
class student:
  def _ _init_ _(self,fullname):
  self.name=fullname
#self parameter is a reference to the current instance of the class and is used to access variablesthat belongs to the class
#creating object
s1=student("rajesh")
print(s1.name)
