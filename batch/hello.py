from pyspark import SparkContext

sc = SparkContext("spark://spark-master:7077", "PopularItems")

# each worker loads a piece of the data file
data = sc.textFile("/app/logging.txt", 2)

#Remove duplicates
distinct = data.distinct()

#tell each worker to split each line of it's partition
pairs = distinct.map(lambda line: line.split("\t"))

#(user_id, [list of item ids they clicked on])
group1 = pairs.groupByKey()
group2 = group1.mapValues(list)
grouped = group2.map(lambda pair: (pair[0], pair[1])) ###DO WE NEED THIS?

#Transform into (user_id, (item1, item2)
def combinations(trip_list):
	combos = []
	for i in range(len(trip_list)):
		j = i + 1
		while j < len(trip_list):
			first = trip_list[i]
			second = trip_list[j]
			tup = (trip_list[i], trip_list[j])
			combos.append(tup)
			j += 1
	return combos

combine = grouped.map(lambda pair: ((pair[0]), combinations(pair[1])))

seperated = combine.flatMapValues(lambda pair: pair)

reversed_pairs = seperated.map(lambda pair: (pair[1],pair[0]))
rev_grouped = reversed_pairs.groupByKey().mapValues(list)

counts = rev_grouped.map(lambda pair: (pair[0], len(pair[1])))

filtered = counts.filter(lambda pair: pair[1] > 2)

#Collect all output data
output = filtered.collect()

sc.stop()