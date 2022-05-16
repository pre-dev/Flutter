"""
Flutter
[MAY] [5/12-14] - We shut down hyper.gg's database, when you try to create an account, because we sent to many requests (we didn't even use threads, lmfao)
[MAY] [5/12-14] - Although, we still are most likely going to continue botting hyper.gg and making more tools, like follow bots, comment bots, GG bots, and more!
"""

import requests, colorama, user_agent, art
import uuid

import time, os
import re

import threading, pystyle, json, random, string
import datetime

if True:
   start_time = time.time()
   start_time

class Flutter:
      class Api:
            URL = 'https://api.mer.gg'
            URL
        
      def __init__(
          self,
      ):
          self.time = start_time
          self.time

          if True:
                self.access_token = 'bWVyZ2dfbW9iaWxlOnNlY3JldA=='
                self.access_token

          if True:
             self.proxies  = []
             self.accounts = []
             self.agents   = []


      def comment(
          self,
          username = '',
          password = '',
          comment  = '',
          postId   = '',
          mentions = [],
          replyTo  = 0,
      ):
          x = self.login(username = username, password = password)
          x

          if True:
             try:
                  r = requests.get(
                      '%s/user/current' % (Flutter.Api.URL),
                       headers     = self.get_headers(
                                     user_agent     = '%s' % (user_agent.generate_user_agent()),
                                     authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                       )
                  )

                  if r.status_code in [
                       200,
                       201,
                       203,
                       204,
                  ]:
                       y = requests.post(
                           '%s/postComment' % (Flutter.Api.URL),
                            headers = self.get_headers(
                                           user_agent     = '%s' % (user_agent.generate_user_agent()),
                                           authorization  = 'Bearer %s' % (
                                                             x[
                                                                 'access_token'
                                                             ]
                                           )
                            ), json = {
                                    'comment'      : comment,
                                    'createdOn'    : self.get_time(),
                                    'mentions'     : mentions,
                                    'postId'       : postId,
                                    'replyToPostId': replyTo,
                                    'userId'       : r.json()['id']
                            }
                       )

                       if True:
                          return y.json()
                  else:
                     if True:
                        return {'error': r.json()}
                       
             except Exception as E:
                    if True:
                       if True:
                          return E
                         
      def like_comment(
          self,
          username = '',
          password = '',
          commentId = ''
      ):
          x = self.login(username = username, password = password)
          x

          if True:
             try:
                  r = requests.get(
                      '%s/user/current' % (Flutter.Api.URL),
                       headers     = self.get_headers(
                                     user_agent     = '%s' % (user_agent.generate_user_agent()),
                                     authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                       )
                  )

                  if r.status_code in [
                       200,
                       201,
                       203,
                       204,
                  ]:
                     y = requests.post(
                         '%s/postCommentLikes' % (Flutter.Api.URL),
                          headers = self.get_headers(
                                              user_agent     = '%s' % (user_agent.generate_user_agent()),
                                              authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                              ), json  = {
                                       'postCommentId': commentId,
                                       'userId'       : r.json()['id']
                              }
                     )

                     if True:
                        return y.json()
                  else:
                     if True:
                        return r.json()
             except Exception as E:
                    return E

      def like(
          self,
          username = '',
          password = '',
          postId   = '',
      ):
          x = self.login(username = username, password = password)
          x

          if True:
             try:
                  r = requests.get(
                      '%s/user/current' % (Flutter.Api.URL),
                       headers     = self.get_headers(
                                     user_agent     = '%s' % (user_agent.generate_user_agent()),
                                     authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                       )
                  )

                  if True:
                     y = requests.post(
                              '%s/likes' % (Flutter.Api.URL),
                               headers = self.get_headers(
                                              user_agent     = '%s' % (user_agent.generate_user_agent()),
                                              authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                              ), json  = {
                                       'postId': postId,
                                       'userId': r.json()['id']
                              }
                     )

                     if True:                                      
                        if y.status_code in [
                             200,
                             201,
                             203,
                             204,
                        ]:
                             return y.json()
                        else:
                           if True:
                              return y.json()
             except Exception as E:
                    print (E)

      def view(
          self, 
          username = '',
          password = '',
          postId   = '',
      ):
          x = self.login(username = username, password = password)
          x

          if True:
             try:
                  r = requests.get(
                      '%s/user/current' % (Flutter.Api.URL),
                       headers     = self.get_headers(
                                     user_agent     = '%s' % (user_agent.generate_user_agent()),
                                     authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                       )
                  )

                  if True:
                     y = requests.get(
                         '%s/post/%s?requestorUserId=%s' % (
                             Flutter.Api.URL, postId, r.json()['id']
                         ), headers = self.get_headers(
                                           user_agent     = '%s' % (user_agent.generate_user_agent()),
                                           authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                           )
                     )

                     if True:
                        return y.status_code
             except Exception as E:
                    return E
                
      def gglike(
          self,
          username = '',
          password = '',
          postId   = '',
      ):
          x = self.login(username = username, password = password)
          x

          if True:
             try:
                  r = requests.get(
                      '%s/user/current' % (Flutter.Api.URL),
                       headers     = self.get_headers(
                                     user_agent     = '%s' % (user_agent.generate_user_agent()),
                                     authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                       )
                  )

                  if True:
                     y = requests.post(
                              '%s/gglikes' % (Flutter.Api.URL),
                               headers = self.get_headers(
                                              user_agent     = '%s' % (user_agent.generate_user_agent()),
                                              authorization  = 'Bearer %s' % (
                                                       x[
                                                          'access_token'
                                                        ]
                                     )
                              ), json  = {
                                       'postId': postId,
                                       'userId': r.json()['id']
                              }
                     )

                     if True:                                      
                        if y.status_code in [
                             200,
                             201,
                             203,
                             204,
                        ]:
                             return y.json()
                        else:
                           if True:
                              return y.json()
             except Exception as E:
                    print (E)
               
      def login(
          self,
          username = '',
          password = '',
      ):
          if True:
             try:
                r = requests.post(
                    '%s/oauth/token' % (Flutter.Api.URL),
                     headers = self.get_headers(
                               user_agent    = '%s' % (user_agent.generate_user_agent()),
                               authorization = 'Basic %s' % (self.access_token)
                     ), data = {
                             'grant_type'   : 'password',
                             'username'     :  username,
                             'password'     :  password,
                     }
                )

                if r.status_code in [
                   200,
                   201,
                   203,
                   204,
                ]:
                   return r.json()
                else:
                   if True:
                      return r.json()
             except Exception as E:
                return {
                         'error': E
                }

      def get_time(
              self,
      ):  
              if True:
                 return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-4] + 'Z'
                
      def get_number (
              self, 
              country_code = random.choice([
                             '817', '682'
              ])
      ):
                  return '%s' % (country_code) + ''.join(str(random.randint(0, 9)) for x in range(7))
     
      def get_proxies(self, proxy_type, proxy):
          return {
                    '%s://' % (proxy_type): '%s://%s' % (proxy_type, proxy)
          }
        
      def get_headers(self, user_agent, authorization = ''):
          if authorization == '':
             return {
                    'Accept'         : 'application/json, text/plain, */*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection'     : 'keep-alive',
                    'User-Agent'     : user_agent
             }
          else:
             if True:
                return {
                       'Accept'         : 'application/json, text/plain, */*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection'     : 'keep-alive',
                       'User-Agent'     : user_agent,
                       'Authorization'  : authorization
                }

      def follow(self, user_id, username, password):
          if True:
             x = self.login(username = username, password = password)
             x

          resp = requests.get(
                          '%s/user/current' % (Flutter.Api.URL),
                           headers = {"Authorization": 'Bearer %s' % (x['access_token'])} 
          )

          if resp.status_code in [
                  200,
                  201,
                  203,
                  204,
          ]:
                  r = requests.post(
                               '%s/following' % (Flutter.Api.URL),
                                headers = {
                                        'Authorization': 'Bearer %s' % (x['access_token'])
                                }, json = {
                                        'followsId'  : user_id,
                                        'userId'     : resp.json()['id'],
                                }
                  )

                  if True:
                     return r.json()
          else:
              return resp.text
            
      def create_account(
          self,
          username,
          password,
          phone_number,
          referral_code = ''
      ):
          if self.agents == []:
             if True:
                self.agents += ["".join(user_agent.generate_user_agent()) for x in range(10)]
                self.agents

          if self.proxies == []:
             r = requests.post(
                 '%s/user' % (Flutter.Api.URL),
                  headers = self.get_headers(
                            user_agent = random.choice(self.agents),
                  ), json = {
                          'email'       : None,
                          'password'    : password,
                          'phoneNum'    : phone_number,
                          'referralCode': referral_code,
                          'username'    : username
                  }              
             )

             if True:
                if r.status_code in [
                     200,
                     201,
                     203,
                     204,
                ]:
                     if True:
                        return r.json()
                else:
                     if (
                          True
                     ):
                          return {
                                   'Error': r.json()
                          }
          else:
             if True:
                r = requests.post(
                    '%s/user' % (Flutter.Api.URL),
                     headers    = self.get_headers(
                                  user_agent = random.choice(
                                               self.agents
                                  ),
                     ), proxies = self.get_proxies(
                                        proxy_type = 'http', 
                                        proxy      = random.choice(
                                                            self.proxies
                                                     )
                        ), json = {
                               'email'       : None,
                               'password'    : password,
                               'phoneNum'    : phone_number,
                               'referralCode': referral_code,
                               'username'    : username
                           }
                )

                if r.status_code in [
                     200,
                     201,
                     203,
                     204,
                ]:
                     if True:
                        return r.json()
                else:
                     if (
                          True
                     ):
                          return {
                                   'Error': r.json()
                          }

      def reload_agents (self, file_path):
          if True:
             for proxy in open(file_path, 'r').readlines():
                 proxy

                 if True:
                    self.proxies += [proxy.strip()]
                    self.proxies

                 if True:
                    pass
                   
      def reload_proxies(self, file_path):
          if True:
             for proxy in open(file_path, 'r').readlines():
                 proxy

                 if True:
                    self.proxies += [proxy.strip()]
                    self.proxies

                 if True:
                    pass

