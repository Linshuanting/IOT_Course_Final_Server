# IOT Server、Mysql、ejs Server 

## 編譯環境
### Centos8


---

## Python Server
此Python會建立一個 Server：用來與各位手機作連接，當各位手機付帳後，獲得結帳的訊息，會傳到該Server作處理。
處理方式：
- 從Client端會傳入一筆Json檔案，裡面有：身分認證，來判斷該資料的可靠性、使用者資訊，尋找該使用者的資料庫、結帳資料，需存入DataBase的資料。
- 透過winuser做與資料庫的連線，並將使用者做為關鍵字，來尋找使用者的Table。(考慮到安全問題，winuser的db使用權限只能查看與寫入特定資料庫)
- 找到該使用者Table後，做Mysql語法的寫入，將獲得的資料填入Database中。
- 當使用者端想要同步該手機與資料庫資料時，可以向PyServer提取資料，Server會根據Json格式裡的資料向Client做回傳。

### JSON檔案內容
```json 
yourdata = {
            # 這裡需要將資料寫入
            # 範例格式如下:
            'identity': "raspberryPi",
            'user': 'people',
            'action': 'POST',
            'goods': 'driver',
            'price': 40,
            'category': '水果',
            'spendTime': '12/27',
            'remark': 'driver pie'
}
```
---
## Mysql
1. 使用者以及使用者表格
[Imgur](images/sqltable01.png)
2. 商品資料表格
[Imgur](images/sqltable02.png)
---

## Docker
使用docker做容器化，可將PyServer、Mysql、NodeJs作封裝，來到達輕量級服務，並可在任意裝置做簡單架設，做小型晨發。
- 使用DockerFile 做Container initialize，將需要的文件存入該Container中
- 使用Docker-Compose 做Container Build，以方便Server重複建立以及更改，並可以上傳到Docker Hub [My Docker Hub](https://hub.docker.com/)
---

## Node Js
使用Node Js以及ejs做後端可視化界面，並使用Express API做簡單網頁架設，以達到人性化操作模式
1. 可以看到User以及對應table
[Imgur](images/ejs01.png)
2.	可以看到User買過的商品
[Imgur](images/ejs01.png)