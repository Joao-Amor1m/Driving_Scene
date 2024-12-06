import DrawingPanel

w = DrawingPanel.DrawingPanel(800,600)

w.fill_rect(0,0,800,600,"LightSalmon1")

w.fill_oval(700,300,200,300,"DarkGoldenRod4")
w.fill_rect(0,450,800,150,"light green")

def blue_car(x,y):
    w.fill_rect(x,y,50,15,"Dodgerblue")
    w.draw_rect(x+15,y-10,25,10,"Dodgerblue")
    w.fill_oval(x+3,y+7,14,14,"black")
    w.fill_oval(x+33,y+7,14,14,"black")


blue_car(100,429)

for i in range(150):
    w.fill_rect(0,389,450,61,"LightSalmon1")
    blue_car(100+(i+20),429)
    w.sleep(1000/60)


