from PIL import Image
img = Image.open('R.png').convert('L')
img.save('greyscale.png')
print("Success!")