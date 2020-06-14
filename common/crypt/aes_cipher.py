# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   Description: aes对称加密
   Author: hushutao
   Create_Date: 2020/3/17
-------------------------------------------------
"""

import uuid
import base64
from Crypto.Cipher import AES


class AesCipher(object):
    def __init__(self, key):
        self.key = key
        self.length = AES.block_size
        self.cryptor = AES.new(self.key.encode("utf-8"), AES.MODE_ECB)

    def encrypt(self, content):
        ciphertext = self.cryptor.encrypt(self.pad(content).encode('utf-8'))
        return base64.b64encode(ciphertext)

    def decrypt(self, data):
        decode = base64.b64decode(data)
        cryptor = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        plain_text = cryptor.decrypt(decode)
        return self.unpad(plain_text)

    def pad(self, text):
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def unpad(self, text):
        return text[0:-ord(text[-1:])]

    @staticmethod
    def generate_16key():
        return str(uuid.uuid1()).replace('-', '')[:16]
