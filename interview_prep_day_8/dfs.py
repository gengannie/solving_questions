from collections import defaultdict, deque
def DFS(flights, origin,result):
    dests = flights[origin]
    while dests:
        nextD = dests.pop() # removes the child from list of destinations
        DFS(flights,nextD, result) # explores the desinations of children
    result.append(origin) # addds origin 
def findItinerary(tickets): # List[List[str]]
    flights = defaultdict(list) # creates a graph using a dictionary
    for ticket in tickets:
        ori, dest = ticket [0], ticket [1] # key is origin, value is destination (list)
        flights[ori].append(dest) # adds this dest corresponding to the key in graph
    for ori, iti in flights.items():
        iti.sort(reverse = True) # sorts it in descending lexicographic order
    result = []
    DFS(flights,"JFK", result)
    return result[::-1] # need to reverse 
if __name__ == "__main__":
    print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
        
