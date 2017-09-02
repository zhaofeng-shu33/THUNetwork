import hashlib
import sys
class THUNetwork:
    main_url='http://net.tsinghua.edu.cn/';
    def get_encrypted_pw(self,unencrypted_pw):
        md5=hashlib.md5()
        md5.update(unencrypted_pw.encode('utf-8'))
        return md5.hexdigest()
    def __init__(self,pyversion,username='',password=''):
        self.login_data={'action':'login','username':username,'password':'{MD5_HEX}'+self.get_encrypted_pw(password),'ac_id':'1'}
        self.logout_data={'action':'logout'}
        self.pyversion=pyversion        
    def login(self):
        if(self.pyversion=='3'):
            import urllib        
            import urllib.parse
            import urllib.request        
            postdata=urllib.parse.urlencode(self.login_data).encode('utf-8')
            request=urllib.request.Request(self.main_url+'do_login.php',postdata)
            f=urllib.request.urlopen(request)
            print(f.read().decode('utf-8'))
        else:
            import urllib        
            postdata=urllib.urlencode(self.login_data)
            f=urllib.urlopen(self.main_url+'do_login.php',postdata)
            print(f.read())
    def logout(self):
        if(self.pyversion=='3'):
            import urllib        
            import urllib.parse
            import urllib.request        
            postdata=urllib.parse.urlencode(self.logout_data).encode('utf-8')
            request=urllib.request.Request(self.main_url+'do_login.php',postdata)
            f=urllib.request.urlopen(request)
            print(f.read().decode('utf-8'))
        else:
            import urllib        
            postdata=urllib.urlencode(self.logout_data)
            f=urllib.urlopen(self.main_url+'do_login.php',postdata)
            print(f.read())        
def usage():
    print("usage: python THUNetwork.py username password login")
    print("or: python THUNetwork.py logout")


if __name__ == '__main__':
    if(len(sys.argv)<2):
        usage();
        exit(0);
    if(sys.argv[1]=='logout'):
        THUNetwork_Instance=THUNetwork(sys.version[0]);
        THUNetwork_Instance.logout();
        exit(0);
    elif(sys.argv[1]=='login' and len(sys.argv)==4):
        THUNetwork_Instance=THUNetwork(sys.version[0],sys.argv[2],sys.argv[3]);
        THUNetwork_Instance.login();
    else:
        usage();
