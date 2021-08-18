# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''#aguia = ["vertebrado", "ave", "carnivoro", "aguia"]
#pomba = ["vertebrado", "ave", "onivoro", "pomba"]
#homem = ["vertebrado", "mamifero", "onivoro", "homem"]
#vaca = ["vertebrado", "mamifero", "herbivoro", "vaca"]
#pulga = ["invertebrado", "inseto", "hematofago", "pulga"]
#lagarta = ["invertebrado", "inseto", "herbivoro", "lagarta"]
#sanguessuga = ["invertebrado", "anelideo", "hematofago", "sanguessuga"]
#minhoca = ["invertebrado", "anelideo", "onivoro", "minhoca"]

animais = [["vertebrado", "ave", "carnivoro", "aguia"], 
           ["vertebrado", "ave", "onivoro", "pomba"],
           ["vertebrado", "mamifero", "onivoro", "homem"],
           ["vertebrado", "mamifero", "herbivoro", "vaca"],
           ["invertebrado", "inseto", "hematofago", "pulga"],
           ["invertebrado", "inseto", "herbivoro", "lagarta"],
           ["invertebrado", "anelideo", "hematofago", "sanguessuga"],
           ["invertebrado", "anelideo", "onivoro", "minhoca"]]

a = ""; b = ""; c = ""

a = input()
b = input()
c = input()

for k in animais:
  if(a == k[0] and b == k[1] and c == k[2]):
    print(k[3])
