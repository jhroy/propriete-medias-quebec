import json, csv

d = json.load(open("data.json"))

a = b = 0

for neu in d["nodes"]:
	a += 1
	try:
		if neu["lat"]:
			x = 0
			b += 1
			print(a,b)
			# print(neu)

			f = open("RQA.csv")
			adresses = csv.reader(f)
			next(adresses)

			for adr in adresses:
				if neu["adr4"] == adr[9] and (adr[5] in neu["adr1"] and adr[17] in neu["adr1"]):
					x += 1
					# print(neu)
					# print(adr)
					neu["géocodé"] = "OUI"
					neu["lat"] = float(adr[-1])
					neu["lon"] = float(adr[-2])
					print(neu)

					# print(".....")
					# with open("test.json","w") as flute:
					# 	json.dump(d,flute)
				# 	break
				# break
			# break
			if x == 0:
				neu["géocodé"] = "NON"
	except:
		pass

	with open("donnees.json","w") as flute:
		json.dump(d,flute)