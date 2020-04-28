class Myheap():

	def __init__(self):
		self.heap = []


	def heappush(self, item):
		self.heap.append(item)
		self._siftdown(0, len(self.heap)-1)

	def heappop():
		lastelt = self.heap.pop()
	    if self.heap:
	        returnitem = self.heap[0]
	        self.heap[0] = lastelt
	        self._siftup(0)
	        return returnitem
	    return lastelt

	def _siftdown(self, start, pos):
	    newitem = self.heap[pos]
	    while pos > start:
	        parentpos = (pos - 1) >> 1
	        parent = self.heap[parentpos]
	        if newitem < parent:
	            self.heap[pos] = parent
	            pos = parentpos
	            continue
	        break
	    self.heap[pos] = newitem

	def _siftup(pos):
	    endpos = len(self.heap)
	    startpos = pos
	    newitem = self.heap[pos]
	    childpos = 2*pos + 1
	    while childpos < endpos:
	        rightpos = childpos + 1
	        if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
	            childpos = rightpos
	        self.heap[pos] = self.heap[childpos]
	        pos = childpos
	        childpos = 2*pos + 1
	    self.heap[pos] = newitem
	    _siftdown(self.heap, startpos, pos)