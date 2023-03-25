# Py Math Buddy

This code creates a basic calculator application using the tkinter library in Python. It also utilizes the math library for certain mathematical operations.
<br>
<br>
Firstly, the tkinter library is imported along with the math library. Then, a new instance of the Tk() class is created and assigned to the variable 'var'. The title of the application is set as "Math Buddy", and the background color is set to a shade of orange.
<br><br>
An Entry widget is created using the Entry() method of tkinter, and assigned to the variable 'e'. The width of the widget is set to 60, the border width is set to 20, and the widget is placed in the grid layout at row 0, column 0, spanning 4 columns, with 20 pixels of padding on both sides.
<br><br>
After setting up the GUI, the backend functions for the calculator are defined. The functions correspond to the various buttons that the user can click on the GUI, and perform the corresponding mathematical operations when the buttons are clicked.
<br><br>
The 'thebutton()' function is used to concatenate the button clicked by the user to the current value in the Entry widget. The 'theclearbutton()' function is used to clear the Entry widget. The 'thebuttonadd()', 'thebuttonsubstract()', 'thebuttonmultiplication()', and 'thebuttondivision()' functions are used to set the appropriate mathematical operation for the calculator and store the first operand in a variable named 'functionnum'.
<br><br>
The 'thebuttonequal()' function is used to perform the mathematical operation on the two operands stored in 'functionnum' and 'num2', which is obtained from the Entry widget. The mathematical operation performed depends on the value of the 'mathematics' variable. The result of the operation is then inserted into the Entry widget using the insert() method.
<br><br>
The remaining functions perform various mathematical operations like finding the sine, cosine, or tangent of a number, finding the square root, calculating a percentage, and many more.
<br><br>
Finally, buttons are created on the GUI using the Button() method of tkinter, and assigned to their respective functions. These buttons are placed in the grid layout at their respective positions on the GUI.
<br><br>
Overall, this code creates a simple calculator application with basic mathematical operations.
<br><br>
![python calculator](https://user-images.githubusercontent.com/61019243/227697994-79b8d8be-a41b-44db-81d8-23261d3f6b2c.png)
<br>
<br>
<br>![Screenshot_3](https://user-images.githubusercontent.com/61019243/227698018-b9d6134a-dbcf-4cd4-95c9-5c9fde381e65.png)


