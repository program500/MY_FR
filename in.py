#list type data 
# 
# my first git push 
 
fruits_list = ['apple', 'banana', 'cherry', 'berry', 'mango']
for index, items in enumerate(sorted(fruits_list), start= 1):
    print(f"{index}. {items}")

fruits_list.append("coconut")
print(fruits_list)
fruits_list.insert(1,('wood apple'))
print(fruits_list)

specialist = ['garlic', 'onion', 'oil', 'green banana']
fruits_list.extend(specialist)
print(fruits_list)

fruits_list.remove("apple")
print(fruits_list)


index = 0 
while index < 21 : 
    print(index)
    index += 1 


#sets type dta 
my_set = {'apple',' banana',' cherry', 'berry', 'mango', 'coconut',' jackfruit'}
my_set.add('pine apple')
print(my_set)
for index , items in enumerate(sorted(my_set), start=1): 
    print(f"{index}. {items}")


#Tuple type data 
my_tuple = ("apple", "banan", 'cherry', 'berry')
my_tuple.index('apple')
print(my_tuple)

for index , items in enumerate(sorted(my_tuple), start=1): 
    print(f"{index}. {items}")



#fozenset 
my = frozenset({'apple', 'banana',' cherry', 'coconut'})
s = tuple(my)
a = frozenset(s)
print(a)
print(type(a))

for index , items in enumerate(sorted(a), start=1): 
    print(f"{index}.{items}")








"""



#dictionary type dart a

my_dictionary = {
             "Name": "Hasip", 
             "age": 20 , 
             "city": "Sanfrancisco"
}

print(my_dictionary.keys())
print(my_dictionary.values())
for index , items in enumerate(sorted(my_dictionary), start=1): 
    print(f"{index}.{items}")



#this is dictionary type dat a 

#Control flow type data

marks = int(input("Enter your marks: "))

if marks <= 100 and marks >= 80 : 
    print('A+')
elif marks <= 80 and marks >= 70 : 
    print("Ar")
elif marks <= 70 and marks >= 60 : 
    print("A-")
elif marks <= 60 and marks >= 50 : 
    print("B") 
elif marks <= 50 and marks >= 40: 
    print('C')
elif marks <= 40 and marks >= 33:
    print('D')
else:
    print('F')"""

"""
#Break and continue 
for i in range (0, 10, 1): 
    if i == 4: 
       continue
    print(i)


#argument and paramitars type data 

def add_two(*person): 
    print(person)
add_two('apple', 10, True, False, 30 , 50 , 90, "Banana")"""

#python encapsulation
class BankAccount: 
    __balance = 0 
    def deposit(self, amount): 
        if amount > 0 : 
            self.__balance += amount 
        else: 
            print("Invalid amount")
    def withdraw(self , amount): 
        if amount > 0 and amount <= self.__balance : 
            self.__balance -= amount 
        else: 
            print("Insufficent amount")
    def check_balance(self): 
        return self.__balance 
    
My_Account = BankAccount()
My_Account.deposit(1000)
print(My_Account.check_balance())
