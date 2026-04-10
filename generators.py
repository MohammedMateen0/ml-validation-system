import sys
import random
from typing import Generator,Iterator
square_list=[i**2 for i in range(1000000)]
square_gen=(i**2 for i in range(1000000))
print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))

def batch_csv_reader(
        data:list[dict],batch_size:int=1000
)->Generator[list[dict],None,None]:
    batch:list[dict]=[]
    for row in data:
        batch.append(row)
        if len(batch)>=batch_size:
            yield batch
            batch=[]
    if batch:
        yield batch

def infinite_sampler(
        data:list,batch_size:int
)->Generator[list,None,None]:

    indices=list(range(len(data)))
    while True:
        random.shuffle(indices)
        for i in range(0,len(indices),batch_size):
            yield [data[j] for j in indices[i:i + batch_size]]

def read_all_files(*paths:str)->Generator[str,None,None]:
    for path in paths:
        yield from _read_file(path)
def _read_file(path:str)->Generator[str,None,None]:
    for i in range(3):
        yield f"{path}: line {i}"

class SlidingWindow:
    def __init__(self,data:list,window:int):
        self.data=data
        self.window=window
        self._idx=0
    def __iter__(self)->Iterator:
        self._idx=0
        return self
    def __next__(self)->list:
        end=self._idx +self.window
        if end>len(self.data):
            raise StopIteration
        result = self.data[self._idx:end]
        self._idx+=1
        return result

def make_batches(
        X:list,y:list,batch_size:int=32
)->Generator[tuple[list,list],None,None]:
    for i in range(0,len(X),batch_size):
        yield X[i:i+batch_size],y[i:i+batch_size]