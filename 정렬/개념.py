from functools import cmp_to_key

students =[('kim', 'B+', 18), ('lee', 'A+', 21), ('jeong', 'A', 18), ('aa', 'B+', 18)]

def new_sort(n1, n2):
  if n1[2] > n2[2]: return 1
  elif n1[2] == n2[2]: return 0
  else: return -1

# cmp_to_key
print(sorted(students, key=cmp_to_key(new_sort)))

# 람다
print(sorted(students, key=lambda x : x[1] + str(x[2]), reverse=True))

####################################
# 2번째 원소 기준으로 오름차순 정렬
sample = [[0, 4], [0, 2], [1, 3], [2, 1], [0, 10], [-1, 11], [10, -1]]
def second(x): return x[1]
print(sorted(sample, key=second)) # 함수
print(sorted(sample, key=lambda x : x[1])) # 람다