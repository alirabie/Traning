import urllib.request,json
class Webservice :
    def call_vendors(self,path):
        url="https://www.hurrybunny.com/{}".format(path)
        data= urllib.request.urlopen(url)
        response = json.loads(data.read().decode("utf-8"))
        return response['vendors']

def main():
    webservice = Webservice()
    print(webservice.call_vendors("api/vendors/"))



if __name__ == '__main__': main()