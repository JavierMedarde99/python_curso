from pathlib import Path


base = Path.home()
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(guia)
print(guia2)
print(guia.parent.parent)

guia = Path(Path.home(),"Europa")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)

guia = Path("Europa","España","Barcelona", "SagradaFamilia.txt")

en_europa = guia.relative_to(Path("Europa"))

en_espania = guia.relative_to(Path("Europa","España"))

print(en_europa)

print(en_espania)