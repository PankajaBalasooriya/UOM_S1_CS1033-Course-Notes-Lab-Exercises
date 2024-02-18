#Read the angles from the user
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

angle_sum = angle1 + angle2 + angle3

#check angles form a triangle
if angle_sum == 180 and (angle1 != 0 and angle2 != 0 and angle3 != 0):
    #check the type of the triangle
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Right angled")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Obtuse angled")
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("Acute angled")
else:
    print("Angles do not form a triangle")