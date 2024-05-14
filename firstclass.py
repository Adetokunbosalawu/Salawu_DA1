# #This is how to output words in python
# print('welcome to first class')
# print('Nigeria is a great country')
# #How to create a variable
# bottle='water'
# print (bottle)
# print(type(bottle))
# firstname='wura'
# print(firstname)
# num1=10.0
# print(num1)
# print(type(num1))
# Online=True
# print(Online)
# print(type(Online))
# x=' awesome'
# print('python is' +x)
# print('python is' +" "+x)
# x='welcome'
# y= ' here'
# print(x+y)

# x=' Ade'
# y='Salawu'
# print('my firstname is'+x + ' my last name is '+y) 

# print(f"my firstname is{x} my last name is {y}")
# name='dayo'
# age=12
# print(name+str(age))
# []
# {}
# x='winners'
# print(x.upper())
# x='WINNERS'
# print(x.lower())
# print(x.capitalize())
# print(x.count('N'))
# print(len(x)) 
# a='hello world'
# print(a[2])
# print(a[-1])
# print(a.replace('h','j'))
# #addition
# a=8
# b=5
# c=a+b
# print(c)


# #subtraction
# a=8
# b=5
# c=a-b
# print(c)


# #multiplication
# a=8
# b=5
# c=a*b
# print(c)


# #division
# a=8
# b=5
# c=a/b
# print(c)


# #modulus
# a=8
# b=5
# c=a%b
# print(c)


# #exponential
# a=8
# b=5
# c=a**b
# print(c)


# #addition
# a=8
# b=5
# c=a==b
# print(c)


# #addition
# a=8
# b=5
# c=a!=b
# print(c)


#addition
a=8
b=5
c=a>b
print(c)


# #addition
# a=8
# b=5
# c=a<b
# print(c)


#addition
a=8
b=5
c=a>=b
print(c)


#addition
a=8
b=5
c=a<=b
print(c)

x=5
print(x>3 and x<10)



x=5
print(x>3 and x<4)



x=5
print(x>3 or  x<4)

#This is how to output words in python
print('welcome to first class')


a='this'
b=' a great'
c=' country'
d= a + b + c
print(d)

a='Ibadan is a big city'
print(a[0])
print(a[-1])
print(a.upper ())
print(a.lower ())
print(a.capitalize ())
print(a.count ('i'))
print(len (a))

# name='wura'
# user=input('please enter your name')
# print (user)
# print ('welcome ' +user)
# address=input('where do you live')
# print(address)
# print('I am living at ' +address)

# Convert Naira to Dollar
# dollar=input('enter the amount in dollar')
# print(int(dollar)*750)
# naira=input('enter the amount in naira')
# print(int(naira)/750)
#pounds=input('enter the amount in pounds')
#print(int(pounds)*2)
#print(float(pounds)*1.5)

# Temperature
#C=F*9/5+32
#f=input('enter the temperature in fahrenheit')
#print(int(f)*9/5+32 , 'celcius')

# C=f*5/9-32
#c=input('enter the temperature in celcius')
#print(int(c)-32*(5/9) , 'fahrenheit')

#K=C+32
# c=input('enter temperature in celcius')
# print(int(c)+32, 'kelvin')


# Secret_Key='Ade'
# passcode=input('guess the secret key')
# if Secret_Key==passcode:
#     print('you guessed right')
# else:
#     print('you just guessed wrong')

    
# Secret_Key='ade'
# passcode=input('guess the secret key right').lower()
# if Secret_Key==passcode:
#     print('you guessed right')
# else:
#     print('you just guessed wrong')


# question1=input('what is the capital of oyo state').lower()
# answer1='ibadan'
# if question1==answer1:
#     print('correct')
# else:
#     print('wrong')


# question1=input('what is the capital of lagos state').lower()
# answer1='ikeja'
# if question1==answer1:
#     print('correct')
# else:
#     print('wrong')
    
# question1=input('what is the capital of ogun state').lower()
# answer1='abeokuta'
# if question1==answer1:
#     print('correct')
# else:
#     print('wrong')

#Advance Data Types
#recall the last food
# food=['rice','beans','plantain','semo','amala','fufu']
# print(food)
# print(food[-1])

#replace beans with moinmoin
# food=['rice','beans','plantain','semo','amala','fufu']
# food[1]='moinmoin'
# print(food)

#replace semo with whole wheat
# food=['rice','beans','plantain','semo','amala','fufu']
# food[3]='whole wheat'
# print(food)

#replace semo with whole wheat
# food=['rice','beans','plantain','semo','amala','fufu']
# food[3]='whole wheat'
#print(food)

#count the food
# print(len(food))

#append or add
# food=['rice','beans','plantain','semo','amala','fufu']
# food.append('moinmoin')
# print(food)

#insert at a postion 1 or beans
# food=['rice','beans','plantain','semo','amala','fufu']
# food.insert(1,'moinmoin')
# print(food)

#Remove method1
# food=['rice','beans','plantain','semo','amala','fufu']
# food.remove('rice')
# print(food)

#Remove method2
# food=['rice','beans','plantain','semo','amala','fufu']
# food.pop(0)
# print(food)

#clear 
# food=['rice','beans','plantain','semo','amala','fufu']
# food.clear()
# print(food)

#type of variable cleared
food=['rice','beans','plantain','semo','amala','fufu']
food.clear()
print(type(food))

#Tuple
#ludo=('star','square','circle','rectangle')
# print(ludo[1])

#Tuple cannot be changed
# ludo=('star','square','circle','rectangle')
# ludo[1]='kite'
# print(ludo)

#Tuple cannot be deleted
# ludo=('star','square','circle','rectangle')
# ludo.clear()
# print(ludo)

#Sets
food={'rice','beans','amala','fufu'}
print(food)

# #set add
# food={'rice','beans','amala','fufu'}
# food.add('egusi')
# print(food)

# #set add more than one thing
# food={'rice','beans','amala','fufu'}
# food.update(['egusi', 'efo', 'ewedu', 'ogbono'])
# print(food)


#set count the length
food={'rice','beans','amala','fufu'}
print(len(food))


# #set remove method1
# food={'rice','beans','amala','fufu'}
# food.remove ('rice')
# print(food)

# #set remove method2
# food={'rice','beans','amala','fufu'}
# food.discard ('rice')
# print(food)

#set clear
food={'rice','beans','amala','fufu'}
food.clear ()
print(food)

#set newdata
food={'rice','beans','amala','fufu'}
newdata=food.copy()
print(newdata)


#Dictionary go indepth
version={
    'name':'wura',
    'age':12,
    'gender':'female'
}
x=version['gender']
print(x)

x=version['age']
print(x)

#change gender to male
version={
    'name':'wura',
    'age':12,
    'gender':'female'
}
version['gender']='male'
print(version)

#pop removing method 1

version.pop('age')
print(version)

#pop item removing all gender or last element method 2
version.popitem()
print(version)
























