#!usr/bin/python
#Coding: utf-8
#Coded By : MrMaNd0
import requests, json
import time
logo = """
	►*****************************************◄
   ~|      Coded By Mohamed Abd Elazeem\n     |~
   ~| https://www.facebook.com/MrMaNd0JustOne |~
    ►*****************************************◄
"""

print(logo)
print(►*****************************************◄)
print('| 1- Rating Pages With Access Token.    |')
print('| 2- Like Pages With Access Token.      |')
print('| 3- Follow Accounts With Access Token. |')
print('| 4- Likes Posts With Access Token.     |')
print('| 5- Share Posts With Access Token.     |')
print('| 6- Poking Acc With Access Token.      |')
print('| 7- Friend Request With Access Token.  |')
print('| 8- Share Posts With Page Token.       |')
print(►*****************************************◄)
ask = input('Enter Number>>')

if (int(ask) == 1):
	p_user = input('Enter Page ID >> ')
	ratings_number = input('Enter Rating Number >> ')
	access_token = input('Enter Access Tokens File >> ')
	opener = open(access_token, 'r').readlines()
	for at in opener:
		time.sleep(1)
		token = at.strip()
		url = 'https://graph.facebook.com/' +p_user+ '/ratings?Name=hector&rating=' +ratings_number+ '&access_token=' +token+ '&method=post'
		http = requests.post(url)
		content = http.content
		data = json.loads.(content.decode("utf-8"))
		print(data)
		
elif (int(ask) == 2):
	p_user = input('Enter Page ID >> ')
	access_token = input('Enter Access Tokens File >> ')
	opener = open(access_token, 'r').readlines()
	for at in opener:
		time.sleep(1)
		token = at.strip()
		url = 'https://graph.facebook.com/' +p_user+ '/likes?access_token=' +token+ '&method=post'
		http = requests.post(url)
		content = http.content
		data = json.loads.(content.decode("utf-8"))
		print(data)
		
elif (int(ask) == 3):
	acc_id = input('Enter Your Account ID >> ')
	access_token = input('Enter Access Tokens File >> ')
	opener = open(access_token, 'r').readlines()
	for at in opener:
		time.sleep(1)
		token = at.strip()
		url = 'https://graph.facebook.com/' +acc_id+ '/subscribers?access_token=' +token+ '&method=post'
		http = requests.post(url)
		content = http.content
		data = json.loads.(content.decode("utf-8"))
		print(data)
		
elif (int(ask) == 4):
	post_id = input('Enter Your Post ID >> ')
	access_token = input('Enter Access Tokens File >> ')
	opener = open(access_token, 'r').readlines()
	for at in opener:
		time.sleep(1)
		token = at.strip()
		url = 'https://graph.facebook.com/' +post_id+ '/likes?access_token=' +token+ '&method=post'
		http = requests.post(url)
		content = http.content
		data = json.loads.(content.decode("utf-8"))
		print(data)
		
elif (int(ask) == 5):
	post_id = input('Enter Your Post ID >> ')
	access_token = input('Enter Access Tokens File >> ')
	opener = open(access_token, 'r').readlines()
	for at in opener:
		time.sleep(1)
		token = at.strip()
		url = 'https://graph.facebook.com/' +post_id+ '/sharedposts?access_token=' +token+ '&method=post'
		http = requests.post(url)
		content = http.content
		data = json.loads.(content.decode("utf-8"))
		print(data)
		
elif (int(ask) == 6):
	acc_id = input('Enter Your Account ID >> ')
	access_token = input('Enter Access Tokens File >> ')
	opener = open(access_token, 'r').readlines()
	for at in opener:
		time.sleep(1)
		token = at.strip()
		url = 'https://graph.facebook.com/' +acc_id+ '/pokes?access_token=' +token+ '&method=post'
		http = requests.post(url)
		content = http.content
		data = json.loads.(content.decode("utf-8"))
		print(data)
elif (int(ask) == 7):

	acc_id = input('Enter Your Account ID >> ')
	access_token = input('Enter Access Tokens File >> ')
	opener = open(access_token, 'r').readlines()
	for at in opener:
		time.sleep(1)
		token = at.strip()
		url = 'https://graph.facebook.com/' +acc_id+ '/friendrequests?access_token=' +token+ '&method=post'
		http = requests.post(url)
		content = http.content
		data = json.loads.(content.decode("utf-8"))
		print(data)
		
elif (int(ask) == 8)
	post_id = input('Enter Your Post ID >> ')
	page_token = input('Enter Access Tokens File >> ')
	opener = open(page_token, 'r').readlines()
	for at in opener:
		time.sleep(1)
		token = at.strip()
		url = 'https://graph.facebook.com/' +post_id+ '/sharedposts?access_token=' +token+ '&method=post'
		http = requests.post(url)
		content = http.content
		data = json.loads.(content.decode("utf-8"))
		print(data)
