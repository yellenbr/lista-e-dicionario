p = 10
while p == 10 :
  print(" 1 - criar lista ")
  print(" 2 - criar dicionário ")
  print(" 3 - fechar programa ")
  p1 = input(" digite o número da sua opção : ")
  if p1 == "1" :
    lista = []
    while p == 10 :
      print(" 1 - adicionar itens a lista ")
      print(" 2 - remover itens da lista ")
      print(" 3 - imprimir lista completa ")
      print(" 4 - sair dessa função ")
      p2 = input(" qual sua opção : ")
      if p2 == "1" :
        adc = input(" : ")
        lista.append(adc)
      elif p2 == "2" :
        rmv = input(" : ")
        if rmv in lista :
          lista.remove(rmv)
        else :
          print(" esse item não está na lista ")
      elif p2 == "3" :
        print(lista)
      elif p2 == "4" :
        break
      else :
        print(" digite uma opção válida ")
  elif p1 == "2" :
    dicionario = {}
    while a == 10 :
      print(" 1 - adicionar pares chaves ao dicionário ")
      print(" 2 - remover pares chaves do dicionário ")
      print(" 3 - imprimir dicionário ")
      print(" 4 - sair dessa função ")
      op3 = input(" qual sua opção : ")
      if p3 == "1" :
        chave = input(" qual a chave : ")
        valor = input( " valor : ")
        dicionario[chave] = valor
      elif p3 == "2" :
        rmv = input(" qual a chave do par que deseja remover : ")
        if rmv in dicionario :
          del dicionario[rmv]
        else :
          print(" esse chave não existe")
      elif p3 == "3" :
        print(dicionario)
      elif p3 == "4" :
        break
      else :
        print(" digite uma opção válida ")
  elif p1 == "3" :
    break
  else :
    print(" digite uma opção válida ")