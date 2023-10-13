Bag_1p_Weight = 3.56
Bag_2p_Weight = 7.12
Bag_5p_Weight = 2.35
Bag_10p_Weight = 6.50
Bag_20p_Weight = 5.00
Bag_50p_Weight = 8.00
Bag_100p_Weight = 8.75
Bag_200p_Weight = 12.00

Bag_1p_Value = 1.00
Bag_2p_Value = 1.00
Bag_5p_Value = 5.00
Bag_10p_Value = 5.00
Bag_20p_Value = 10.00
Bag_50p_Value = 10.00
Bag_100p_Value = 20.00
Bag_200p_Value = 20.00

type1 = input("What Coin Type Are You Counting?\n")
if type1 == 0.01 :
    print("What Is The Weight Of The Bag?")
    weight1 = input()
    Total_Bag1p_Weight = Bag_1p_Value * Bag_1p_Weight
    if weight1 == Total_Bag1p_Weight :
        print("Weight Of The Bag Is Correct")
    else :
        Amount1 = Total_Bag1p_Weight - weight1
        if Amount1 > Total_Bag1p_Weight :
         print(Amount1,"Needs To Be Removed")
        else :
           print(Amount1,"Needs To Be Added")
elif type1 == 0.02 : 
    print("What Is The Weight Of The Bag?")
    weight1 = input()
    Total_Bag1p_Weight = Bag_1p_Value * Bag_1p_Weight
    if weight1 == Total_Bag1p_Weight :
        print("Weight Of The Bag Is Correct")
    else :
        Amount1 = Total_Bag1p_Weight - weight1
        if Amount1 > Total_Bag1p_Weight :
            print(Amount1,"Needs To Be Removed")
        else :
         print(Amount1,"Needs To Be Added")