import math
def isPrime():
  try:
    print("Enter positive integer")
    a = int(input())
    if a > 0:
        def check_Prime(num):
            if a==1:
              return False
            elif a == 2:
                return True
            else:
                for i in range(2,math.ceil(a/2)+1):
                    if(a % i) == 0:
                        return False
                return True
        print(check_Prime(a))
    else:
        print("Only accepts positive integer")
  except Exception:
    print("Only accepts positive integer")


def reverse():
  print("Enter list elements separated by ','")
  s = input()
  l = s.split(",")
  x = reversed(l)
  return list(x)

def k_rotate():
  print("Enter value of k")
  k = int(input())
  print("Enter list elements separated by ','")
  arr = (input()).split(",")
  for i in range(k):
    temp = arr[0]
    for j in range(len(arr)):
      arr[j] = arr[(j+1)%len(arr)]
    arr[-1] = temp
    print(arr)

def merge_sortedlist():
  print("Enter list 1 elements separated by ','")
  arr1 = [int(i) for i in (input()).split(",")]
  print("Enter list 2 elements separated by ','")
  arr2 = [int(i) for i in (input()).split(",")]
  if (sorted(arr1) != arr1 or sorted(arr2) != arr2):
    return "Given list is not sorted, please enter only sorted list"
  else:
    arr3 = []
    i = j =0
    while(i < len(arr1) and j < len(arr2)):
      if arr1[i] <= arr2[j]:
        arr3.append(arr1[i])
        i+= 1
      else:
        arr3.append(arr2[j])
        j+= 1
    if i >= len(arr1):
      for k in range(j,len(arr2)):
        arr3.append(arr2[k])
    if j >= len(arr2):
      for k in range(i,len(arr1)):
        arr3.append(arr1[k])
    return arr3

def digit_list():
  print("Enter number")
  n = input()
  arr = list(n)
  return arr

def remove_k_largest():
  print("Enter list separated by ','")
  arr1 = [int(i) for i in (input()).split(",")]
  print("Enter value of k")
  k = int(input())
  if k < len(arr1) and k > 0:
    hash_map = {}
    # print(max(arr1))
    for i in range(max(arr1)+1):
      hash_map[i] = 0
    for i in arr1:
      hash_map[i] += 1
    n = max(arr1)
    final = -1
    while(k>0 and n>0):
      if hash_map[n] > 0 and k == 1:
        final = n
        break
      elif hash_map[n] > 0 and k != 1:
        k-= 1
        n-= 1
      else:
        n-=1
    for j in arr1:
      if j == final:
        arr1.remove(j)
    return arr1
  else:
    return "K value should be less then size of list and greater then 0"

def sort_list_bylength():
  print("Enter how many list u want")
  n = int(input())
  arr = []
  for i in range(n):
    print("Enter ",i+1," list separated by ','")
    temp = [i for i in (input()).split(",")]
    arr.append(temp)
  hash_map = {}
  for i in arr:
    hash_map[str(i)] = len(i)
  sorted_hash_map = sorted(hash_map.items(), key = 
             lambda kv:(kv[1], kv[0]))
  final = []
  for k,v in sorted_hash_map:
    for ele in arr:
      if eval(k) == ele:
        final.append(eval(k))
  return final

def sort_list_bylength_frequency():
  print("Enter how many list u want")
  n = int(input())
  arr = []
  for i in range(n):
    print("Enter ",i+1," list separated by ','")
    temp = [i for i in (input()).split(",")]
    arr.append(temp)
  hash_map = {}
  for i in arr:
    hash_map[str(i)] = len(i)
  sorted_hash_map = sorted(hash_map.items(), key = 
             lambda kv:(kv[1], kv[0]))
  temp = {}
  temp1 = []
  for k,v in sorted_hash_map:
    temp1.append(v)
  p = max(temp1)
  for i in range(1,p+1):
    temp[i] = 0
  for k,v in sorted_hash_map:
    temp[v] += 1
  sorted_frequency = sorted(temp.items(), key = 
             lambda kv:(kv[1], kv[0]))
  final = []
  for k,v in sorted_frequency:
    for k1,v1 in sorted_hash_map:
      if v1 == v:
        final.append(eval(k1))
  return final
    
