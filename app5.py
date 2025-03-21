from pathlib import Path
path = Path('ecommerce')
print(path.exists())

path = Path('emails')
if(path.exists()):
    path.rmdir()
else:
    path.mkdir()
    
path = Path()

for file in path.glob('*.py'):
    print(file)