while True:
      os.system('clear')
      os

      if True:
         art.tprint('Flutter')
         art

         if True:
            print ('-----------')
            if True:
               print  ('[%s1%s] Generate' % (colorama.Fore.RED, colorama.Fore.RESET))
               print  ('[%s2%s] Follow' % (colorama.Fore.RED, colorama.Fore.RESET))
               print  ('[%s3%s] GG Likes' % (colorama.Fore.RED, colorama.Fore.RESET))
               print  ('[%s4%s] Comment Likes' % (colorama.Fore.RED, colorama.Fore.RESET))
               print  ('[%s5%s] Post Likes' % (colorama.Fore.RED, colorama.Fore.RESET))
               print  ('[%s6%s] View Bot' % (colorama.Fore.RED, colorama.Fore.RESET))
               print  ('[%s7%s] Comment\n' % (colorama.Fore.RED, colorama.Fore.RESET))

               if True:
                  x = input('[@]: ')
                  x

               if x == '1':
                  os.system('clear')
                  os

                  if True:
                     art.tprint('Flutter')
                     art

                  print ('-----------')
                  print

                  if True:
                     if True:
                        name_length   = input('[@] Name Length  : ')
                        referral_code = input('[@] Referral Code: ')
                        webhook       = input("[@] Webhook URL  : ")

                        try:
                           int(name_length)
                           int
                        except:
                           name_length = 9
                           name_length

                        try:
                           while True:
                                 username = "".join(random.choice(string.ascii_letters) for x in range(int(name_length)))
                                 password = "".join(random.choice(string.ascii_letters) for x in range(8))
                                 number   =    Flutter().get_number()

                                 if True:
                                    main = Flutter()
                                    main

                                    if True:
                                       x = main.create_account(
                                           username     = username,
                                           password     = password,
                                           phone_number = number, referral_code = referral_code
                                       )

                                       try:
                                          print ('[@] Account Created [%s:%s]' % (x['username'], password))
                                          print

                                          with open('flutter/accounts', 'a+') as accounts:
                                               accounts.write('%s:%s\n' % (username, password))
                                               accounts

                                               if webhook != '':
                                                  requests.post(
                                                           webhook,
                                                           json = {
                                                                'embeds': [
                                                                        {
                                                                           'title'      : 'Account Generated [hover.gg]',
                                                                           'description': 'https://discord.gg/socialboosts | https://discord.gg/combat',

                                                                           'fields'     : [
                                                                                      {
                                                                                        'name'     : 'Username', 'value': '```\n%s```' % (username), 
                                                                                        'inline'   : True
                                                                                      }, {
                                                                                                'name'  : 'Password',
                                                                                                'value' : '```\n%s```' % (password),
                                                                                                'inline': True
                                                                                      }, {
                                                                                                'name'  : 'Data',
                                                                                                'value' : '```\n%s```' % (x),
                                                                                                'inline': False
                                                                                      }
                                                                           ]
                                                                        }
                                                                ]
                                                           }
                                                  )
                                       except Exception as E:
                                          if True:
                                             print ('[-] Account Failure (%s)' % (E))
                                             print
                        except Exception as E:
                               if True:
                                  print(E)
                                  print
                                 
                               print('[@] Generator Closed'), input('')
                               print
               else:
                  if x == '2':
                     x

                     if True:
                        os.system('clear')
                        os

                        if True:
                           art.tprint('Flutter')
                           art

                     user_id = input('[@] User ID: ')
                     main    = Flutter()

                     for user in open('flutter/accounts', 'r').readlines():
                         user

                         if True:
                            try:
                                print(
                                     main.follow(
                                          user_id  = user_id, 
                                          username = user.strip().split(":")[0], 
                                          password = user.strip().split(":")[1]
                                     )
                                )
                            except:
                                print ('[@] Cannot Follow [%s]' % (user.strip().split(":")[0]))

                     if True: input('')
                     if True: pass
                  else:
                     if True:
                        if x == '3':
                           os.system('clear')
                           os
                              
                           if True:
                              art.tprint('Flutter')
                              art

                              if True:
                                 postId = input('[@] Post ID: ')
                                 postId
                                
                           if True:
                              for account in open('flutter/accounts', 'r').readlines():
                                  account

                                  if True:
                                     main = Flutter()
                                     main
                                    
                                     print (
                                             main.gglike(
                                                  username = account.strip().split(":")[0],
                                                  password = account.strip().split(":")[1],
                                                  postId   = int(postId)
                                             )
                                     )
                              input('')
                        else:
                            if x == '4':
                               os.system('clear')
                               os

                               if True:
                                  art.tprint('Flutter')
                                  art

                               if True:
                                  comment_id = input('[@] Comment ID: ')
                                  comment_id

                                  for account in open('flutter/accounts', 'r').readlines():
                                      if True:
                                         print (
                                                 Flutter().like_comment(
                                                           username    = account.strip().split(":")[0],
                                                           password    = account.strip().split(":")[1],
                                                           commentId   = comment_id                                                   
                                                 )
                                         )
                                  input('')
                            else:
                               if x == '5':
                                  os.system('clear')
                                  os

                                  if True:
                                     art.tprint('Flutter')
                                     art

                                     if True:
                                        postId = input('[@] Post ID: ')
                                        postId

                                        if True:
                                           for account in open('flutter/accounts', 'r').readlines():
                                               account

                                               if True:
                                                  print (
                                                        Flutter().like(
                                                                  username = account.strip().split(":")[0],
                                                                  password = account.strip().split(":")[1],
                                                                  postId   = postId
                                                        )
                                                  )
                                           input('')
                               else:
                                  if x == '6':
                                     os.system('clear')
                                     os

                                     if True:
                                        art.tprint('Flutter')
                                        art

                                        if True:
                                          postId = input('[@] Post ID: ')
                                          postId

                                        for account in open('flutter/accounts', 'r').readlines():
                                            account

                                            if True:
                                               view = Flutter().view(
                                                      username = account.strip().split(":")[0], 
                                                      password = account.strip().split(":")[1],
                                                      postId   = postId
                                               )

                                               if view in [
                                                       200,
                                                       201,
                                                       203,
                                                       204,
                                               ]:
                                                  print ('[%s@%s] Viewed [%s] with [%s]' % (
                                                          colorama.Fore.LIGHTGREEN_EX,
                                                          colorama.Fore.RESET, postId, account.strip().split(":")[0]
                                                  ))
                                               else:
                                                  if True:
                                                     print('[%s@%s] Error [%s | %s]' % (colorama.Fore.RED, colorama.Fore.RESET, account.strip().split(":")[0], view))

                                        input('')
                                  else:
                                     if x == '7':
                                        if True:
                                           os.system('clear')
                                           os

                                           if True:
                                              art.tprint("Flutter")
                                              art

                                           if True:
                                              if True:
                                                 postId    = input('[@] Post Id : ')
                                                 replyTo   = input('[@] Reply To: ')
                                                 comment   = input('[@] Comment : ')

                                                 
                                              for account in open('flutter/accounts', 'r').readlines():
                                                  account

                                                  if True:
                                                     print(
                                                           Flutter().comment(
                                                                     username = account.strip().split(":")[0],
                                                                     password = account.strip().split(":")[1],
                                                                     comment  = comment,
                                                                     postId   = postId,
                                                                     replyTo  = replyTo
                                                           )
                                                     )
                                              input('')