def graph():
  print("Enter number of nodes")
  n = int(input())
  matrix = []
  print("Enter values of nodes")
  node_values = [i for i in (input()).split(",")]
  print("Enter adjacency matrix rows by rows separated by ,")
  for i in range(n):
    matrix.append([int(i) for i in (input()).split(",")])

  graph_structure = {}
  for i in node_values:
    graph_structure[i] = []
  for i in range(n):
    for j in range(n):
      if matrix[i][j] != -1:
        graph_structure[node_values[i]].append((node_values[j],matrix[i][j]))
  print("Your graph structure is ")
  print(graph_structure)
  print("-------------------------------------------")
  print("Press 1 for insertion of node,2 for deletion of node, 3 for insertion of edge, 4 for deletion of edge")
  num = int(input())
  if(num == 1):
    print("Enter node value")
    new_node = input()
    if(new_node in node_values):
      print("Node is already present in graph")
    else:
      node_values.append(new_node)
      graph_structure[new_node] = []
      print("Enter adjacency list for this new node")
      matrix.append([int(i) for i in (input()).split(",")])
      for i in range(n):
        matrix[i].append(matrix[-1][i]) 
      n = n + 1
      # print("Matrix is :",matrix)
      for i in range(n):
        if matrix[-1][i] != -1:
          graph_structure[node_values[n-1]].append((node_values[i],matrix[-1][i]))
          graph_structure[node_values[i]].append((node_values[n-1],matrix[-1][i]))
    print("Updated graph is:")
    print(graph_structure)
  elif(num == 2):
    print("Enter node_value u want to delete")
    del_node = input()
    if not del_node in node_values:
      print("Entered node is missing")
    else:
      index = -1
      for i in range(len(node_values)):
        if node_values[i] == del_node:
          index = i
      print("Index to be deleted is ",index)
      graph_structure.pop(del_node)
      node_values.remove(del_node)
      for i in node_values:
        x = graph_structure[i]
        for ele in x:
          x,y = ele
          if x == del_node:
            graph_structure[i].remove(ele)
      print(graph_structure)
  elif(num == 3):
    print("Enter source_value destination_value edge_value")
    new_edge = [i for i in input().split(" ")]
    for i in range(len(node_values)):
      if node_values[i] == new_edge[0]:
        src_index = i
      if node_values[i] == new_edge[1]:
        dest_index = i
    graph_structure[node_values[src_index]].append((node_values[dest_index],int(new_edge[2])))
    graph_structure[node_values[dest_index]].append((node_values[src_index],int(new_edge[2])))
    print(graph_structure)
  elif(num == 4):
    print("Enter source destination i.e edge to be deleted")
    del_edge = [i for i in input().split(" ")]
    for i in range(len(node_values)):
      if node_values[i] == del_edge[0]:
        src_index = i
      if node_values[i] == del_edge[1]:
        dest_index = i
    # graph_structure[node_values[src_index]].remove
    x = graph_structure[del_edge[0]]
    for ele in x:
      p,q = ele
      if p == del_edge[1]:
        graph_structure[del_edge[0]].remove(ele)
    x = graph_structure[del_edge[1]]
    for ele in x:
      p,q = ele
      if p == del_edge[0]:
        graph_structure[del_edge[1]].remove(ele)
    print(graph_structure)
  else:
    return graph_structure


def matrix_mul():
  print("Enter order of 1st matrix")
  matrix_order1 = [int(i) for i in input().split("*")]
  print("Enter order of 2nd matrix")
  matrix_order2 = [int(i) for i in input().split("*")]
  print(matrix_order1,matrix_order2)
  if(matrix_order1[1] != matrix_order2[0]):
    print("Matrix can't be multiplied")
  else:
    print("Enter matrix 1")
    matrix1 = []
    for i in range(matrix_order1[0]):
      matrix1.append([int(i) for i in input().split(" ")])
    print("Enter matrix 2")
    matrix2 = []
    for i in range(matrix_order2[0]):
      matrix2.append([int(i) for i in input().split(" ")])
    final_matrix = []
    for i in range(matrix_order1[0]):
      temp1 = []
      for k in range(matrix_order2[1]):
        temp = 0
        for j in range(matrix_order1[1]):
          temp += matrix1[i][j]*matrix2[j][k]
        temp1.append(temp)
      final_matrix.append(temp1)
    return(final_matrix)

