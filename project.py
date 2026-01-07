"""
Project: Minor-I Project - Arundhati Roy ASCII Art
Author: [Your Name]
Constraint: 25 Lines of Output, using Loops and If/Else only.
"""

def draw_arundhati_compact():
    height = 25  
    width = 60   

    print(f"Generating 25-line Portrait...\n")

    for y in range(height):
        line = ""
        for x in range(width):
            
            
            if y >= 19 and (15 <= x <= 45):
            
                if (x + y) % 2 == 0:
                    char = "#"
                else:
                    char = "="
            
            # 2. FACIAL FEATURES
            elif y == 11 and ((23 <= x <= 25) or (35 <= x <= 37)):
                char = "@"
            # Eyebrows (y=10)
            elif y == 10 and ((22 <= x <= 26) or (34 <= x <= 38)):
                char = "~"
            # Nose (y=12 to 14)
            elif (12 <= y <= 14) and x == 30:
                char = "|"
            # Mouth (y=16)
            elif y == 16 and (28 <= x <= 32):
                char = "="

            # 3. FACE SKIN (The shape of the face)
            
            elif (9 <= y <= 18) and (20 <= x <= 40):
                # Chin shaping at the bottom
                if y == 18 and (x < 25 or x > 35):
                    char = ":" # Shadow on jawline
                else:
                    char = "." # Lighter skin tone

            # 4. HAIR (The Volume)
            # Arundhati's hair is big and surrounds the face.
            # We define a large area around the face coordinates.
            elif (3 <= y <= 18) and (12 <= x <= 48):
                 # Logic for circular hair shape (cutting off corners)
                 # Distance from center (30, 10)
                 dx = x - 30
                 dy = (y - 10) * 2.2 # Stretch y to make it circular
                 
                 # If inside the hair radius
                 if (dx*dx) + (dy*dy) <= 450:
                     # Textured curly hair
                     if (x * y) % 3 == 0: char = "S"
                     elif (x * y) % 3 == 1: char = "#"
                     else: char = "&"
                 else:
                     char = " " # Outside hair curl radius

            # 5. BACKGROUND
            else:
                char = " "

            line += char

        print(line)

    print(" " * 20 + "Arundhati Roy")

if __name__ == "__main__": 
    draw_arundhati_compact()