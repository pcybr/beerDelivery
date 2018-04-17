from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json

while True:
	try:
		consumer = KafkaConsumer('trip_topic', group_id='listing-index', bootstrap_servers=['kafka:9092'])
		# consumer2 = KafkaConsumer('order_topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
		es = Elasticsearch(['es'])

		for index in consumer:
			listing = json.loads((index.value).decode('utf-8'))
			print("Trip Listing",listing)
			es.index(index='listing_index_trip', doc_type='listing', id=listing['trip_id'], body=listing)
			es.indices.refresh(index="listing_index_trip")

		# for index in consumer2:
		# 	print('loop 2')
		# 	listing = json.loads((index.value).decode('utf-8'))
		# 	print("Order Listing",listing)
		# 	es.index(index='listing_index', doc_type='listing', id=listing['order_id'], body=listing[0])
		# 	es.indices.refresh(index="listing_index")

		continue

	except:
		print("Error")

