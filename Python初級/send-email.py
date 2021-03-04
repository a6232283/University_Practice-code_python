#準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="smileabc30832777@gmail.com"
msg["To"]="a6232283@g.pccu.edu.tw"
msg["Subject"]="你好，阿佐"

#寄送純文字內容
msg.set_content("hello jason")

#寄送比較多樣式內容(html)
# msg.add_alternative("<h3>哈摟</h3>你好帥",subtype="html")

#連線到SMTP Server,驗證寄件人身分並發送郵件
import smtplib
#到網路上尋找Gmail smtp sever
Server=smtplib.SMTP_SSL("smtp.gmail.com",465)
Server.login("smileabc30832777@gmail.com","d30832777")
Server.send_message(msg)
Server.close()