
import os
  
  
# Ruta del archivo de origen.
source = 'main.txt'
  
# Ruta de archivo de destino
dest = 'newfile.txt'
  
  
# Ahora renombra la ruta de origen
# Ruta de destino
# Usa el método os.rename() 
os.rename(source, dest)
print("La ruta de origen fue renombrada ruta de destino exitosamente.")
