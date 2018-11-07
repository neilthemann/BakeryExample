# Bakery cart appliction example
# Neil Mann
# CIS-120-FA18

# Define variables
totalCost = 0
totalCupcakes = 0
totalPies = 0
totalMuffins = 0
totalCakes = 0
userExit = False
userMenuChoice = 0
userSubMenuExit = False
userSubMenuChoice = 0

def viewCart():
    print("*******************")
    print("Your cart:")
    print("Total cupcakes: " + str(totalCupcakes))
    print("Total pies: " + str(totalPies))
    print("Total muffins: " + str(totalMuffins))
    print("Total cakes: " + str(totalCakes))
    print("Total cost: " + str(totalCost))
    print("*******************")

def checkout():
    file = open("reciept.txt", "w")
    file.write("Thank you for your purchase from the Bakery!\n")
    file.write("*******************\n")
    file.write("Total cupcakes: " + str(totalCupcakes) + "\n")
    file.write("Total pies: " + str(totalPies) + "\n")
    file.write("Total muffins: " + str(totalMuffins) + "\n")
    file.write("Total cakes: " + str(totalCakes) + "\n")
    file.write("Total cost: " + str(totalCost) + "\n")
    file.write("*******************\n")
    file.write("Please visit us on Facepage\n")
    file.close()
    
while (userExit == False):
    print("Welcome to the bakery!")
    print("What would you like to do?")
    print("1. Add an item to your cart")
    print("2. View your cart")
    print("3. Checkout and exit")
    userMenuChoice = int(input())

    if (userMenuChoice == 1):
        while(userSubMenuExit == False):
            print("What would you like to add to your cart?")
            print("1. Cupcakes (1 dozen) - $5")
            print("2. Apple Pie - $6")
            print("3. Muffins (1 dozen) - $4")
            print("4. Birthday Cake - $15")
            print("5. Return to previous menu")
            userSubMenuChoice = int(input())

            if(userSubMenuChoice == 1):
                totalCupcakes = totalCupcakes + 1
                totalCost = totalCost + 5
            elif(userSubMenuChoice == 2):
                totalPies = totalPies + 1
                totalCost = totalCost + 6
            elif(userSubMenuChoice == 3):
                totalMuffins = totalMuffins + 1
                totalCost = totalCost + 4
            elif(userSubMenuChoice == 4):
                totalCakes = totalCakes + 1
                totalCost = totalCost + 15
            elif(userSubMenuChoice == 5):
                userSubMenuExit = True
                break
            else:
                print("Please enter a valid number")

    elif(userMenuChoice == 2):
        viewCart()

    elif(userMenuChoice == 3):
        checkout()
        userExit = True





        

    
