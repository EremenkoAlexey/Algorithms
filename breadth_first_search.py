# -*- coding: utf-8 -*-
"""
Алгоритм поиска в ширину (англ. breadth-first search, BFS) позволяет найти кратчайшие пути из одной вершины 
невзвешенного (ориентированного или неориентированного) графа до всех остальных вершин. 
Под кратчайшим путем подразумевается путь, содержащий наименьшее число ребер.
"""
initGraph = {
    "A": ['B', 'C'],
    "B": ['D', 'E'],
    "C": ['F', 'G'],
    "D": [],
    "E": ['H'],
    "F": [],
    "G": [],
    "H": []}
      #      A
      #    /   \
      #   B     C
      #  /  \   / \
      # D    E F   G
      #       \
      #        H
ROOT = 'A'
KEY = 'H'
visited = {ROOT:""}

def breadth_first_search(graph, root, key)->bool:
    """Looks for KEY in graph. Returns True if KEY found"""
    if graph == {}:
        return False
    queue = [root]
    def check_cell(value: str)-> str:
        if value == key:
            return True
        for cell in graph[value]:
            queue.append(cell)
            visited[cell] = value
        return False
    while True:
        if len(queue) > 0:
            if check_cell(queue.pop(0)):
                return True
        else:
            return False

def push(value: str)->str:
    """Prints the way to the KEY"""
    cur_value = visited[value]
    if cur_value != "":
        return push(cur_value)+"->"+value
    return value

if breadth_first_search(initGraph, ROOT, KEY):
    print("Route to", KEY, "is", push(KEY))
else:
    print("Key "+ KEY+ " doesn't exist!")
    
