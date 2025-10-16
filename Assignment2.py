# 15 meaning_full_use_cases using the slice operator with the index value in string:
# let us start with the positive index which is from forward direction:
# Index values can be mentioned can be followed as : [start value : End value : step value]
import time
print()
S="python with generative AI developer"
#1. using the above string print the full string with start value:
print()
print("Print the full string using the index :  ",S[0:])
print()
time.sleep(2)
print("End of the first use_case")
print()
#2. Using the start value print the first character of the string
print("print the first character of the string:",S[0])
print()
time.sleep(2) 
print("End of the second use_case")
print()
#3. Using the start and end value print the full string
# for that we have to find the length of the string then use the end value 

print("Print the string using the start and end value :",S[0:len(S)])
print()
time.sleep(2)
print("End of the third use_case")
print()

# 4.print specific characters or words using the start and end values:
print("Print the 'python' word using start and end value :",S[0:6])
print()
time.sleep(1)
print("end of fourth use_case")
print()

# 5.print the combination of words with the spaces 
print("Print the 'with gen' word using start and end vale:",S[7:15])
print()
time.sleep(1)
print("end of the fifth use_case")
print()

# 6. print the first and last 3 characters using two times slice operator  
print("Print the first and last 3 characters 'pyt per' :",S[0:3],S[32:35])
print()
time.sleep(1)
print("End of the sixth use_case")
print()

#7.Get the first 10 characters without using the start value:
print("Print the first 10 characters without usnig start value:",S[:11])
print()
time.sleep(1)
print("End of the seventh use_case")
print()
# 8. print all the characters without using the start value:
print("print the string without using start value: ",S[:35])
print()
time.sleep(1)
print("End of eighth use_case")
print()

# 9.Print the string with start,end, step value:
print("print the string using start,end,step value : ",S[0:35:1]) # here the 1 can use to print all the values we can use to step 2,3,4 etc on next examples
print()
time.sleep(1)
print("end of ninth use_case")
print()

# 10. Get the every 2nd character using the step value:
print("print the every 2nd character using step value: ",S[0:35:2])
print()
time.sleep(1)
print("End of 10th use_case")
print()

#11. Get the every 3rd character using the step value
print("print the every 3rd character using step value: ",S[0:35:3])
print()
time.sleep(1)
print("End of 11th use_case")
print()

#12.Slice the string so that it only contains characters from index 7 to 18.
print("print the characters from index from 7 to 18 : ",S[7:19])
print()
time.sleep(1)
print("End of 12th use_case")
print()

# 13.Retrieve the substring "AI" using slicing.
print("Retrieve the substring 'AI' using slicing : ",S[23:25])
print()
time.sleep(1)
print("End of 13th use_case")
print()

# 14.Get the substring between "with" and "AI" using slicing only.
print("Retrieve the substring between 'with' and 'AI' using slicing : ",S[12:22])
print()
time.sleep(1)
print("End of 14th use_case")
print()

# 15. Extract every second character from the set of characters or words:
print("extract every second character from the set of characters or words  : ",S[10:25:2])
print()
time.sleep(1)
print("End of 15th use_case")
print()
print("End of the assignment 2 with positive indexing values")
print()



