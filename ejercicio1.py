# class en minisula y el objeto con la primera en mayusculas 
class Moto:
    
    marca="BMW"
    modelo="BSX"
    color="NEGRO"
    
    def acelerar (self, km):
        print("acelerando a {0}km".format(km))
        
vehiculo= Moto()

print(vehiculo.modelo)
print(vehiculo.marca)    
print(vehiculo.color)   
