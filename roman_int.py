dict = {"I" : 1, "II" : 2, "III" : 3, "IV" : 4, "V" : 5, "VI" : 6, "VII" : 7, "VIII" : 8, "IX" : 9, "X" : 10, "XV" : 15, "XX" : 20, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

roman = input("Enter a number :")
print()
sum  = 0

for i in range(len(roman)) :
    if i+1<len(roman) and dict[roman[i]] < dict[roman[i+1]] :
        sum -= dict[roman[i]]
    else :
        sum += dict[roman[i]]
print(sum)

'''for i in range(len(roman)) :
    print(roman[i])
    
    if dict[roman[i]] < dict[roman[i-1]] :
        sum -= dict[roman[i]]
    else :
        sum += dict[roman[i]]
print(sum)'''


    