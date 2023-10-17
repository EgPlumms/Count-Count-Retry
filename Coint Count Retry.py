Bag_1p_Weight = 3.56
Bag_2p_Weight = 7.12
Bag_5p_Weight = 2.35
Bag_10p_Weight = 6.50
Bag_20p_Weight = 5.00
Bag_50p_Weight = 8.00
Bag_100p_Weight = 8.75
Bag_200p_Weight = 12.00

Bag_1p_Value = 100
Bag_2p_Value = 50
Bag_5p_Value = 100
Bag_10p_Value = 50
Bag_20p_Value = 50
Bag_50p_Value = 20
Bag_100p_Value = 20
Bag_200p_Value = 10

cointypes = 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01
Max_Bag = 8
Max_Bag = float(Max_Bag)

print("""
  ______             __                   ______                                   __     
 /      \           /  |                 /      \                                 /  |    
/$$$$$$  |  ______  $$/  _______        /$$$$$$  |  ______   __    __  _______   _$$ |_   
$$ |  $$/  /      \ /  |/       \       $$ |  $$/  /      \ /  |  /  |/       \ / $$   |  
$$ |      /$$$$$$  |$$ |$$$$$$$  |      $$ |      /$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$/   
$$ |   __ $$ |  $$ |$$ |$$ |  $$ |      $$ |   __ $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ | __ 
$$ \__/  |$$ \__$$ |$$ |$$ |  $$ |      $$ \__/  |$$ \__$$ |$$ \__$$ |$$ |  $$ |  $$ |/  |
$$    $$/ $$    $$/ $$ |$$ |  $$ |      $$    $$/ $$    $$/ $$    $$/ $$ |  $$ |  $$  $$/ 
 $$$$$$/   $$$$$$/  $$/ $$/   $$/        $$$$$$/   $$$$$$/   $$$$$$/  $$/   $$/    $$$$/ \n""")

