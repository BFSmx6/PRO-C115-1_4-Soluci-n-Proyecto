
import os
  
  
# Ruta del archivo source - (fuente)
source = 'main.txt'
  
# Ruta de archivo de destino
dest = 'newfile.txt'
  
  
# Ahora renombra la ruta source
# Ruta de destino
# Usa el método os.rename() 
os.rename(source, dest)
print("La ruta Source fue renombrada ruta de destino exitosamente.")
