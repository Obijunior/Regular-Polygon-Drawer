import turtle

def regular_polygon(sn, x, y, sl):
  turtle.clear()
  turtle.penup()
  turtle.setx(x)
  turtle.sety(y)
  turtle.pendown()
  for i in range(1, sn + 1):
    turtle.forward(sl)
    turtle.right(360 / sn)



a = int(input("Number of sides? : "))
b = int(input("Starting X position? : "))
c = int(input("Starting Y position? : "))
d = int(input("Side length? : "))

regular_polygon(a, b, c, d)
