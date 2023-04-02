sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]

# print("맨 처음: ", sample)

def bubbleSort(data):
  for i in range(len(data) - 1):
    # print('========================================================= i : ', i)
    for j in range(i):
      # print('--------------------------------------------- j : ', j)
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
        # print("바뀐 배열", sample)

bubbleSort(sample)
print(sample)