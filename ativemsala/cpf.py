def cpfvalido (cpf: str):
if type(cpf) != srt:
  return false
cpf = cpf.replace('.','').replace('.','')
if cpf.isdecimal() == False:
    return False
    if len(cpf) !=11:
      return False
  soma = 0
  for pos in range(10):
soma += int(cpf[pos])* (11- pos)
dv = 11 - soma % 11
if dv1 > = 10:
dv1 = 0
if dv1 != int(cpf[10]):
  return False
return True
  *input fora da função.
cpf = ....
print('cpf é valido:', cpf_valido(cpf)
