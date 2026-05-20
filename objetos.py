"""
c#
class Perro{
    public string raza {get;set;}
    public string edad {get;set;}
    
    public Perro(){
        this.edad = 1;
    }
    public Perro(string raza){
        this.raza = raza;
        this.edad = 1;
    }
    public string ToString(){
        return $"{this.raza} de {this.edad} años"
    }
    public void Ladrar(){
        Console.WriteLine($"{this.raza} dice guau")
    }
}

Perro p = new Perro();
Perro q = new Perro("Chuguagua");
q.Ladrar()
"""
#python POO

class Perro:

    #"Constructor"
    def __init__(self, raza =""):
        self.edad = 1
        self.raza = raza
    def __str__(self):
        return f"{self.raza} de {self.edad} años"
    def ladrar (self):
        print (f"{self.raza} dice guau")
 
p = Perro()
print (p)
q = Perro("CHIGUAGUA")
print(q)
q.ladrar()