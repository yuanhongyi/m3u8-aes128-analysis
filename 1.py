from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(data,key,iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec_data = unpad(cipher.decrypt(data), AES.block_size)
    return dec_data


if __name__ == '__main__':
    key = bytes.fromhex('C79484DBEC26149A49DE6DE1109A37B3')
    iv  = bytes.fromhex('26AD0A5D74D67AC9BFE7A00C65B96BDB')
    # 读取本地加密ts文件
    with open('1.ts','rb') as f:
        enc_ts = f.read()
        # 解密ts
        dec_ts = decrypt(enc_ts,key,iv)
        # 将解密后的ts保存
        with open('dec.ts','wb') as ff:
            ff.write(dec_ts)
