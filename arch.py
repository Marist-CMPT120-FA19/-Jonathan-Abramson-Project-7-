from graphics import *
import math
 
win = GraphWin("Archery Target", 500,500)
win.setBackground('goldenrod')
win.setCoords(-250, -250, 250, 250)
cen = Point(0,0)
 
msg = Text(Point(0,230), 'Click to hit the target.')
msg.setFill('blue')
msg.draw(win)
 
def score_text(): #Displays score
    v = 190
    z = 18
 
    bullseye = Text(Point(0,0), 'x')
    bullseye.setSize(14)
    bullseye.draw(win)
 
    for i in range(1,11):
        score_number = Text(Point(0,v), i)
        score_number.setSize(z)
        score_number.setFill('blue')
        score_number.draw(win)
        v = v - 19
        z -= 1
 
def hit_target(): #Shows "Hits"
    count = 0
    for i in range(10):
 
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        p = Circle(Point(x,y),4)
        p.setFill('purple')
        p.draw(win)
        d = x**2 + y**2
 
        string = 'You hit the target. Score is %s.'
        if d > 200**2:
            msg.setText(('You missed the target. Score is %s.' %count))
        elif d <= 10**2:
            count += 11
            msg.setText(('Congrats! You hit the bullseye. Score is %s.' %count))
        elif d <= 29**2:
            count += 10
            message = msg.setText((string %count))
        elif d <= 48**2:
            count += 9
            message = msg.setText((string %count))
        elif d <= 67**2:
            count += 8
            message = msg.setText((string %count))
        elif d <= 86**2:
            count += 7
            message = msg.setText((string %count))
        elif d <= 105**2:
            count += 6
            message = msg.setText((string %count))
        elif d <= 124**2:
            count += 5
            message = msg.setText((string %count))
        elif d <= 143**2:
            count += 4
            message = msg.setText((string %count))
        elif d <= 162**2:
            count += 3
            message = msg.setText((string %count))
        elif d <= 181**2:
            count += 2
            message = msg.setText((string %count))
        elif d <= 200**2:
            count += 1
            message = msg.setText((string %count))
 
    msg.setText('Game over. Score is %s. Click anywhere to quit.' %count)
    win.getMouse()
    win.close()
 
    return count
 
def main(): 
    rad = 200
    color = ['white', 'black', 'cyan3', 'red', 'yellow']
    for i in range(5):
        for j in range(2):
            c = Circle(cen, rad)
            c.setFill(color[i])
            c.setOutline('gray')
            c.setWidth('2')
            c.draw(win)
            rad = (rad - 19)
    center = Circle(cen,10)
    center.setOutline('gray')
    center.setWidth('2')
    center.draw(win)
    score_text()
    hit_target()
 
if __name__ == '__main__':
    main()