import os
from PIL import Image
read = "original/" # folder sa .png slikama
write = "final/" # folder gde ce se cuvati .jpg slike

names = os.listdir(read)
brojac = 0 # brojac

for name in names:

    img = Image.open(read + name) # ucitavanje slika
    name = name.split(".") # splitovanje po tacki
    
    if name[-1] == "png":
        
        name[-1] = "jpg" # definisanje formata
        name = str.join(".", name) # konvertovanje u jpg, dodavanje sufiksa .jpg 
        save_path = write + name # putanja za cuvanje 
        
        img = img.convert('RGB') # konvertovanje u RGB
        img.save(save_path) # pilow funkcija za cuvanje
        
        brojac += 1 # inkrementovanje brojaca
        print(save_path, "------Ok", brojac) # ispis povratnih informaacija u konzoli
    
    else:
 
        continue