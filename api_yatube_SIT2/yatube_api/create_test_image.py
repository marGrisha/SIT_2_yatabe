from PIL import Image
from io import BytesIO


img = Image.new('RGB', (100, 100), color='red')
img.save('test_image.jpg', 'JPEG')
print("✅ test_image.jpg создан!")
