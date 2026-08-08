str = input(" user's first name: ")

len = len(str)

print("the length of string is :",len)

ch = str[1:5]
ch2 = str[-3:-1]

print(ch,'\n',ch2)

print(str.capitalize())
print(str.replace("kabir","AVI"))
print(str.count("r"))
print(str.find("e"))



str2= ("my name is compare to $ because its is $ realated to $ and $is my love, $ is my name")

print(str2.count("$"))
print(str2.replace ("$","avi"))


rashi = 98
annu =97

if rashi >= 90 and annu >=90:
    print("A+ grade")

else :
    print ("c grade ")
