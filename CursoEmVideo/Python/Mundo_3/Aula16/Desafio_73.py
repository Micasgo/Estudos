"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B)Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense.
"""
	
times = ("Botafogo","Chapecoense","Vitória","São Paulo","Fluminense","Mirassol","Bahia",
"Athletico","Bragantino","Palmeiras","Atlético","Vasco","Grêmio","Corinthians","Flamengo",
"Internacional","Coritiba","Santos","Remo","Cruzeiro")

print("\n","-=-="*30,f"\nOs primeiros 5 colocados são: {times[:6]}\n","-=-="*30)
print("\n","-=-="*30,f"\nOs últimos 4 colocados são: {times[-4:]}\n","-=-="*30)
print("\n","-=-="*30,f"\nTimes em ordem Alfabética: {sorted(times)}\n","-=-="*30)
print("\n","-=-="*30,f"\nChapecoense está em {times.index("Chapecoense")+1}° lugar\n","-=-="*30)