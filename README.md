# Q-Learning Algorithm solves the Hanoi Towers Problem with 3 Poles & 4 Discs
==

An Inteligent Agent was programmed to solve the Hanoi Towers problem with 3 poles and 4 discs, the agent first creates the 
States Universe (81 possible states and their respective transitions) based on the rules for the Hanoi Towers problem.
Once it knows what are the possible states and valid transitions, it uses a machine learning algorithm to find the optima solution
(2^n)-1, in this case 15 steps at most.

The first few iterations it will take too many states to solve it, because the Q matrix (Quality or Knowledge matrix) doesn't
have much information. Solutions are improved with each training episodes, until the optimal solution is found.

Please note that this program was writtn when I was just starting with Python, I later found that the itertools library would
have made many things much easier and in a more 'pythonic' way. I will update this program when I have a chance.

I forgot to mention that a couple of weeks after I implemented this simple application, I ported it to Visual C# and used
the Aforge.NET library to support Computer Vision, the C# application uses a webcam to detects the initial state of the board
 and then it solves the problem using the optimal solution. I will upload it to github shortly.

Thank you,

Daniel.
