import base64

#base64 encode
raw_str = 'abc'
print(raw_str)
byte_str = bytes(raw_str,'utf-8')
print(byte_str)

encoded_str = base64.b64encode(byte_str)
print(encoded_str)


#base64 decode
decode_byte_str=base64.b64decode(encoded_str)
print(decode_byte_str)

print(decode_byte_str.decode())