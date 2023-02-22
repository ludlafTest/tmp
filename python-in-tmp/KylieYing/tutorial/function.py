# defining a function
# function name is addition, and we are passing in 2 parameters: x and y
# we want to return the value of x plus y
def addition(x, y):
    return x + y

def add_one_in_loop(some_list):
    new_list = []
    for item in some_list:
        item = item + 1
        new_list.append(item)

    return new_list

# using if statements allows us to have a more powerful arsenal
def number_relation(x, y):
    if x < y:
        return "Too low!"
    elif x > y: # else if
        return "Too high!"
    else:
        return "Equal :))"


# calling the function
# print(addition(1, 50))
print(add_one_in_loop([1,2,3]))

secret_number = 16
print(number_relation(20, secret_number)) # expect "Equal :)"

# we can allow functions to run inside one another
print(number_relation(addition(15, 236), addition(1263, -478))) 