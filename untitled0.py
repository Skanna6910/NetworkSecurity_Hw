# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPyAcDAJmCP9JabUJGEK8ARQC658IXyi
"""

#ENCRYPTION
from numpy import matrixlib
import math
import numpy

UID = "118406473"
FirstName = "Suprajha"
LastName = "Kanna"

def row_trans_enc(msg,key):
  key_len = len(key)
  key_list = list(key)
  msg_list = list(msg)
  msg_len = int(len(msg))
  k_ptr = 0

  col = len(key)
  row = int(math.ceil(msg_len/col))
  print("ENCRYPTION")
  #print('\n')
  print("The message displayed as list: ",msg_list)
  print("The message length: ",msg_len)
  print("The key list is displayed as: ",key_list)
  print("The key length is: ",col)

  CT = ""

  print("The row & col value is...",row,col)

  pad_val = int((row*col)-msg_len)
  print("The padding value is found to be: ",pad_val)
  #msg_padded = msg_list.extend('_' * pad_val)
  msg_padded = msg + pad_val * 'X'
  msg_padded_list = list(msg_padded)
  print("Message with padding dispalyed as list: ",msg_padded_list)
  #print('\n')

  orderlist = numpy.argsort(key_list)
  matrix = []
  matrix = [msg_padded_list[i: i + col]
              for i in range(0, len(msg_padded_list), col)]
  print("The matrix is written as:", matrix)

  for x in orderlist:
    for y in range(0,len(matrix)):
      CT += matrix[y][x]
  return CT

msg = "ATTACKPOSTPONEDUNTILTWOAM"
key = "4312567"
encrypted_val = row_trans_enc(msg,key)
print("The encrypted cipher text value is... ",encrypted_val)

                                                        #DECRYPTION

def row_trans_dec(msg1,key1):
  print('\n')
  print('\n')
  key1_len = len(key1)
  key1_list = list(key)
  #key_int = int(key)
  #print("int key is..",key_int)
  msg1_list = list(msg1)
  msg1_len = int(len(msg1))
  k_ptr = 0
  msg_ptr = 0

  col1 = int(math.ceil(msg1_len/key1_len))
  row1 = len(key1)
  PT = ""
  print("DECRYPTION")
  print("The ciphertext displayed as list: ",msg1_list)
  print("The ciphertext length: ",msg1_len)
  print("The key list is displayed as: ",key1_list)
  print("The key length is: ",col1)

  a = list(map(int, key1_list))
  print("The row & col value is...",row1,col1)
  Pad_x_regions = (row1*col1) - len(msg)
  print("The extra padding inside matrix..",Pad_x_regions)
  orderlist1 = numpy.argsort(key1_list)
  print("The key order list is..",orderlist1)

  dec_matrix = []
  dec_matrix = [msg1_list[i: i + col1]
              for i in range(0, len(msg1_list), col1)]
  print("The dec_matrix is written as:", dec_matrix)


  for d in range(col1):
      for j in range(row1):
       PT = PT + dec_matrix[a[j]-1][d]
  return PT

  #col_new = 0
  #row_new = 0
  #for s in msg1:
    #PT[col_new] += s
   # col_new += 1

    #if((col_new == col1) or (col_new == col1-1) and (row_new == row1 - Pad_x_regions)):
    #  col_new = 0
     # row_new += row_new

msg1 = "TTNAAPTMTSUOAODWCOIXKNLXPETX"
key1 = "4312567"
decrypted_val = row_trans_dec(msg1,key1)
print("The decrypted cipher text value is... ",decrypted_val)



