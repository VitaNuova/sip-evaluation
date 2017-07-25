import binascii

with open('team3', 'r+b') as f:
	f.seek(0x477f)
	# f.write(hex("! H A C K E D !"))
	# m = b'! H A C K E D !'
	# x = binascii.hexlify(m)
	# f.write(x)
	f.write(b'!  H A C K E D  !')
	f.seek(0x46a2)
	f.write(b'8888')
