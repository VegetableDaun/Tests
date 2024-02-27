class keyword_cipher(object):
    def __init__(self, abc, keyword):
        key_dublicate = ''
        for i in keyword:
            if i not in key_dublicate:
                key_dublicate += i
        keyword = key_dublicate

        cipher_abc = keyword + ''.join([i for i in abc if i not in keyword])
        self.encode_abc = dict(zip(list(abc), list(cipher_abc)))
        self.decode_abc = dict(zip(list(cipher_abc), list(abc)))

    def encode(self, plain):
        encode_plain = ''
        for i in plain:
            encode_plain += self.encode_abc.get(i, i)
        return encode_plain

    def decode(self, ciphered):
        decode_ciphered = ''
        for i in ciphered:
            decode_ciphered += self.decode_abc.get(i, i)
        return decode_ciphered


abc = "abcdefghijklmnopqrstuvwxyz"
key = "keyword"
cipher = keyword_cipher(abc, key)

print(cipher.encode("abc"), "key")
print(cipher.encode("xyz"), "vxz")
print(cipher.decode("key"), "abc")
print(cipher.decode("vxz"), "xyz")
