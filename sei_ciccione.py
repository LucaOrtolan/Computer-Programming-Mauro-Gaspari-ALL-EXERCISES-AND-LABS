def forma(w,h):
    BMI=w/(h**2)
    if BMI<18.5:
        print("Underweight")
    if 18.5<BMI<24.9:
        print("Normal")
    if 25.0<BMI<29.9:
        print("Overweight")
    if 30.0<BMI<34.9:
        print("Obese I")
    if 35.0<BMI<34.9:
        print("Obese II")
    if BMI>40.0:
        print("Obese III")

w=float(input("Insert your weight:"))
h=float(input("Insert your height:"))
forma(w,h)
