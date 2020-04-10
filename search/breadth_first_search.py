from collections import deque

def found(item, end_item):
    return item == end_item

def search(graph, start_item, end_item):
    search_queue = deque()
    search_queue += graph[start_item]
    searched_items = []
    while search_queue:
        cur_item = search_queue.popleft()
        if not cur_item in searched_items:
            if found(cur_item, end_item):
                return True
            else:
                search_queue += graph[cur_item]
                searched_items.append(cur_item)
    
    return False

graph = {}
graph['A'] = ['B', 'E']
graph['B'] = ['C']
graph['E'] = ['D']
graph['C'] = ['D']
graph['D'] = []

print(search(graph, 'E', 'B'))