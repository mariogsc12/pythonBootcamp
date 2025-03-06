import random

random_int = random.randint(0,10)
print(random_int)

random_float = random.uniform(0.0,20.0)
print(random_float)

my_list = ["Mario", "Alba", "Alvaro", "Pedro"]
random_item = random.choice(my_list)
print(random_item)
print(my_list[random.randint(0,len(my_list)-1)])