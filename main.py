import requests, os
v,n=0,0
for user in open('Users.txt','r').read().splitlines():
    try:
        req = requests.post('https://quack.duckduckgo.com/api/auth/signup', files={'user':(None, user.split('.')[0]),'email':(None, 'ep7dyt@gmail.com'),'disable_secure_reply':(None, '1'),'dry_run':(None, '1'),}, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','referer' : 'http://www.sitename.com'})
        if '"status":"valid"' in req.text: print(f"[VALID] {user.split('.')[0]}"); v+=1 ; open('Valid.txt','a').write(user+'\n')
        elif '"error":"unavailable_username"' in req.text: n+=1
    except Exception as e: print(f"[ERROR] {e} - User: {user}")
    os.system(f'title Not taken - {v} / Taken - {n}')