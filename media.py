nota1= float(input("Digite sua primeira nota: "))
nota2= float(input("Digite sua segunda nota: "))
media= float((nota1 + nota2)/2)

if media >= 9.0:
  conceito= "A"
elif media >= 7.5 and media < 9:
  conceito= "B"
elif media >= 6.0 and media < 7.5:
  conceito= "C"
elif media >= 4.0 and media < 6.0:
  conceito= "D"
else :
  conceito= "E"

if conceito == "A" or conceito == "B" or conceito == "C":
  situacao= "APROVADO"
else :
  situacao= "REPROVADO"

print(f"""
Primeira nota: {nota1}
Segunda nota: {nota2}
Média: {media}
Conceito: {conceito}
O aluno(a) está {situacao}
      """)