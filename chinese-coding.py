import sys
s = raw_input()
print s
print repr(s)
u = s.decode(sys.stdin.encoding)
print u
print repr(u)
o = u.encode(sys.stdout.encoding)