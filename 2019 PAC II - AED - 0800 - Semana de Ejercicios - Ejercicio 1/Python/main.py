from Caja import*
from Objetos import*


caja = Caja()

print(caja.agregarFila())
print(caja.agregarObjeto(Lapiz("BIC","Mina")))
print(caja.agregarObjeto(ResmaDePapel("Copan","Carta",200)))
print(caja.primerGrupo.valor.obtenerLongitud())
print(caja.agregarObjeto(Clips(2000,"Mediano"),1))

print(caja.agregarFila())
print(caja.agregarObjeto(Grapadora("Dell",500)))
print(caja.agregarObjeto(Grapas(6000,"Medianas")))
print(caja.agregarObjeto(Folder("Oficio","Plastico"), 1))

print(caja.agregarFila())
print(caja.agregarObjeto(PostIts("Rosa",20)))
print(caja.agregarObjeto(Marcador("BIC","Board")))
print(caja.agregarObjeto(Borrador("Estudio","Goma")))

print(caja.agregarFila())
print(caja.agregarObjeto(Corrector("Penzoil","LiquidPaper")))
print(caja.agregarObjeto(CintaAdhesiva("Botsch","Masking"), 0))


caja.imprimirCaja()