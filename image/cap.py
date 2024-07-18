import random
from PIL import Image, ImageDraw

def generate_captcha_image(width, height):
    captcha_image = Image.new('RGB', (width, height), (255, 255, 255))
    captcha_draw = ImageDraw.Draw(captcha_image)

    # Define the desired order of shapes
    shape_order = ['rectangle', 'circle', 'triangle','triangle','circle','rectangle']  # Modify as desired
    random.shuffle(shape_order)
    shape_width = width // len(shape_order)
    
    captcha_text = ''
    for i, shape_name in enumerate(shape_order):
        if shape_name == 'rectangle':
            x1 = i * shape_width
            y1 = 0
            x2 = (i + 1) * shape_width
            y2 = height
            captcha_draw.rectangle([(x1, y1), (x2, y2)], fill=random_color(), outline=random_color())
            captcha_text += 'R'
        
        elif shape_name == 'circle':
            x = i * shape_width
            y = 0
            r = shape_width // 2
            captcha_draw.ellipse([(x, y), (x + r, y + r)], fill=random_color(), outline=random_color())
            captcha_text += 'C'
        
        elif shape_name == 'triangle':
            x1 = i * shape_width
            y1 = 0
            x2 = (i + 1) * shape_width
            y2 = height
            x3 = random.randint(x1, x2)
            y3 = random.randint(y1, y2)
            captcha_draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=random_color(), outline=random_color())
            captcha_text += 'T'
    
    return captcha_image, captcha_text

# Rest of the code remains the same as before

# Function to generate a random color
def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Example usage:
width = 200
height = 100
length = 5
captcha_image, captcha_text = generate_captcha_image(width, height)
captcha_image.show()  # Display the captcha image

# Verify the captcha
user_input = input('Enter the captcha text: ')
if user_input == captcha_text:
    print('Captcha verification successful!')
else:
    print('Captcha verification failed.')
