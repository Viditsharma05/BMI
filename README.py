# BMI
# <!-- It will tell us the BMI after entering all the necessary data using def function in python. -->


def bodymassindex(weight,height):
  return round((weight/height**2),2)
print("Your BMI Calculator Welcomes you")
w=float(input("Enter your Weight in kg:-"))
# n=int(input("Enter 1 for height in metres, 2 for height in h'h'' "))
h=float(input("Enter your height in metres:-"))
bmi=bodymassindex(w,h)
print("Your body mass index is:-",bmi)



if bmi<18.5:
  print("Underweight")
elif 18.5<bmi<=24.9:
  print("Healthy weight")
elif 25<bmi<29.9:
  print("Overweight")
else:
  print("You are obese")
