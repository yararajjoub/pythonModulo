# Hanterar räknaren åt oss, skapar en range obj

################################################
i = 100
while i < 200:
    print(i)
    i = i + 5  # Öka med 5 varje gång
print()
################################################
# for(i, i < 200, i+10) samma ex I JAVA

for i in range(100, 200, 10):  # Startvärde, CONDITION/"Range", Ökar med "nått" efter varje iteration
    print(i)
print()
# Exakt samma som exemplet ovan med While-loop
###############################################

for i in range(0, 20, 1):  # (Start, Stop, Step)
    print(i)
print()

""" Man kan också ha endast två parametrar (start, stop)"""
for i in range(0, 10):  # Starta med 0, avsluta innan 10
    print(i)
print()
""" Man kan också ha endast en parameter som betyder (STOP), default startvärde med noll """
for i in range(10):  # Startar räkna med 0, ökar varje gång med 1 och sista värdet blir 9
    print(i, end=' ')
print()
###############################################
""" Man kan ha negativ steg, dvs iterera Bakåt istället för framåt."""
""" START MÅSTE VARA STÖRRE ÄN STOP """
for i in range(100, 0, -10):  # Notera att 0 inkluderas inte utan sista värdet kommer att vara 10
    print(i)
print()
##############################################
n = 4
for i in range(n):  # n=4
    for j in range(n):  # n=4
        print(i + j, end=' ')
    print()
"""
i + j
i = 0

# Första iteration (i)
j = 0 + 0 = 0 # output 0 # range n, n = 4, default 1
j = 1 + 0 = 1 # 2:a iteration
j = 2 + 0 = 2 # 3.e iteration
j = 3 + 0 = 3 # 4:e iteration

# Andra iterationen, (i)
 i = 1,
    J = 0
j = 0 + 1 = 1 ## 1:a iteration
j = 1 + 1 = 2 ## 2:a iteration
j = 2 + 1 = 3 ## 3:e iteration
j = 3 + 1 = 4 ## 4:e iteration

# Tredje iterationen, (i)
 i = 2,
  J = 0
j = 0 + 2 = 2 
j = 1 + 2 = 3
j = 2 + 2 = 4
j = 3 + 2 = 5

# Fjärde iterationen,(i) 
 START i = 3,
  START J = 0
j = 0 + 3 = 3
j = 1 + 3 = 4
j = 2 + 3 = 5
j = 3 + 3 = 6
"""



