Minor-I ProjectThis Python project generates a 25-line ASCII art portrait of the renowned author and activist Arundhati Roy. The project demonstrates the use of coordinate logic, mathematical patterns, and control structures (loops/conditionals) to create visual art without the use of external image processing libraries.🎨 Output PreviewWhen you run the script, the following 25-line output is generated:Plaintext           
            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&            
          S&S&S&S&S&S&S&S&S&S&S&S&S&S&S&S&S&S&S&S&          
         &#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S         
        S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#        
       &#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&#S&       
       #&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#&S#       
      S&#S&#S&.....................&#S&#S&#S&#S&#S&#S       
      #&S#&S#&..~~~...~~~..S#&S#&S#&S#&S&#S&#S&#S&#S       
      S&#S&#S&...@@@.......@@@...&#S&#S&#S&#S&#S&#S&#       
      #&S#&S#&..........|........S#&S#&S#&S#&S#&S#&S#       
      S&#S&#S&..........|........&#S&#S&#S&#S&#S&#S&#       
      #&S#&S#&..........|........S#&S#&S#&S#&S#&S#&S#       
      S&#S&#S&...................&#S&#S&#S&#S&#S&#S&#       
      #&S#&S#&........=====......S#&S#&S#&S#&S#&S#&S#       
      S&#S&#S&...................&#S&#S&#S&#S&#S&#S&#       
      #&S#&:::::...........::::::S#&S#&S#&S#&S#&S#&S#       
       &#S=|=|==|=|==|=|==|=|==|=|=|==|=|==|=|#S&#S&        
        S#|=|=|==|=|==|=|==|=|==|=|=|==|=|==|=|&S#&         
         &=|=|==|=|==|=|==|=|==|=|=|==|=|==|=|==S&          
          =|=|==|=|==|=|==|=|==|=|=|==|=|==|=|==            
           |=|==|=|==|=|==|=|==|=|=|==|=|==|=|              
            =|==|=|==|=|==|=|==|=|=|==|=|==|=               
                                                            
                    Arundhati Roy
⚙️ Project ConstraintsThis project was built under the following strict constraints to test algorithmic logic rather than library usage:Output Limit: Strictly 25 lines of vertical output.No Libraries: No PIL, OpenCV, or ASCII art converters allowed.Core Logic: Must use standard Python Loops (for) and Conditional Statements (if/elif/else) only.🧠 How It WorksThe script treats the terminal window as a Cartesian coordinate system ($x, y$).The Grid: It iterates through a grid of Height 25 x Width 60.Layering Logic: For every coordinate, the script checks specific conditions in a prioritized order:Scarf: Uses Modulo arithmetic (x + y) % 2 to create a checkered pattern.Face Features: Uses exact coordinate ranges to place Eyes (@), Nose (|), and Mouth (=).Hair Geometry: Uses the circle equation $(x-h)^2 + (y-k)^2 \le r^2$ to determine the boundary of the hair. Inside this boundary, it cycles through characters (S, #, &) to simulate curly texture.Skin: Fills the remaining central area with dots (.).🚀 How to RunEnsure you have Python installed (3.x recommended).Save the code as arundhati_art.py.Run the following command in your terminal:Bashpython arundhati_art.py
📋 RequirementsPython 3.xA terminal window (monospaced font recommended for best viewing).