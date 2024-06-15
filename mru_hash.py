import hashlib

h = hashlib.sha1()
h.update(b'mrCloud')

l = 0
with open( "c:\\path\\to\\big_file.txt", "rb" ) as f:
    b = f.read( 1024*1024 )
    while b:
        h.update( b )
        l += len(b)

        b = f.read(1024 * 1024)

print( "Len: " + str(l) )
h.update( str.encode(str(l)) )

d = h.digest()

print( d.hex().upper() )