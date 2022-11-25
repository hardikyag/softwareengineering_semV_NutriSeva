print("\n----Welcome to NutriSeva----\n")
print("For which meal do you want to donate:")
print("Enter 1 for breakfast")
print("Enter 2 for lunch")
print("Enter 3 for dinner")

#get user input on the type of meal he/she wants to donote for
mealtype = int(input())

#depending on the meal type giving options to the user
if mealtype == 1:
    #breakfast
    print("Enter the number of people 'Pooha' can feed:")
    pooham = int(input())
    print("Enter the number of people 'Upma' can feed:")
    upmam = int(input())
    print("Enter the number of people 'Aloo Paratha' can feed:")
    alooparatham = int(input())
    print("Enter the number of people 'Cheela' can feed:")
    cheelam = int(input())

    if pooham>0 and upmam>3 and alooparatham>2 and cheelam>0:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Seva Sahayog Foundation"
              "\n2.ASK - Anandi seva kendra"
              "\n3.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mayank Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 3:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    elif pooham>6 and upmam>=4 and alooparatham>0 and cheelam>0:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Seva Sahayog Foundation"
              "\n2.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    elif pooham>5 and upmam>4 and alooparatham>3 and cheelam>3:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Palms Care Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Subramaniam Iyer is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    elif pooham>0 and upmam>0 and alooparatham>0 and cheelam>0:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Seva Sahayog Foundation"
              "\n2.ASK - Anandi seva kendra"
              "\n3.Palms Care Foundation"
              "\n4.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mayank Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 3:
            print("Subramaniam Iyer is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 4:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    else:
        print("There are no NGO's ready to accept your food.")

elif mealtype == 2:
    #lunch
    print("Enter the number of people 'Paneer Tikka Masala' can feed:")
    paneertikkamasalam = int(input())
    print("Enter the number of people 'Mix Vegetable' can feed:")
    mixvegetablem = int(input())
    print("Enter the number of people 'Chole' can feed:")
    cholem = int(input())
    print("Enter the number of people 'Bhindi ki sabji' can feed:")
    bhindikisabji = int(input())
    if paneertikkamasalam > 0 and mixvegetablem > 3 and cholem > 2 and bhindikisabji > 0:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Seva Sahayog Foundation"
              "\n2.ASK - Anandi seva kendra"
              "\n3.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mayank Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 3:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")

    elif paneertikkamasalam > 6 and mixvegetablem >= 4 and cholem > 0 and bhindikisabji > 0:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Seva Sahayog Foundation"
              "\n2.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    elif paneertikkamasalam > 5 and mixvegetablem > 4 and cholem > 3 and bhindikisabji > 3:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Palms Care Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
                print("Subramaniam Iyer is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    elif paneertikkamasalam > 0 and mixvegetablem > 0 and cholem > 0 and bhindikisabji > 0:
        print("The NGO's ready to accept the meal near you are:\n"
                  "\n1.Seva Sahayog Foundation"
                  "\n2.ASK - Anandi seva kendra"
                  "\n3.Palms Care Foundation"
                  "\n4.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mayank Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 3:
            print("Subramaniam Iyer is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 4:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    else:
         print("There are no NGO's ready to accept your food.")

elif mealtype == 3:
    #dinner
    print("Enter the number of people 'Palak Paneer' can feed:")
    palakpannerm = int(input())
    print("Enter the number of people 'Mushroom & Corn' can feed:")
    mushcornm = int(input())
    print("Enter the number of people 'Cabbage Fry' can feed:")
    cabbagefrym = int(input())
    print("Enter the number of people 'Aloo Capsicum' can feed:")
    aloocapsicumm = int(input())

    if palakpannerm>0 and mushcornm>3 and cabbagefrym>2 and aloocapsicumm>0:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Seva Sahayog Foundation"
              "\n2.ASK - Anandi seva kendra"
              "\n3.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mayank Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 3:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    elif palakpannerm>6 and mushcornm>=4 and cabbagefrym>0 and aloocapsicumm>0:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Seva Sahayog Foundation"
              "\n2.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    elif palakpannerm>5 and mushcornm>4 and cabbagefrym>3 and aloocapsicumm>3:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Palms Care Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Subramaniam Iyer is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    elif palakpannerm>0 and mushcornm>0 and cabbagefrym>0 and aloocapsicumm>0:
        print("The NGO's ready to accept the meal near you are:\n"
              "\n1.Seva Sahayog Foundation"
              "\n2.ASK - Anandi seva kendra"
              "\n3.Palms Care Foundation"
              "\n4.Jayashree Foundation")
        print("Which NGO would you like to pick up the food?")
        targetngo = int(input())
        if targetngo == 1:
            print("Ramesh Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 2:
            print("Mayank Sharma is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 3:
            print("Subramaniam Iyer is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        elif targetngo == 4:
            print("Mahesh Babu is on the way to pick-up your donation. Thank you for the donation, have a great day ahead!")
        else:
            print("Invalid Entry")
    else:
        print("There are no NGO's ready to accept your food.")


else:
    print("Wrong Input")