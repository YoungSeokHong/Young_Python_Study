with open('read_file_example\chicken.txt', 'r', encoding='UTF-8') as f:
   print(type(f))
   for line in f:
      # strip
      print(line.strip())
