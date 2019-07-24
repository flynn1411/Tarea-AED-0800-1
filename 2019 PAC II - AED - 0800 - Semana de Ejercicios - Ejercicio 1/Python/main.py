from Caja import*
from Objetos import*


caja = Caja()

print(caja.agregarFila())
print(caja.agregarObjeto(Lapiz("BIC","Mina")))
print(caja.agregarObjeto(ResmaDePapel("Copan","Carta",200)))
print(caja.agregarObjeto(Clips(1000,"Mediano")))

print(caja.agregarFila())
print(caja.agregarObjeto(Grapadora("Dell",500)))
print(caja.agregarObjeto(Grapas(6000,"Medianas")))
print(caja.agregarObjeto(Folder("Oficio","Plastico")))

print(caja.agregarFila())
print(caja.agregarObjeto(PostIts("Rosa",20)))
print(caja.agregarObjeto(Marcador("BIC","Board")))
print(caja.agregarObjeto(Borrador("Estudio","Goma")))

print(caja.agregarFila())
print(caja.agregarObjeto(Corrector("Penzoil","LiquidPaper")))
print(caja.agregarObjeto(CintaAdhesiva("Botsch","Masking")))


#caja.imprimirCaja()
#caja.primerGrupo.valor.imprimirista()
