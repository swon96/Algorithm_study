from collections import deque

def person_is_right(name):
    if name[-1] == 'h':
        return True
    else:
        return False


def search_frined(name):
    searching_queue = deque()
    searching_queue += graph[name]
    searched = []

    while len(searching_queue) != 0:
        person = searching_queue.popleft()
        if not person in searched:
            if person_is_right(person):
                print("Found Right Person " + person)
                return True
            else:
                searched.append(person)
                searching_queue += graph[person]
    return False


graph = {}
graph["Me"] = ["JW Kim", "YS Lee", "SM Choi", "SE Chae"]
graph["YS Lee"] = ["JH Oh"]
graph["JH Oh"] = ["SE Oh"]
graph["JW Kim"] = []
graph["SM Choi"] = []
graph["SE Chae"] = ["CS Choi", "HY Soon"]
graph["CS Choi"] = []
graph["HY Soon"] = []
graph["SE Oh"] = []

search_frined("Me")