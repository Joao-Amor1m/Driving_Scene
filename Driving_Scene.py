##Joao Amorim
##December 16
##Driving_Scene.py
##make a scene with a moving car and a reaction



import DrawingPanel

w = DrawingPanel.DrawingPanel(800,600)

def background():
    w.fill_rect(0,0,800,600,"LightSalmon1")
    w.fill_oval(700,300,200,300,"DarkGoldenRod4")
    w.fill_rect(0,450,800,150,"light green")
    w.fill_rect(0,450,800,10,"black")


def blue_car(x,y):
    w.fill_rect(x,y,50,15,"Dodgerblue")
    w.draw_rect(x+15,y-10,25,10,"Dodgerblue")
    w.fill_oval(x+3,y+7,14,14,"black")
    w.fill_oval(x+33,y+7,14,14,"black")

def kid(z,y):
    w.fill_rect(z,y,15,25,"maroon2")
    w.fill_rect(z+3,y-15,10,15,"wheat2")

for i in range(150):
    background()
    blue_car(100+(i*2),429)
    kid(450,429)
    w.sleep(1000/60)
   

w.sleep(2000)
    
for i in range(150):
    background()
    blue_car(450+(i*20),429)
    w.sleep(1000/60)


    

  
        
    














