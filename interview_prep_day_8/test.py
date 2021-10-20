arr = [2, 1]
def findSignatureCounts(arr):
  n = len(arr)
  res = [0] * n
  completed = set()
  for place, stu in enumerate(arr, start = 1):
    if place == stu:
      res [place - 1] = 1 
      completed.add(stu)
      continue
    next_stu = place - 1 if place - 1 >= 1 else n
    while next_stu != stu and len(completed) < n:
      if next_stu not in completed:
        res [place - 1] += 1
      next_stu = next_stu - 1 if next_stu - 1 >= 1 else n
      
  return res
print(findSignatureCounts(arr))