from Crypto.Cipher import AES
import base64
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



def aes_decrypt(ciphertext, key_str, iv_str):
    try:
        key = key_str.encode()
        iv = iv_str.encode()
        ciphertext_bytes = bytes.fromhex(ciphertext)
        # print(ciphertext_bytes)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(ciphertext_bytes)
        return base64.b64decode(decrypted_data.decode(encoding="utf-8"))
    except ValueError as e:
        print(f"AES decode error: {e}")
        return None
    except UnicodeDecodeError as e:
        print(f"UTF-8 decode error: {e}")
        return None


if __name__ == "__main__":

    vid = "81327783a84341a1cfa3d20163b34a64_8"
    # MD5-32 加密 vid:
    md5_vid = md5_32(vid)
    # print(md5_vid)
    # 示例的 key 和 iv，需以字符串形式提供
    key_str = md5_vid[:16]
    iv_str = md5_vid[16:]
    # print(key_str, iv_str)

    # 示例密文，以文本形式给出，这里假设是 base64 编码
    ciphertext = ""

    decrypted = aes_decrypt(ciphertext, key_str, iv_str)
    if decrypted is not None:
        # Save the decrypted data to a file
        with open('decrypted.json', 'wb') as f:
            f.write(decrypted)
            f.close()
        print('Decryption successful!')
