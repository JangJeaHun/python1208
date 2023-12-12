from rembg import remove
from PIL import Image

input_path = '1.뉴진스.jpg'
output_path = '1.뉴진스_배경제거.png'

input_ = Image.open(input_path)
output_ = remove(input_)
output_.save(output_path)