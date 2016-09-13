import time

def matrix_mul(A, B):
  return ([A[0][0] * B[0][0] + A[0][1] * B[1][0],
           A[0][0] * B[0][1] + A[0][1] * B[1][1]],
          [A[1][0] * B[0][0] + A[1][1] * B[1][0],
           A[1][0] * B[0][1] + A[1][1] * B[1][1]])

def matrix_exp(A, e):
  if not e:
    return [[1,0],[0,1]]
  elif e % 2:
    return matrix_mul(A, matrix_exp(A, e-1))
  else:
    sq= matrix_exp(A, e//2)
    return matrix_mul(sq, sq)


def fibo(n, que):
  M = [[1,1],[1,0]]
  start_time = time.time()
  val = matrix_exp(M, n)[0][0]
  end_time = str((time.time() - start_time)*100)
  que.put([val,end_time])

