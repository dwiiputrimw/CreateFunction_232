def printme(text1):#This is a print function#
    print(text1)
    return

printme("I'm first call to user defined function!")
printme(text1="Again second call to the same function")


def changeme( mylist ):#This changes a passed list#
    mylist.append([1, 2, 3, 4]);
    print("Values inside the function: ", mylist)
    return
mylist_2 = [10, 20, 30];
changeme( mylist_2 );
print("Values outside the function: ", mylist_2)


def changeme( mylist ):
    "This changes a passed list"
    mylist = [1, 2, 3, 4]
    print("Values inside the function: ", mylist)
    return
mylist = [10, 20, 30];
changeme( mylist );
print("Values outside the function: ", mylist)


def printme(str):
    "This prints a passed string"
    print(str)
    return
printme("Halo");


def printinfo(name, age=35): #TEST Function#
    print("Name: ", name)
    print("Age ", age)
    return

printinfo(age=12, name="miki");
printinfo( 30, "dwi");
printinfo( name="miku" );
printinfo( 71, "kiya");


def printinfo(arg1, *vartuple): #This is test#
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo(5);
printinfo(100, 200, 300, 400);


total = lambda arg1, arg2: arg1 - arg2
print("Value of total : ", total(7, 3))
print("Value of total : ", total(250, 50))


x = 10 
while x > 8:
    x -= 1
    print(x)

for i in range(4, 6):
    print(i)
    