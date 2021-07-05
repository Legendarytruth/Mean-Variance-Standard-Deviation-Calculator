import numpy as np

def calculate(list):
  if(len(list) < 9):
    raise ValueError("List must contain nine numbers.") 
  else:
    lis = np.array([list[0:3], list[3:6], list[6:9]])

    calculations = {
      'mean': [lis.mean(axis = 0).tolist(), lis.mean(axis = 1).tolist(), lis.mean().tolist()],
      'variance': [lis.var(axis = 0).tolist(), lis.var(axis = 1).tolist(), lis.var().tolist()],
      'standard deviation': [lis.std(axis = 0).tolist(), lis.std(axis = 1).tolist(), lis.std()],
      'max': [lis.max(axis = 0).tolist(), lis.max(axis = 1).tolist(), lis.max().tolist()],
      'min': [lis.min(axis = 0).tolist(), lis.min(axis = 1).tolist(), lis.min().tolist()],
      'sum': [lis.sum(axis = 0).tolist(), lis.sum(axis = 1).tolist(), lis.sum().tolist()]}
    print(calculations)
    return calculations



{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
  'variance': [[6.0, 6.0, 6.0], [6.0, 6.0, 6.0], 6.666666666666667], 
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611], 
  'max': [[6, 7, 8], [2, 5, 8], 8], 
  'min': [[0, 1, 2], [0, 3, 6], 0], 
  'sum': [[9, 12, 15], [3, 12, 21], 36]}
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}