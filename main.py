
"Solved By Nasse Salah Yazgi"

"""
Numbera
"""
# # 69
# # Corn Production Suppose each acre of farmland produces 18 tons of corn. How
# #many tons of corn can be grown on a 30-acre farm?
#
# # here i will say for 1 farmland i will make 9 corn
#
# farmland = 30
# tons = 18
# print("#69  The Answer is = :    "+str(farmland*tons))

# #70
# i =50
# ii=5
# time=3
# ha=-16*time**2+i*time+ii
# print("High the ball after 3 seconds= ",ha)


# #71
# avaspeedis= 81.34
# timefromair = 5
# forhome=9
# avartime= forhome -timefromair
# space =avaspeedis*avartime
# print("#71  The distance is : "+str(space))


# #72
# whenfilled= 23352
# when_need=23695
# number_golas = 14
# ava =when_need - whenfilled
# print("#72\tThe Avar for every gallon \t"+ str(ava/number_golas))

# #73
# numberofpeople=5000000
# electricitneed=750000000
# numbeday=30
# everdayelectricity = numberofpeople * numbeday
# foreverypeople =electricitneed/everdayelectricity
# print("#73\t daily power consumption in watts of each residen   "+str(foreverypeople))
#
# #74
# s=432**.5
# print("Side of the deck = ",s)

# # #75
# # first_money =1000
# # dis=.087
# # years =2
# # total = ( 1+ (first_money * (dis**years)) )
# # print("#75\tThe Total Menoy is "+str(round(total)))
#
#
# #STRING SOLVE PROBLEM .
# print("STRING PROBLEM \n " )

"""
Strings
"""
# #97
# lig = float(input("S #97\tEnter number of seconds between"))
# strom = lig/5
# print("Distance from storm: " + str(round(strom,2)))

# #98
# age = float(input("S #97\tEnter your age "))
# resting = float(input("Enter your resting heart ratee "))
# total = int(0.7*(220-age) +0.3*resting)
# print("Training heart rate: " + str(total) +" beats/min." )

# #101
# name_team = input("Enter name of team:")
# win_game = int(input("Enter number of games won: "))
# lost_game = int(input("Enter number of games lost:"))
# ava=((win_game) /(win_game +lost_game) )
# total = round(100* ava  , 1)
# print( name_team +" WIN " + str(total)+ "% of their games ")

# #108
# purchase = float(input("Enter purchase price: "))
# selling = float(input("Enter selling price:"))
# markup= selling - purchase
# percentage_markup = (markup /purchase)*100
# profit_margin=(markup/selling)*100
# print("Markup:${0:.2f}".format(markup))
# print("Percentage markup:  {0:.2f}%".format(percentage_markup))
# print("Profit margin:  {0:.2f} %".format(profit_margin))

#109
# number = input("Enter number")
# dd=number.find('.')
# print(dd-1, "digits to left of decimal point")
# AFF = len(number)-dd -1
# print(AFF, "digits to right of decimal point")


#110
# stat = input("Enter a sentence")
# word1 = input("Enter word to replace : ")
# word2 = input("Enter replacement word:")
# print(stat.replace(word1 , word2) )
#111
# methods = int(input("Enter number of months"))
# years = methods // 12 ;
# meth = methods %12 ;
# print(str(methods)+" months is " + str(years) +" Years and " + str(meth) )

"""
#OutPut

"""


# #53
# amount = float(input("Enter amount of bill :"))
# perc = int(input("Enter percentage tig :"))
# tip = (perc/100) * amount
# print("Tip: ${0:.2f}".format(tip))
#
# #54
# rev = float(input("Enter revenue"))
# exp = float(input("Enter expesnses"))
# income = rev - exp
# print("Net income : ${0:.2f}".format(income))

#55
#
# salary = int(input("Enter beginning salary:"))
# salary_after = (salary*0.1) + salary
#
# salary_befor =  salary_after*0.1 - salary
# total = (salary_befor  - salary ) / salary
# print("New Salary : ${0:.2f}".format(salary_befor))
# print("Change ${0:.2f}".format(total))


"""
Lists, tuples and files
"""
#101
# string2 = input("Enter a sentence :  ")
# a=string2.count(" ")
# print("Number of words : ",a+1)

# #102
# st = input("Reach for the stars")
# a = st.split(" ")
# first=a[0]
# last=a[-1]
# print("Frist Word   "+a[1])
# print("Last Word : "+a[-1])

#103
# st=input("Enter a 2-part name :")
# a=st.split(" ")
# strs= a[-1]+ " , " + a[1]
# print("Revised From : " + strs)

#104
# ss=input("Enter 3-part name :")
# a=ss.split(" ")
# print("Middle Name :"+a[2])


