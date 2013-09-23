def parse_username(username):
  name = []
  for letter in username[1:]:
    name.append(ord(letter))
  name.append(0)
  return name

def xor_l2r(key_list, username):
  key_circle = key_list
  key_len = len(key_circle)
  key_index = 0
  ulen = len(username)  
  ct = [0] * ulen
  for i in range(ulen):
    l = username[i]
    k = key_circle[key_index]
    c = l^k
    ct[i] = c
    key_circle[key_index]=l

    key_index += 1
    if key_index == key_len: key_index = 0
  return ct

def xor_r2l(key_list, username):
  key_circle = key_list
  key_len = len(key_circle)
  key_index = 0
  ulen = len(username)
  ct = [0] * ulen
  for i in reversed(range(ulen)):
    l = username[i]
    k = key_circle[key_index]
    c = l^k
    ct[i] = c
    key_circle[key_index]=l

    key_index += 1
    if key_index == key_len: key_index = 0
  return ct

def add_r2l(key_list, username):
  key_circle = key_list
  key_len = len(key_circle)
  key_index = 0
  ulen = len(username)  
  ct = [0] * ulen
  for i in range(ulen):
    l = username[i]
    k = key_circle[key_index]
    c = (l+k)&0xFF
    key_circle[key_index]=(c)

    key_index += 1
    if key_index == key_len: key_index = 0
  return key_circle

def div(key_list):
  divisor = 0xA
  key_circle = key_list
  answer = []
  combine = ''
  remainder = None
  mul = 0x10**6
  a = key_list[0]*mul
  mul = 0x10**4
  b = key_list[1]*mul
  mul = 0x10**2
  c = key_list[2]*mul  
  d = key_list[3]
  numerator = (a+b+c+d)

  while ((numerator & numerator) != 0):
    remainder = numerator%divisor
    numerator = numerator/divisor
    answer.append(remainder+0x30)
  return answer

def be2le(hex_list):
  data = []
  for item in reversed(hex_list):
    data.append(item)
  return data

def numberFlip(hex_list):
  data = ''
  for item in reversed(hex_list):
    data = data + chr(item)
  return data

name = parse_username('mynameisjc')

r1 = xor_l2r([0xAA, 0x89, 0xC4, 0xFE, 0x46], name)
r2 = xor_r2l([0x78, 0xF0, 0xD0, 0x03, 0xE7], r1)
r3 = xor_l2r([0xF7, 0xFD, 0xF4, 0xE7, 0xB9], r2)
r4 = xor_r2l([0xB5, 0x1B, 0xC9, 0x50, 0x73], r3)
a1 = add_r2l([0x00, 0x00, 0x00, 0x00], r4)
d1 = div(be2le(a1))
print numberFlip(d1)


# for i in a1:
#   print hex(i)

#print "\nr1 legit:\n0xd3\n0xe7\n0xa5\n0x93\n0x23\n0x10\n0x1d\n0xb\n0xe\n0x65"
#print "\nr2 legit:\n0xC3\n0xFA\n0xAE\n0x9D\n0x46\n0xF7\n0x1E\n0xDB\n0xFE\n0x1D"
#print "\nr3 legit:\n0x34\n0x5A\n0xFA\n0x7A\n0xFF\n0x34\n0xE4\n0x75\n0x63\n0x5B"
#print "\nr4 legit:\n0x"

