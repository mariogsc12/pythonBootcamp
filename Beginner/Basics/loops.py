# -- Easy examples with loops

# 1. FOR LOOP
programming_languages = ["Python","C++","Java","C","Rust"]

for i in programming_languages:
    print(i)

for i in range(0,10,3):     # (start , end , step)
    print(i)

j = 0
while j<10:
    j+=1
    print(f"j={j}") 