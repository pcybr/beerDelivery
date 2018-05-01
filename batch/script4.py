from kafka import KafkaConsumer
import json

while True:
	try:
		consumer = KafkaConsumer('recommendation_topic', group_id='listing-index', bootstrap_servers=['kafka:9092'])
		# consumer2 = KafkaConsumer('order_topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])

		for index in consumer:
			listing = json.loads((index.value).decode('utf-8'))
			print("Trip Listing",listing)
			file = open("logging.txt","w")
			file.write(listing['user_id'] + "\t" + listing['item_id'] + "\n")
			file.close()

		continue

	except:
		print("Error")

