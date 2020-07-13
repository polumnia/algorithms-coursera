# from algorithms import utils

def swap(inp_array, ind1, ind2):
    inp_array[ind1], inp_array[ind2] = inp_array[ind2], inp_array[ind1]

class MinPQ:
    def __init__(self):
        self._pq = [None]
        self.size = 0
    
    def _parent_idx(self, idx):
        return idx // 2
    
    def _child_ids(self, idx):
        return (2 * idx, 2 * idx + 1)
    
    def swim(self, value_id):
        while value_id > 1 and self._bigger(self._parent_idx(value_id), value_id):
            swap(self._pq, self._parent_idx(value_id), value_id)
            value_id = self._parent_idx(value_id)
    
    def sink(self, value_id):
        while self._child_ids(value_id)[0] <= self.size:
            childs = self._child_ids(value_id)
            if childs[0] < self.size and self._bigger(*childs):
                smallest_child = childs[1]
            else:
                smallest_child = childs[0]
            if not self._bigger(value_id, smallest_child):
                break

            swap(self._pq, value_id, smallest_child)
            value_id = smallest_child
        
    def insert(self, value):
        self.size += 1
        self._pq.append(value)
        self.swim(self.size)
    
    def _bigger(self, id1, id2):
        return self._pq[id1] > self._pq[id2]
    
    def del_min(self):
        min_key = self._pq[1]
        swap(self._pq, 1, self.size)
        self.size -= 1
        self.sink(1)
        del self._pq[self.size+1]
        return min_key


if __name__ == '__main__':
    mpq = MinPQ()
    for key in "HGNPEIOARTS":
        mpq.insert(key)
    print(mpq._pq)

    mkey = mpq.del_min()
    print(mpq._pq)