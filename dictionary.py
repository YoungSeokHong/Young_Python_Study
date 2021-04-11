# 사전(dictionary)
# key-value pair (키-값 쌍)
my_dictionary = {
   5 : 25,
   2 : 4,
   3 : 9
}

print(type(my_dictionary))
print(my_dictionary[3])
my_dictionary[9] = 81
print(my_dictionary)

my_family = {
   '엄마' : '박미영',
   '아빠' : '홍기혁',
   '형' : '홍범석',
   '나' : '홍영석'
}
print(my_family['나'])
print('김민태' in my_family.values())