print("---Py-Fest 2026 stage manager!---")
print("1.view lineup & Total time")
print("2.add new band ")
print("3.move first band to the end")
print("4.remove band by name")
print("5.move band to a specific position")
print("6.exit")
choice = input("select an option (1-6) ")
line_up = [
    ("code Play", "indie", 30),
    ("the pythonistas", "rock", 45),
    ("syntax erorr", "Metal", 60),
    ]

while True:
    time = sum(band[2] for band in line_up)
    choice = input("select an option (1-6) ")
    if choice == "1":
        print(line_up)
        print(f"total time is {time}")
        choice = input("select an option (1-6) ")
    elif choice == "2":
        name = input("enter the name of the band you want to add")
        genera = input("enter the genre of band you want to add")
        time = int(input("Enter the time of your band that you are adding"))
        new = (name, genera, time)
        line_up.append(new)
        choice = input("select an option (1-6) ")
    elif choice == "3":
        moved = line_up.pop
        line_up.append(moved)

