from geopy.distance import geodesic
import mysql.connector

#database connection function
def database_connector():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="database"
        )
        return mydb
    except:
        print("Cannot Connect to Database")
        return None

def InsertRequirmentData(requirmentDic):

	#insert Data in data base with given input.
	# min or max budget is not given then store min and max with 25% up and down
	# min and max bedroom/bathroom is not given then store with +2/-2 up and down value
	pass

def InsertPropertyData(propertyDic):
	#insert property data in database
	pass

#	Match property detail with interseted buyer and return there list
def MatchRequirment(propertyDic):

	#add sql server connection
	#
	#mydb = databse_connector()
	#myCursor = mydb.cursor()
	#myCursor.excute("select optimize Query")
	#output should be list | requirmentList = SQL_output
	
	#static data
	requirmentList = [[1,23.0,75.0,2500000,3000000,2,3,2,4],[2,23.05,75.06,1500000,2500000,3,4,2,3],[3,24.05,75.01,1500000,1800000,1,2,1,2]]

	result=[]

	#find interested buyer
	for requirment_info in requirmentList:
		origin = (propertyDic['latitude'],propertyDic['longitude'])  # (latitude, longitude) don't confuse
		nearbyRequirment = (requirment_info[1], requirment_info[2])
		dist = geodesic(origin, nearbyRequirment).miles # function to calculate distance
		print("\n" )
		print("Distance from given location ")
		print(dist)

		if(dist <= 100):
			percent=0;
			if(dist <=2):
				percent+=30;
			if(propertyDic['budget'] >=requirment_info[3] and propertyDic['budget'] <=requirment_info[4]):
				percent+=30;
			if(propertyDic['bathroom'] >= requirment_info[7] and propertyDic['bathroom'] <= requirment_info[8]):
				percent+=20;
			if(propertyDic['bedroom'] >= requirment_info[5] and propertyDic['bedroom'] <= requirment_info[6]):
				percent+=20;
			if(percent >= 40):
				requirment_info.append(percent)
				result.append(requirment_info)
	return result # format :-[id,lat,long,minbudget,maxBudget,minbedroom,maxBedroom,minBathroom,maxBathroom,percentage]

# Matching function compare requirment with database and return suitable property with percentage
def MatchProperty(requirmentDic):

	#add sql server connection
	#
	#mydb = databse_connector()
	#myCursor = mydb.cursor()
	#myCursor.excute("select optimize Query")
	#output should be list | propertyList = SQL_output
	
	#static data
	propertyList =[[1,23.0,75.0,2500000,2,2],[2,23.05,75.06,2000000,2,3],[3,24.05,75.01,1500000,3,4]]
	result =[]

	# Find favrable property
	for property_info in propertyList:
		origin = (requirmentDic['latitude'],requirmentDic['longitude'])  # (latitude, longitude) don't confuse
		nearbyProperty = (property_info[1], property_info[2])
		dist = geodesic(origin, nearbyProperty).miles # function to calculate distance
		print("\n" )
		print("distance from given location")
		print(dist)
		if(dist <= 100):
			percent=0;
			if(dist <=2):
				percent+=30;
			if(property_info[3] >=requirmentDic['minBudget'] and property_info[3] <=requirmentDic['maxBudget']):
				percent+=30;
			if(property_info[5] >= requirmentDic['minBathroom'] and property_info[5] <= requirmentDic['maxBathroom']):
				percent+=20;
			if(property_info[4] >= requirmentDic['minBedroom'] and property_info[4] <= requirmentDic['maxBedroom']):
				percent+=20;
			if(percent >= 40):
				property_info.append(percent)
				result.append(property_info)
	return result # Format :- [Id,lat,long,budget,bedroom,bathroom,percentage]

# Take requirment of buyer and display list of suitable property  
def Buyer():
	print("Please provide Your requirment data\n")
	print("If you auto fill click 1 or for manual click 2\n")
	x= input()
	if(x=='1'):
		latitude = 23.02
		longitude= 76.2
		minBudget= 1500000
		maxBudget= 2000000
		minBedroom=	2
		maxBedroom=	3
		minBathroom=2
		maxBathroom=3
	else:
		latitude = float(input("Please enter latitude "))
		longitude= float(input("Please enter longitude "))
		minBudget= int(input("Please enter minimum budget "))
		maxBudget= int(input("Please enter max budget "))
		minBedroom=int(input("Please enter min bedroom "))
		maxBedroom=int(input("Please enter max bedroom "))
		minBathroom=int(input("Please enter min bathroom "))
		maxBathroom=int(input("Please enter max bathroom "))

	requirmentDic = {'latitude':latitude,'longitude':longitude,'minBudget':minBudget,'maxBudget':maxBudget,'minBedroom':minBedroom,'maxBedroom':maxBedroom,'minBathroom':minBathroom,'maxBathroom':maxBathroom}
	print(requirmentDic)
	#insert data
	InsertRequirmentData(requirmentDic)
	#find property
	propertyList =MatchProperty(requirmentDic)
	#print property
	print("Final List\n")
	print(propertyList)
	print("\n")


#function take information of seller and provide info of interested buyer
def Seller():
	print("Please provide Your Property detail\n")

	print("If you auto fill click 1 or for manual click 2\n")
	x= input()
	if(x=='1'):
		latitude = 23.02
		longitude= 76.2
		budget= 1500000
		bedroom=	2
		bathroom=	2
	else:
		latitude = float(input("Please enter latitude "))
		longitude= float(input("Please enter longitude "))
		budget= int(input("Please enter budget "))
		bedroom=int(input("Please enter bedroom "))
		bathroom=int(input("Please enter bathroom "))

	propertyDic ={'latitude':latitude,'longitude':longitude,'budget':budget,'bedroom':bedroom,'bathroom':bathroom}
	
	#insert Data
	InsertPropertyData(propertyDic)
	#find buyer
	intrestedBuyer = MatchRequirment(propertyDic)
	#print intersted buyer detail
	print("Final List")
	print(intrestedBuyer)
	print("\n")

#main function /starting function
def main():
	

	while(1):
		print("click 1 if you are Buyer\nClick 2 if you are Seller\n")
		ch = input();
		if(ch =='1'):
			Buyer()
		elif (ch == '2'):
			Seller()
		else:
			print("Please enter Correct input\n")


if __name__ == '__main__':
	main()