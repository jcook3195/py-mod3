from graphics import *


def main():
    window = GraphWin("Draw Rectangle", 300, 300)
    window.setBackground("white")
    cl1 = window.getMouse()
    cl2 = window.getMouse()
    rect = Rectangle(cl1, cl2)
    rect.setFill("red")
    rect.setOutline("blue")
    rect.draw(window)

    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()
