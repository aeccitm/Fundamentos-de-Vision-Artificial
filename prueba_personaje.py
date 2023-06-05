import Personaje as ps

#1
p = ps.Jugador("Jack", "m", 0, 5, 100)
e = ps.Enemigo("Cid", "m", 0, 0, 80)
#2
p.golpear(e)
p.golpear(e)
p.moverDerecha(10)
p.moverAbajo(5)
#3
e.golpear(p)
e.golpear(p)
p.recogerBotiquin()
#4
p.usarBotiquin()
p.usarBotiquin
p.golpear(e)
p.golpear(e)
p.golpear(e)
#5
e.golpear(p)
e.golpear(p)
#6
p.golpear(e)
p.golpear(e)
#7
p.golpear(e)




print("El nombre del jugador es: ", p.nombre)
print("Sexo: ", p.sexo) 
print("Posición en X: ", p.posicionX)
print("Posición en Y: ", p.posicionY)
print("Damage: ", p.damage)
print("Vida: ", p.vida)
print("numero de botiquines: ", p.numeroBotiquines)

print("El nombre del enemigo es: ", e.nombre)
print("Sexo: ", e.sexo) 
print("Posición en X: ", p.posicionX)
print("Posición en Y: ", p.posicionY)
print("Damage: ", p.damage)
print("Vida: ", e.vida) 
print("Evoluciones aplicadas: ", e.evolucionesAplicadas)
print("Resistencia: ", e.resistencia)






