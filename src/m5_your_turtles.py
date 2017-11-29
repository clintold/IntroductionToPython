"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Luke Clinton
"""
########################################################################
# Done.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
luke= rg.SimpleTurtle('turtle')
jayne = rg.SimpleTurtle('turtle')
luke.pen = rg.Pen('green',10)
jayne.pen = rg.Pen('pink',10)
luke.speed = 10
jayne.speed = 10
size= 5

for k in range (10):

    luke.draw_regular_polygon(k + 3, 10*k + 100)

    luke.pen_up()
    luke.right(45)
    luke.forward(10)
    luke.left(45)

    luke.pen_down()

    jayne.draw_circle(10*k)
    jayne.pen_up()
    jayne.right(45)
    jayne.forward(10)
    jayne.left(45)
    jayne.pen_down()

window.close_on_mouse_click()