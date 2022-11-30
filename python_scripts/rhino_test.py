import rhinoscriptsyntax as rs

x = input("enter x_pos: ")
y = input("enter y_pos: ")

rs.AddPoint(x, y, 0)


for i in range(0, 100, 20):
    rs.AddPoint(x, i, 0)
