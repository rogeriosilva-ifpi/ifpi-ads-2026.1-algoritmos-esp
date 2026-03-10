import turtle


def main():
  bob = turtle.Turtle('turtle')
  
  quadrado(bob, 170, 'green')
  quadrado(bob, 70, 'blue')
  quadrado(bob, 35, 'red')

  bob.pencolor('red')
  bob.fd(200)
  bob.left(120)
  bob.fd(200)
  bob.left(120)
  bob.fd(200)
  bob.left(120)

  bob.pencolor('blue')
  bob.fd(100)
  bob.left(120)
  bob.fd(100)
  bob.left(120)
  bob.fd(100)
  bob.left(120)
 
  turtle.mainloop()


def quadrado(t, lado, cor):
  t.pencolor(cor)

  for i in range(4):
    t.forward(lado)
    t.left(90)


main()