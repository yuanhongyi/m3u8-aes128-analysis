# m3u8-aes128-analysis

Analysis for 32byte key AES128 encryption of Polyv for .ts file in hls
对某利威加密的视频逆向分析，适用于【蓝铅笔】等平台

> 本人仅对视频加密方式感兴趣，并没有对视频进行传播，仅供学习交流使用

分析过程见[analysis.md](analysis.md)

`1.py` turn encrypted .ts file to decrypted .ts file
`1.py` 将加密的.ts文件转换为解密的.ts文件

`2.py` decrypt the json file
`2.py` 解密json文件

`3.py` decrypt the ts key
`3.py` 解密ts文件的key

并非自动化脚本，只是逆向逻辑，有需要的请自行完善！
