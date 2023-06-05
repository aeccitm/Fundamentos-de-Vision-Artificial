import math

class Personaje:
  def __init__(self,nombre, sexo, posicionX, posicionY, damage):
    self.nombre = nombre
    self.sexo = sexo
    self.posicionX = posicionX
    self.posicionY = posicionY
    self.damage = damage
    self.vida = 100
  def golpear(self, p):
    p.vida -= self.damage/self.calcularDistanciaRespectoPersonaje(p)
  def recibirImpacto(self, d):
    self.vida -= d
    
  def calcularDistanciaRespectoPersonaje(self,p):
      return math.sqrt((self.posicionX-p.posicionX)**2 + (self.posicionY-p.posicionY)**2)
      

class Jugador(Personaje):
  numeroBotiquines = 0
  def moverDerecha(self,d):
    self.posicionX += d  
  def moverIzquierda(self, d):
    self.posicionX -= d    
  def moverArriba(self,d):
    self.posicionY += d    
  def moverAbajo(self, d):
    self.posicionY -= d    
  def recogerBotiquin(self):
    self.numeroBotiquines += 1
    
  def usarBotiquin(self):
    if self.numeroBotiquines > 0:
      v = 100-self.vida
      if self.vida <= 90:
        self.numeroBotiquines -=1
        self.vida += 5
        
      elif self.vida > 90 and self.vida < 100:
        self.vida += v
        self.numeroBotiquines -=1
        
      else:
        self.vida = 100
        print("No necesita botiquin ")  
    else:
      print("No tiene botiquines")
  def golpear(self,p):
      p.vida -= self.damage/self.calcularDistanciaRespectoPersonaje(p)
      p.evolucionar()
       
      
class Enemigo(Personaje):
  evolucionesAplicadas = 0
  resistencia = 1
  def evolucionar(self):
    if self.vida <= 30 and self.evolucionesAplicadas == 0:
      self.damage += 20 
      self.evolucionesAplicadas += 1
    elif self.vida <= 10 and self.evolucionesAplicadas == 1:
      self.resistencia += 1
      self.evolucionesAplicadas +=1
  def recibirImpacto(self, d):
      self.vida -= d/self.resistencia

    
