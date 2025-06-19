def circleArea(r):
    area =( 3.14 * r)
    print(f"Area = {area:.2f}")

def cleanName(to="world"):
    to=to.strip().title()
    print(f"Hello, {to} !")

# find the circle area 
radius =float(input("Enter the radius to find the circle area : "))
circleArea(radius)

# clean the name and say hello 
name = input("what is your name ? ")
cleanName(name)