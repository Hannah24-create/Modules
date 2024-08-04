import hannahmymodules as mymodule 


#def test_my_module():
# Using functions from the mymodule
result_add = mymodule.add(4,2)    
result_subtract = mymodule.subtract(4, 2)  
result_multiply = mymodule.multiply(4, 2)  
result_divide = mymodule.divide(4, 2)      

print(result_add)
print(result_subtract)
print(result_multiply)
print(result_divide)


# Using the class from the module
animal = mymodule.Animal("dog","brown")
animal.pet() 


#list from the module
my_list = mymodule.animal_list
print(my_list)


#dictionary from the module
my_dict = mymodule.my_dict
print(my_dict)