# >>> Importação <<<
import time
# <<<<< -------------------- >>>>>

# >>> Definições <<<
class Inscricao:
    def __init__(self, periodo, curso, grau, matricula):
        self.p = periodo
        self.c = curso
        self.g = grau
        self.m = matricula

    def __str__(self):
        return ("Período: %s; Curso: %-22s; Grau: %5.2f; Matrícula: %s"
                %(self.p,self.c,float(self.g),self.m))

    def __lt__(self, outra):
        pass

def bubbleSort(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-j-1):
            if float(lista[i].p) > float(lista[i+1].p):
                lista[i], lista[i+1] = lista[i+1], lista[i]
            elif float(lista[i].p) == float(lista[i+1].p):
                if lista[i].c.lower() > lista[i+1].c.lower():
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                elif lista[i].c == lista[i+1].c:
                    if float(lista[i].g) < float(lista[i+1].g):
                        lista[i], lista[i+1] = lista[i+1], lista[i]
                    elif lista[i].g == lista[i+1].g:
                        if lista[i].m > lista[i+1].m:
                            lista[i], lista[i+1] = lista[i+1], lista[i]

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if float(lefthalf[i].p) < float(righthalf[j].p):
                alist[k]=lefthalf[i]
                i=i+1
            else:
                while True:
                    if float(lefthalf[i].p) == float(righthalf[j].p):
                        if lefthalf[i].c.lower() < righthalf[j].c.lower():
                            alist[k]=lefthalf[i]
                            i=i+1
                            break
                        elif lefthalf[i].c.lower() == righthalf[j].c.lower():
                            if float(lefthalf[i].g) > float(righthalf[j].g):
                                alist[k]=lefthalf[i]
                                i=i+1
                                break
                            elif float(lefthalf[i].g) == float(righthalf[j].g):
                                if float(lefthalf[i].m) < float(righthalf[j].m):
                                    alist[k]=lefthalf[i]
                                    i=i+1
                                    break
                    alist[k]=righthalf[j]
                    j=j+1
                    break
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
# <<<<< -------------------- >>>>>

# >>> SCRIPT <<<                  
start = time.time()

ARQUIVO = open("XYZ999.txt", "r")

inscricoes = []

for linha in ARQUIVO.readlines():
    m, c, p, g = linha.split(',')
    g = g.strip('\n')
    insc = Inscricao(p, c, g, m)
    inscricoes.append(insc)

ARQUIVO.close()

print("Tempo para ler = {0:.5f}s".format(time.time() - start))

mergeSort(inscricoes)

print("Tempo para organizar = {0:.5f}s".format(time.time() - start))

output = open("XYZ999(Organizado).txt", "w+")
soma_grau_total = 0
soma_grau_cursos = [[0,0],[0,0],[0,0]]
reprovacoes = 0
reprovados = []
aprovados = []
dicio_periodos = {}

for i in inscricoes:
    output.write("%s,%s,%s,%s\n"%(i.p, i.c, i.g, i.m))
    
    soma_grau_total += float(i.g)

    if i.c[-1] == "l":
        soma_grau_cursos[0][0] += 1
        soma_grau_cursos[0][1] += float(i.g)
    elif i.c[-1] == "o":
        soma_grau_cursos[1][0] += 1
        soma_grau_cursos[1][1] += float(i.g)
    elif i.c[-1] == "a":
        soma_grau_cursos[2][0] += 1
        soma_grau_cursos[2][1] += float(i.g)

    if float(i.g) < 5:
        reprovacoes += 1
        reprovados.append(i.m)
    else:
        aprovados.append(i.m)

    if i.p not in dicio_periodos:
        dicio_periodos[i.p] = float(i.g)
    else:
        dicio_periodos[i.p] += float(i.g)

    #print(i)
    
output.close()

media_geral = soma_grau_total / len(inscricoes)
media_civil = soma_grau_cursos[0][1]/soma_grau_cursos[0][0]
media_producao = soma_grau_cursos[1][1]/soma_grau_cursos[1][0]
media_mecanica = soma_grau_cursos[2][1]/soma_grau_cursos[2][0]
maior_media = max(dicio_periodos, key=dicio_periodos.get)
menor_media = min(dicio_periodos, key=dicio_periodos.get)
con_aprovados = set(aprovados)
con_reprovados = set(reprovados)
desistencias = con_reprovados.difference(con_aprovados)

info = open("info_XYZ999.txt", "w+")

info.write("Média Geral da disciplina: %.2f\n"%media_geral)
info.write("Grau Médio Eng. Civil: %.2f\n"%media_civil)
info.write("Grau Médio Eng. de Produção: %.2f\n"%media_producao)
info.write("Grau Médio Eng. Mecânica: %.2f\n"%media_mecanica)
info.write("Período com maior Grau Médio: %s\n"%maior_media)
info.write("Período com menor Grau Médio: %s\n"%menor_media)
info.write("Percentual de reprovações: %.2f%% (%d de %d)\n"%((reprovacoes/len(inscricoes)*100), reprovacoes, len(inscricoes)))
info.write("Desistências: %d\n"%len(desistencias))

info.close()

print("Tempo para criar arquivos = {0:.5f}s".format(time.time() - start))

print("Tempo total de execução = {0:.5f}s".format(time.time() - start))
input("Digite Enter para encerrar.")
# <<<<< -------------------- >>>>>
