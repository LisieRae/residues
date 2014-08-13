----------------------------------
     README Contents:
----------------------------------

I.   Why Quadratic Residues?
II.  Folder Contents
III. The Story
IV.  Some Nice Math


----------------------------------
I.   Why Quadratic Residues?
----------------------------------

1. The math is pretty. A quadratic residue is y^2 mod x. Residues
	across a grid of incrementing values of y and x have beautiful patterns.
2. Implementing this was a fun way to demo different programming languages,
	particularly Python and JavaScript, and their visualization tools.
3. This project highlights my approach to a puzzle from intuition to solutions.


----------------------------------
II.  Folder Contents
----------------------------------

Excel:

01mod_demo.xlsx				-	small sample file, to explore the math;
								see the equations and the number patterns
02quadratic_residues.xlsx		- 	the whole data file (slow!);
								better to just open the png version
03quad_res_excel.png			- 	figure of the result!


Python:

04quadratic_residues.py		- 	the code; uses pylab (matplotlib) for figure;
								run with the python command
05quadratic_residues_py.png	-	figure of the result; same pattern, but now 
								triangular (more like Pascal's triangle)
								

JavaScript:

06quadratic_residues.html 	-	JavaScript code v1; uses D3 for figure;
								double click to run and it should open in a
								web browser
d3.min.js 					- 	dependency file for running D3 (ignore)
07white_blue_d3.png			-	figure 1; similar to the python one
08red_purple_d3.png			- 	figure 2; fun with colors
09quad_res_interactive.html	-	generates a prettier version of the figure; 
								smaller, but easier to explore the patterns; 
								shows the residue value on long mouseover
10bubbly_d3.png				- 	pretty figure output by quad_res_interactive;
								run the code in the browser to get the 
								interactive version of this figure


----------------------------------
III. The Story
----------------------------------

A few months ago, I was in an Intro to Cyber Security course and we were 
reviewing the foundation of public key cryptography, modular arithmetic. I 
played around with some numbers and began to observe patterns. After class,
I pulled up Excel to verify that the patterns continued. I also
Googled around to see what other people called this pattern and what was known.
I found the term "quadratic residues," to describe the math, but little on the
patterns. With Excel, I stuck in the formula and colored the cells by value.
Then I zoomed way out and captured the figure. I liked the result
aesthetically, but mathematically it seemed to make more sense to show the 
pattern as an isosceles triangle (like Pascal's triangle), rather than as a 
rectangle. Excel doesn't provide the option of a triangular spreadsheet, so 
I set the concept aside for a while. Then when Dave asked for a code sample,
I decided to revisit the project. 

I programmed the quadratic residue visualization in Python (using pylab/
matplotlib) and in JavaScript (using D3). Together, these implementations demo  
familiarity in these languages, proficiency in visualization, and a novel
mathematical pattern. In my computer science BS/MS, coursework was more 
focused on algorithms and research than on programming or visualization, so
this project was a nice change. If I had more time, I would have liked to 
implement a second project doing data analysis in Python. Python's pandas tool 
makes operations on the data very clean and it would have given me the chance 
to demonstrate some complementary aspects of programming (like data analysis
and algorithms). The advantage of this project, however, was that it used an 
original idea and showed my process from exploration to implementation. 


----------------------------------
IV.  Some Nice Math
----------------------------------

What is going on?

Each point is colored according to the value of y^2 mod x.
If it helps, think about Pascal's triangle, where each entry is y choose x.
This is the same idea, but with a different formula. Patterns appear because
of mathematical properties of the modulo operator.


Why is the triangle symmetrical?

Consider some point (x, y, color) with values (a, b, b^2 mod a). The 
symmetrical point on the other half of the triangle will have the same 
x value, but a y value of x - y. (There are x values per row and now you are
looking at the yth from the end, rather than yth from the beginning). This
symmetrical point is (a, a - b, (a - b)^2 mod a). 

		(a - b)^2 mod a = (a^2 - 2ab + b^2) mod a 
		= a^2 mod a - 2ab mod a + b^2 mod a = b^2 mod a
	
The first two terms in the expansion have a as a factor, so they equal zero,
and we are left with b^2 mod a, which is the same residue (and color value)
as the original point. This proves why the figure is symmetrical.


In the Excel version, what is happening to the right of the triangle?

1. 	The center of the big red diagonal is where x = y, so 

		y^2 mod x = x^2 mod x = 0.

2. 	The diagonal is wide because the adjacent values are also low numbers.
	In the previous cell, y = x - 1
	
		y^2 mod x = (x - 1)^2 mod x = (x^2 - 2x + 1) mod x = 1
		
	The first two terms cancel and the value is 1. The same math works to show 
	that cell to the right of the diagonal, where y = x + 1, is also 1. The 
	triangular versions start and end with these diagonals.
	
3. 	Each row repeats after x = y. The shallower diagonals are where y^2 mod x
	equals zero again. Values repeat every x values. For any integer n, 
	consider the point (x, y + nx, (y + nx)^2 mod x) 
	
		(y + nx)^2 mod x = (y^2 + 2ynx + (nx)^2) mod x = y^2 mod x
		
	The last two terms both have x as a factor, so irrespective of n, the value
	is just y^2 mod x. This proves the values repeat every x.
	

Is that all?

Nope! There are lots more patterns in the figure. Many can be verified using a
simple understanding of modular arithmetic, and others I have yet to explain. 
Let me know what you find!

		
		

