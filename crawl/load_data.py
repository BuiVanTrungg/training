import pymongo


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


list_infor = []
# main
load = open("data.txt","r")
count = 0
# initial
name = ""
link_fb = ""
link_img = ""
address = ""
company = ""
for line in load.readlines():
    if count == 0:
        name = line
        count = count + 1
    elif count == 1:
        link_fb = line
        count = count + 1
    elif count == 2:
        link_img = line
        count = count + 1
    elif count == 3:
        address = line
        count = count + 1
    elif count == 4:
        company = line
        count = count + 1
    elif count == 5:
        add = Infor(link_fb,link_img,name,address,company)
        list_infor.append(add)
        count = 0
    else:
        break
    # print (line)
load.close()


# print(len(list_infor))
# for i in list_infor:
#     i.display()



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = []
for i in list_infor:
    add = {"name":i.name,"link_fb":str(i.link_fb) ,"link_img":str(i.link_img),"address":i.address,"company":i.company}
    mylist.append(add)
	#x = mycol.insert_one(add)     
	# mylist.append(add)
#print(mylist)
x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
# print(x.inserted_ids)
# y = mycol.find_one()
# print(y)
# for i in mycol.find():
#     print (i)

# myquery ={"address": "Ho Chi Minh City, Vietnam\n"}

# mydoc = mycol.find(myquery)
# for i in mydoc:
#     print (i)

# print(mydb.list_collection_names())
# mydict = { "name": "Peter", "address": "Lowstreet 27" }

# x = mycol.insert_one(mydict)

# print(x.inserted_id)
# collist = mydb.list_collection_names()
# if "customers" in collist:
#   print("The collection exists.")
# # print(myclient.list_database_names())

# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")
