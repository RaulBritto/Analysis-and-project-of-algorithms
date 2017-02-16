#! /usr/bin/python

from math import log10
from random import randint
import sys
import time


tamanho = input()
x=[None]*tamanho

for i in range(0,tamanho):
  x[i] = input()


###############################################################################
def bucketsort(list):                             #bucket sort
  n = len(list)
  max_v = max(list)
  min_v = min(list)
  bucket_range = 100
  bucket = [[]]* n

  for x in xrange(n): 
    index = int(map(list[x], min_v, max_v, 0, n-1))
    bucket[index] = bucket[index] + [list[x]]

  for x in xrange(n):
    if len(bucket[x]) <= 100:       # ver a lista eh pequena, caso sim usa o insertion, caso contrario o quick
      insertion_sort(bucket[x])
    else:
      quickSort(bucket[x])

  list = []                     #cria uma lista vazia
  for i in xrange(n):
    for j in bucket[i]:
      list.append(j)            #ordena
      print j
  return list
###############################################################################
def map(x, in_min, in_max, out_min, out_max):               # funcao de calcular o bucket
  return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
#############################################################################
def insertion_sort(lista):                        #insertion sort
  for i in range(1,len(lista)):
    #print 'i = '+str(i)
    key = lista[i]
    k = i
    while k > 0 and key < lista[k - 1]:
      lista[k] = lista[k - 1]
      k -= 1
    lista[k] = key
##############################################################################
def quickSort(lista):                                 # quick sort
    quickSortHelper(lista,0,len(lista)-1)

def quickSortHelper(lista,primeiro,ultimo):
  if primeiro<ultimo:

    splitpoint = partition(lista,primeiro,ultimo)

    quickSortHelper(lista,primeiro,splitpoint-1)
    quickSortHelper(lista,splitpoint+1,ultimo)


def partition(lista,primeiro,ultimo):
  primeiroValor = lista[primeiro]

  ladoEsquerdo = primeiro+1
  ladoDireito = ultimo

  done = False
  while not done:

    while ladoEsquerdo <= ladoDireito and lista[ladoEsquerdo] <= primeiroValor:
      ladoEsquerdo = ladoEsquerdo + 1

    while lista[ladoDireito] >= primeiroValor and ladoDireito >= ladoEsquerdo:
      ladoDireito = ladoDireito -1

    if ladoDireito < ladoEsquerdo:
      done = True
    else:
      temp = lista[ladoEsquerdo]
      lista[ladoEsquerdo] = lista[ladoDireito]
      lista[ladoDireito] = temp

  temp = lista[primeiro]
  lista[primeiro] = lista[ladoDireito]
  lista[ladoDireito] = temp

  return ladoDireito 
##############################################################################

def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for  i in aList:
      tmp = i / placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX

##################################################################################

maximo = max(x)

digitos = len(str(maximo))
if digitos <= 5: 
	
	minimo = min(x)					#	acha o menor valor do vetor

	if minimo < 0:
		minimo = minimo*(-1)

	for i in range(0,tamanho):		#	translacao do vetor
		 x[i] = x[i]+minimo
	radixsort(x)					# chama a funcao
	for i in range(0,tamanho):  	#	subtrai o o minimo de todos os valores do vetor
		x[i] = x[i]-minimo

	for i in xrange(0,len(x)):		#	imprime o vetor ordenado 
		print	x[i]
else:
	bucketsort(x)


