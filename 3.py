from Crypto.Cipher import AES
import os
import hashlib

def md5_32(text):
    # 创建 MD5 哈希对象
    md5_hash = hashlib.md5()
    # 将输入的字符串编码为字节流
    text_bytes = text.encode('utf-8')
    # 更新哈希对象的内容
    md5_hash.update(text_bytes)
    # 获取 32 位十六进制形式的哈希值
    md5_hex = md5_hash.hexdigest()
    return md5_hex


seed_md5 = md5_32('100')
print(seed_md5)
filename = '1.key'
# 把文件内容以byte字节形式读写到缓冲区中。
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    f.close()
    print(buf)
    return buf

# print(list(read_into_buffer(filename)))

key_key_text = seed_md5[:16].encode()
key_iv_text = bytes.fromhex("01020305070B0D1113171D0705030201")
text = read_into_buffer(filename) #需要加密的内容，bytes类型
# AES.MODE_CBC 表示模式是CBC模式
aes = AES.new(key_key_text,AES.MODE_CBC,key_iv_text) #CBC模式下解密需要重新创建一个aes对象
den_text = aes.decrypt(text)
# print("明文：\n",list(den_text))
keys = list(den_text)
hex16 = []
for i in keys[:16]:
    hex16.append(i)

def print_bytes_hex(data):
    lin = ['%02X' % i for i in data]
    for i in range(0,16):
        print(lin[i],end=' ')
        if(i ==7):
            print()

def print_bytes(data):
    lin = ['%02X' % i for i in data]
    for i in range(0,16):
        print(lin[i],end='')

# print_bytes_hex(hex16)
print_bytes(hex16)

