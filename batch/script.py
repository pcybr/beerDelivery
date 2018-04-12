from elasticsearch import Elasticsearch
from kafka import KafkaProducer

while True:
	try:
		consumer = KafkaConsumer('trip_topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
		consumer2 = KafkaConsumer('order_topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
		es = Elasticsearch(['es'])

		for index in consumer:
			listing = json.loads((index.value).decode('utf-8'))
			print("Trip Listing",listing)
			es.index(index='listing_index', doc_type='listing', id=listing['trip_id'], body=listing[0])
			es.indices.refresh(index="listing_index")

		for index in consumer2:
			listing = json.loads((index.value).decode('utf-8'))
			print("Trip Listing",listing)
			es.index(index='listing_index', doc_type='listing', id=listing['order_id'], body=listing[0])
			es.indices.refresh(index="listing_index")

		continue

	except:
		print("Error")

