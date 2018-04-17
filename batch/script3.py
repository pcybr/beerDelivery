from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json

while True:
	try:
		# consumer = KafkaConsumer('trip_topic', group_id='listing-index', bootstrap_servers=['kafka:9092'])
		consumer = KafkaConsumer('person_topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
		es = Elasticsearch(['es'])

		# for index in consumer:
		# 	listing = json.loads((index.value).decode('utf-8'))
		# 	print("Trip Listing",listing)
		# 	es.index(index='listing_index', doc_type='listing', id=listing['trip_id'], body=listing)
		# 	es.indices.refresh(index="listing_index")

		for index in consumer:
			print('loop 3')
			listing = json.loads((index.value).decode('utf-8'))
			print("Person Listing",listing)
			es.index(index='listing_index_person', doc_type='listing', id=listing['person_id'], body=listing)
			es.indices.refresh(index="listing_index_person")

		continue

	except:
		print("Error")

