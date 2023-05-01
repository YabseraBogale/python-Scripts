from pprint import pprint
Date=[31,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
standardRoomPrices=[182.16, 202, 202, 202, 170.74, 170.74, 170.74, 227, 227, 189.75, 189.75, 189.75, 170.79, 189, 210]
executiveRoomPrices=[250.47, 278, 278, 278, 239.1, 239.1, 239.1, 303.6, 303.6, 265, 265, 265, 240, 264, 290]
presidentialRoomPrices=[523.71, 578, 578, 578, 512, 512, 512, 607, 607, 570, 570, 570, 512, 550, 595]
kingBedPrices=[200, 220, 220, 220, 210, 210, 200, 230, 230, 220, 220, 220, 220, 220, 240]
deluxeKingBedPrices=[250, 285, 285, 285, 270, 270, 260, 299, 299, 285, 285, 285, 285, 285, 320]
hyattPresidentialRoomPrices=[2200, 2220, 2220, 2220, 2200, 2200, 2200, 2220, 2220, 2200, 2200, 2200, 2200, 2200, 2240]

price=[]

for i in Date:
	if i==31:
		p={
			i:{
				"standardRoomPrices":standardRoomPrices[0],
				"executiveRoomPrices":executiveRoomPrices[0],
				"presidentialRoomPrices":presidentialRoomPrices[0],
				"kingBedPrices":kingBedPrices[0],
				"deluxeKingBedPrices":deluxeKingBedPrices[0],
				"hyattPresidentialRoomPrices":hyattPresidentialRoomPrices[0]
			}
		}
	else:	
		p={
			i:{
				"standardRoomPrices":standardRoomPrices[Date.index(i)],
				"executiveRoomPrices":executiveRoomPrices[Date.index(i)],
				"presidentialRoomPrices":presidentialRoomPrices[Date.index(i)],
				"kingBedPrices":kingBedPrices[Date.index(i)],
				"deluxeKingBedPrices":deluxeKingBedPrices[Date.index(i)],
				"hyattPresidentialRoomPrices":hyattPresidentialRoomPrices[Date.index(i)]
			}
		}
		
	price.append(p)
	
pprint(price)

"""
will produce
price=[{31: {'deluxeKingBedPrices': 250,
       'executiveRoomPrices': 250.47,
       'hyattPresidentialRoomPrices': 2200,
       'kingBedPrices': 200,
       'presidentialRoomPrices': 523.71,
       'standardRoomPrices': 182.16}},
 {1: {'deluxeKingBedPrices': 285,
      'executiveRoomPrices': 278,
      'hyattPresidentialRoomPrices': 2220,
      'kingBedPrices': 220,
      'presidentialRoomPrices': 578,
      'standardRoomPrices': 202}},
 {2: {'deluxeKingBedPrices': 285,
      'executiveRoomPrices': 278,
      'hyattPresidentialRoomPrices': 2220,
      'kingBedPrices': 220,
      'presidentialRoomPrices': 578,
      'standardRoomPrices': 202}},
 {3: {'deluxeKingBedPrices': 285,
      'executiveRoomPrices': 278,
      'hyattPresidentialRoomPrices': 2220,
      'kingBedPrices': 220,
      'presidentialRoomPrices': 578,
      'standardRoomPrices': 202}},
 {4: {'deluxeKingBedPrices': 270,
      'executiveRoomPrices': 239.1,
      'hyattPresidentialRoomPrices': 2200,
      'kingBedPrices': 210,
      'presidentialRoomPrices': 512,
      'standardRoomPrices': 170.74}},
 {5: {'deluxeKingBedPrices': 270,
      'executiveRoomPrices': 239.1,
      'hyattPresidentialRoomPrices': 2200,
      'kingBedPrices': 210,
      'presidentialRoomPrices': 512,
      'standardRoomPrices': 170.74}},
 {6: {'deluxeKingBedPrices': 260,
      'executiveRoomPrices': 239.1,
      'hyattPresidentialRoomPrices': 2200,
      'kingBedPrices': 200,
      'presidentialRoomPrices': 512,
      'standardRoomPrices': 170.74}},
 {7: {'deluxeKingBedPrices': 299,
      'executiveRoomPrices': 303.6,
      'hyattPresidentialRoomPrices': 2220,
      'kingBedPrices': 230,
      'presidentialRoomPrices': 607,
      'standardRoomPrices': 227}},
 {8: {'deluxeKingBedPrices': 299,
      'executiveRoomPrices': 303.6,
      'hyattPresidentialRoomPrices': 2220,
      'kingBedPrices': 230,
      'presidentialRoomPrices': 607,
      'standardRoomPrices': 227}},
 {9: {'deluxeKingBedPrices': 285,
      'executiveRoomPrices': 265,
      'hyattPresidentialRoomPrices': 2200,
      'kingBedPrices': 220,
      'presidentialRoomPrices': 570,
      'standardRoomPrices': 189.75}},
 {10: {'deluxeKingBedPrices': 285,
       'executiveRoomPrices': 265,
       'hyattPresidentialRoomPrices': 2200,
       'kingBedPrices': 220,
       'presidentialRoomPrices': 570,
       'standardRoomPrices': 189.75}},
 {11: {'deluxeKingBedPrices': 285,
       'executiveRoomPrices': 265,
       'hyattPresidentialRoomPrices': 2200,
       'kingBedPrices': 220,
       'presidentialRoomPrices': 570,
       'standardRoomPrices': 189.75}},
 {12: {'deluxeKingBedPrices': 285,
       'executiveRoomPrices': 240,
       'hyattPresidentialRoomPrices': 2200,
       'kingBedPrices': 220,
       'presidentialRoomPrices': 512,
       'standardRoomPrices': 170.79}},
 {13: {'deluxeKingBedPrices': 285,
       'executiveRoomPrices': 264,
       'hyattPresidentialRoomPrices': 2200,
       'kingBedPrices': 220,
       'presidentialRoomPrices': 550,
       'standardRoomPrices': 189}},
 {14: {'deluxeKingBedPrices': 320,
       'executiveRoomPrices': 290,
       'hyattPresidentialRoomPrices': 2240,
       'kingBedPrices': 240,
       'presidentialRoomPrices': 595,
       'standardRoomPrices': 210}}]

pprint(price)

"""