Bag_Amount = int(input("How Many Bags Are You Counting?\n"))
for i in range(0,Bag_Amount) :
    type1 = input("What Coin Type Are You Counting? (Use 0.00)\n")
    if type1 == '0.01' :
        print("What Is The Weight Of The Bag?")
        weight1 = input()
        Total_Bag1p_Weight = Bag_1p_Value * Bag_1p_Weight
        if weight1 == Total_Bag1p_Weight :
            print("Weight Of The Bag Is Correct")
        else :
            weight1 = float(weight1)
            Amount1 = weight1 - Total_Bag1p_Weight
        if Amount1 < Total_Bag1p_Weight :
            print(Amount1,"Needs To Be Removed\n")
        elif Amount1 > Total_Bag1p_Weight :
            print(Amount1,"Needs To Be Added\n")
    elif type1 == '0.02' : 
        print("What Is The Weight Of The Bag?")
        weight2 = input()
        Total_Bag2p_Weight = Bag_2p_Value * Bag_2p_Weight
        if weight2 == Total_Bag2p_Weight :
            print("Weight Of The Bag Is Correct")
        else :
            weight2 = float(weight2)
            Amount2 = weight2 - Total_Bag2p_Weight
        if Amount2 < Total_Bag2p_Weight :
            print(Amount2,"Needs To Be Removed\n")
        else :
            print(Amount2,"Needs To Be Added\n")
    elif type1 == '0.05' : 
        print("What Is The Weight Of The Bag?")
        weight3 = input()
        Total_Bag5p_Weight = Bag_5p_Value * Bag_5p_Weight
        if weight3 == Total_Bag5p_Weight :
            print("Weight Of The Bag Is Correct")
        else :
            weight3 = float(weight3)
            Amount3 = weight3 - Total_Bag5p_Weight
        if Amount3 < Total_Bag5p_Weight :
            print(Amount3,"Needs To Be Removed\n")
        else :
            print(Amount3,"Needs To Be Added\n")
    elif type1 == '0.10' : 
        print("What Is The Weight Of The Bag?")
        weight4 = input()
        Total_Bag10p_Weight = Bag_10p_Value * Bag_10p_Weight
        if weight4 == Total_Bag10p_Weight :
            print("Weight Of The Bag Is Correct")
        else :
            weight4 = float(weight4)
            Amount4 = weight4 - Total_Bag10p_Weight 
        if Amount4 < Total_Bag10p_Weight :
            print(Amount4,"Needs To Be Removed\n")
        else :
            print(Amount4,"Needs To Be Added\n")
    elif type1 == '0.20' : 
        print("What Is The Weight Of The Bag?")
        weight5 = input()
        Total_Bag20p_Weight = Bag_20p_Value * Bag_20p_Weight
        if weight5 == Total_Bag20p_Weight :
            print("Weight Of The Bag Is Correct")
        else :
            weight5 = float(weight5)
            Amount5 = weight5 - Total_Bag20p_Weight
        if Amount5 < Total_Bag20p_Weight :
            print(Amount5,"Needs To Be Removed\n")
        else :
            print(Amount5,"Needs To Be Added\n")
    elif type1 == '0.50' : 
        print("What Is The Weight Of The Bag?")
        weight6 = input()
        Total_Bag50p_Weight = Bag_50p_Value * Bag_50p_Weight
        if weight6 == Total_Bag50p_Weight :
            print("Weight Of The Bag Is Correct")
        else :
            weight6 = float(weight6)
            Amount6 = weight6 - Total_Bag50p_Weight
        if Amount6 < Total_Bag50p_Weight :
            print(Amount6,"Needs To Be Removed\n")
        else :
            print(Amount6,"Needs To Be Added\n")
    elif type1 == '1.00' : 
        print("What Is The Weight Of The Bag?")
        weight7 = input()
        Total_Bag100p_Weight = Bag_100p_Value * Bag_100p_Weight
        if weight7 == Total_Bag100p_Weight :
            print("Weight Of The Bag Is Correct")
        else :
            weight7 = float(weight7)
            Amount7 = weight7 - Total_Bag100p_Weight
        if Amount7 < Total_Bag100p_Weight :
           print(Amount7,"Needs To Be Removed\n")
        else :
           print(Amount7,"Needs To Be Added\n")
    elif type1 == '2.00' : 
        print("What Is The Weight Of The Bag?")
        weight8 = input()
        Total_Bag200p_Weight = Bag_200p_Value * Bag_200p_Weight
        if weight8 == Total_Bag200p_Weight :
            print("Weight Of The Bag Is Correct")
        else :
            weight8 = float(weight8)
            Amount8 = weight8 - Total_Bag200p_Weight
        if Amount8 < Total_Bag200p_Weight :
           print(Amount8,"Needs To Be Removed\n")
        else :
            print(Amount8,"Needs To Be Added\n")
    else :
        print("This Isn't A Valid Input.\n")

print("What Are the Volunteers Names?(Enter Names Below)\n")
if Bag_Amount == 1 : 
    Vol1 = input()
elif Bag_Amount == 2 :
    Vol1 = input()
    Vol2 = input()
elif Bag_Amount == 3 :
    Vol1 = input()
    Vol2 = input()
    Vol3 = input()
elif Bag_Amount== 4 :
    Vol1 = input()
    Vol2 = input()
    Vol3 = input()
    Vol4 = input()
elif Bag_Amount == 5 :
    Vol1 = input()
    Vol2 = input()
    Vol3 = input()
    Vol4 = input()
    Vol5 = input()
elif Bag_Amount == 6 :
    Vol1 = input()
    Vol2 = input()
    Vol3 = input()
    Vol4 = input()
    Vol5 = input()
    Vol6 = input()
elif Bag_Amount == 7 :
    Vol1 = input()
    Vol2 = input()
    Vol3 = input()
    Vol4 = input()
    Vol5 = input()
    Vol6 = input()
    Vol7 = input()
elif Bag_Amount == 8 :
    Vol1 = input()
    Vol2 = input()
    Vol3 = input()
    Vol4 = input()
    Vol5 = input()
    Vol6 = input()
    Vol7 = input()
    Vol8 = input()
else :
    print("Too Many Volunteers")
print("What Coin Did Each Volunteer Count?")
