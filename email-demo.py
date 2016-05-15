#!/usr/bin/python3

# send email demo

import smtplib # 导入email smtp模块
from email.mime.text import MIMEText
from email.header import Header

class emailObj:

	def __init__(self):
		self.host = "smtp.aliyun.com"
		self.port = 25
		self.user = "l@aliyun.com"
		self.password = "aaaa"
		self.sender = "l@aliyun.com"
		self.receivers = ["8579@qq.com"]

	def sendEmailText(self):
		# message = {}

		message = MIMEText("This is a my first email.", "plain", "utf-8")

		message["To"] = Header("599@qq.com", "utf-8")
		message["Form"] = Header("ls@aliyun.com", "utf-8")
		message["Subject"] = Header("my subject you yes", "utf-8")

		try:
			smtp_obj = smtplib.SMTP()
			conn_status = smtp_obj.connect(self.host, self.port)	# 连接邮箱服务器
			# print(conn_status)

			login_status = smtp_obj.login(self.user, self.password)  # 登录
			# print(login_status)

			print(message.as_string())
			sended_status = smtp_obj.sendmail(self.sender, self.receivers, message.as_string())

			# print(sended_status)

			print("sendmail success")

		except smtplib.SMTPException as e:
			print(str(e))
			print("sendmail failed")

	def sendEmailHtml(self):
		message["To"] = "lymos qq"

		# message = MIMEText(html, "html", "utf-8")  发送HTML格式

	def sendEmailAttach(self):
		message["Form"] = "lymoslymos"

		'''
			添加附件所需操作
		form email.mime.multipart import MIMEMultipart
		message = MIMEMultipart()
		attach = MIMEText(open(file_name, "rb").read(), "base64", "utf-8")
		attach["Content-Type"] = "application/octet-stream"
		attach["Content-Disposition"] = "attachment; filename=fileName"

		message.attach(attach)
		'''

	def sendEmailWithImage(self):
		message["To"] = "lymos qq"
		# from email.mime.image import MIMEImage


# 实例化类
instance = emailObj()
instance.sendEmailText()

