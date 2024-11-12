import turtle
bob = turtle.Turtle()
print(bob)




for i in range(4):
    print('Hello!')

    

def square(t,length):
    

    t.fd(100)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(length)

    turtle.mainloop() 

   

square(bob,50)

def polygon(t,length,n):
    

    t.fd(100)
    t.lt(90)
    t.fd(length(n))
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(length(n))

    turtle.mainloop() 
    
