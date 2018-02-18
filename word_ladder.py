from graph_classDef import Graph


def build_word_graph(wordList):

	buckets = {}
	g = Graph()

	for word in wordList:
		# all four lettered words
		for i in range(3):
			bucket = word[:i]+'_'+word[i+1:]
			if bucket in buckets:
				buckets[bucket].append(word)
			else:
				buckets[bucket] = [word]


	for bucket in buckets:
		for word1 in buckets[bucket]:
			for word2 in buckets[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2, 1) 




def word_ladder(g, start, end):

	if start not in g or end not in g:
		TypeError('word not found!')

	start_vert = g.getVertex(start)
	explore_queue = []
	explore_queue.insert(0, start_vert)
	start_vert.status = 'exploring...'
	start_vert.distance = 0

	while len(explore_queue) > 0:
		curr_vert = explore_queue.pop()

		for nbr in curr_vert.getNeighbors():
			if nbr.status == 'initial':
				nbr.distance = curr_vert.distance + 1
				nbr.pred = curr_vert
				if nbr.key = end:
					break
				nbr.status = 'exploring...'
				explore_queue.insert(0, nbr)

			curr_vert.status = 'explored'

	# now: nbr is the 'end' word
	# print the word ladder
	while (nbr):
		print(nbr.key)
		nbr = nbr.pred











