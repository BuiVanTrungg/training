import requests
import json
import pymongo

## make a struct to store information crawled
class Infor:
  def __init__(self,link_fb,link_img,name,address,company):
    self.link_fb = link_fb
    self.link_img = link_img
    self.name = name
    self.address = address
    self.company = company
    
  def display(self):
    print("Link facebook: "+ str(self.link_fb))
    print("Link image: "+ str(self.link_img))
    print("Name: "+ self.name)
    print("Address: "+ self.address)
    print("Company: "+ self.company)
start = 0
length = 50
total = 2
# link = "https://timkh.com/wp-admin/admin-ajax.php?action=movie_datatables&draw=2&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=50&length=50&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1542627623628", {"credentials":"include","headers":{"accept":"application/json, text/javascript, */*; q=0.01","accept-language":"en-US,en;q=0.9","x-requested-with":"XMLHttpRequest"},"referrer":"https://timkh.com/","referrerPolicy":"no-referrer-when-downgrade","body":null,"method":"GET","mode":"cors"}
# link = "https://timkh.com/wp-admin/admin-ajax.php?action=movie_datatables&draw=3&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start="+str(start)+"&length="+str(length)+"&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1542617840233"
link = "https://timkh.com/wp-admin/admin-ajax.php?action=movie_datatables&draw=3&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=50&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1542700779449"
response = requests.get(link)
# get datas - a dict
# datas = json.loads(response.text)
# list_data.update(datas)
# print(datas == list_data)
# print(len(list_data))
# make a list to store all infor
# list_infor =[]


# for i in range(total):
#   start = length*i
#   response = requests.get(link)
#   # get data
#   datas = json.loads(response.text)
#   for j in range(len(datas['data'])):
#     # 0: img
#     # 1: ignore
#     # 2: name
#     # 3: address
#     # 4: company
    
#     img_ele = datas['data'][j][0].split('"')
#     link_img = img_ele[7]
#     name = datas['data'][j][2]
#     address = datas['data'][j][3]
#     company = datas['data'][j][4]
#     conv = link_img.split('graph.')
#     link_fb = 'https://'+conv[1][0:-18]
    
    
    
#     add = Infor(link_fb,link_img,name,address,company)
#     list_infor.append(add)
    
    
    
# for i in list_infor:
#   i.display()
# print(len(list_infor))

myclient = pymongo.MongoClient(port=27017)


mydb = myclient["mydatabase"]

# print(myclient.list_database_names())
mycol = mydb["customers"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)
# dblist = myclient.list_database_names()
# print(myclient.list_database_names())
# if "mydatabase" in dblist:
#   print("The database exists.")
# print(x.inserted_id)