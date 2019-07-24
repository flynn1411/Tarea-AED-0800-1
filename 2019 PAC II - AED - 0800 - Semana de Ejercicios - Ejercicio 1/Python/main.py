# -*- coding: "utf-8" -*-

from Objetos import*
from Caja import*

caja = Caja()


print(caja.agregarObjeto(Lapiz("Stadtleder", "grafito")))
print(caja.agregarObjeto(ResmaDePapel("Copán", "Carta", 500)))
print(caja.agregarObjeto(Clips(50, "S")))

print(caja.agregarObjeto(Grapadora("Patito", 30)))
print(caja.agregarObjeto(Grapas(30, "M")))
print(caja.agregarObjeto(Folder("Carta", "Manila")))

print(caja.agregarObjeto(PostIts("Rosa", 50)))
print(caja.agregarObjeto(Marcador("BiC", "Permanente")))
print(caja.agregarObjeto(Borrador("BiC", "Goma")))

print(caja.agregarObjeto("NiñoSinVacunar"))

print(caja.primerGrupo.siguiente.siguiente.valor.primero.valor.tipo)