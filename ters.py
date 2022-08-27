# Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak: # input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]

inputt = [[1, 2], [3, 4], [5, 6, 7]]


def reverseList(input):
   for i in input:
    if isinstance(i, list):
        reverseList(i)
        i = i.reverse()
    else:
        inputt.reverse()


reverseList(inputt)

inputt

