# Assignment

--> Problem Statment:

	Agentdesks have a lot of properties from property sellers and search requirements from property buyers which get added to a SQL database every day. Every day these multiple properties and search criteria get added through our application by agents. Write an algorithm to match these properties and search criteria as they come in based on 4 parameters such that each match has a  match percentage.

The 4 parameters are:

    Distance - radius (high weightage)
    Budget (high weightage)
    Number of bedrooms (low weightage)
    Number of bathrooms (Low weightage)

    Each match should have a percentage that indicates the quality of the match. Ex: if a property exactly matches a buyer's search requirement for all 4 constraints mentioned above, it’s a 100% match.  
    Each property has these 6 attributes - Id, Latitude, Longitude, Price, Number of bedrooms, Number of bathrooms
    Each requirement has these 9 attributes - Id, Latitude, Longitude, Min Budget, Max budget, Min Bedrooms required, Max bedroom reqd, Min bathroom reqd, Max bathroom reqd.


--> Program Detail:
	-Work for both Seller and Buyer.
	-Take detail from user(Seller/Buyer) and provide information to user
	-If user is Seller then it will take property detail and provide List of interseted Buyer.
	-If user is Buyer then it will take there requirment and provide List of likable Property
	-Currently used static data but can be used database and work with dynamic data.
	-for Scalability, each functionality is implemented in its own function. Ecah function is scalable as per requirment.   

--> Dependency : python3 and geopy, mysql library 	
--> Excute program:
	$python3 PropertyMatching.py

--> Technical Detail:
	-Python language is used to write this program
	-geopy library need to be install ($pip3 install geopy)
	-Program detail:-
		def main() :- main function /starting function in which ask for user type.
		def Seller():- function take information of seller and provide info of interested buyer.
				it also insert detail by calling InsertPropertyData(propertyDic).
				it also call Matching function :-MatchRequirment(propertyDic).
		def Buyer():- Take requirment of buyer and display list of suitable property.
				it also insert detail by calling InsertRequirmentData(requirmentDic)
				it also call Matching function MatchProperty(requirmentDic)
		
		def MatchProperty(requirmentDic):- Matching function compare requirment with database and return suitable property with percentage.
						Format :- [Id,lat,long,budget,bedroom,bathroom,percentage]
		def MatchRequirment(propertyDic):Match property detail with interseted buyer and return there list
					return format :-[id,lat,long,minbudget,maxBudget,minbedroom,maxBedroom,minBathroom,maxBathroom,percentage]
		
		def InsertPropertyData(propertyDic):-insert property data in database
		def InsertRequirmentData(requirmentDic):-#insert Data in data base with given input.
							# min or max budget is not given then store min and max with 25% up and down
							# min and max bedroom/bathroom is not given then store with +2/-2 up and down value

		

Assumtion :
	Instead of 10 mile cirlce i used 100 mile circle just for static data use

--> Could be done: Exception handling ,Database connectivity, Can be optimize as per requirment
