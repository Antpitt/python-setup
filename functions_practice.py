def hello():
  print("Hello, user!")

def pack(el_1, el_2, el_3):
    return[el_1, el_2, el_3]

def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunchbox is empty")
    for food_index in range(len(my_lunch)):
        if food_index == 0:
            print("First i eat {my_lunch[food_index]}")
        elif food_index < len(my_lunch) -1 :
            print("Then I eat {my_lunch[food_index]}")
        else:
            print("My lunchbox is empty")    

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])
