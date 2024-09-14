def common_elements(list1, list2):
  commonElements = set()
  for x in list1:
    for i in list2:
      if i == x:
        commonElements.add(x)
  return commonElements

list = (1, 2, 3, 4, 5, 6)
list2 = (1, 6, 7, 8, 9, 4)
common_elements(list, list2)
