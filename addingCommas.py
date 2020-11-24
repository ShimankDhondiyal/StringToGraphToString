import networkx as nx

def make_graph(text):
    #create new blank graph and array to keep track of duplicates
    graph = nx.MultiDiGraph()
    firstNode = ("", 0, 0)
    iteration = 1
    for currentWord in text.split():
        #first, make note of whether the current word has a comma or period
        hasP = 0
        hasC = 0
        if currentWord.endswith(","):
            hasC = 1
        elif currentWord.endswith("."):
            hasP = -1
        #shorten the word so that comma/period is not added to graph
        if hasC == 1 or hasP == -1:
            currentWord = currentWord[0:len(currentWord) - 1]
        
        #if this is the first iteration, re-define firstNode (special case)
        if iteration == 1:
            firstNode = (currentWord, hasC, hasP)
            graph.add_node(currentWord)
            iteration += 1
            continue
        #if this is not first iteration (normal case)
        else:
            secondNode = (currentWord, hasC, hasP)
            #only add a node if it does not exist
            if currentWord not in graph:
                graph.add_node(currentWord)
            #now we hve to create an adge between firstNode and secondNode
            #if the first node has a comma
            if firstNode[1] == 1:
                graph.add_edge(firstNode[0], currentWord, weight = 1)
            #elif the first node has a period
            elif firstNode[2] == -1:
                graph.add_edge(firstNode[0], currentWord, weight = -1)
            #else the first node has neither period nor comma
            else:
                graph.add_edge(firstNode[0], currentWord, weight = 0)
            firstNode = secondNode
    
  
            
    return graph

def move_graph(currentNode, a):
    #1. check all incoming edges of the currentNode
    for edge in list(a.in_edges(currentNode, data = 'weight')):
        #if any edge has value 1...
        if edge[2] == 1:
            #...restart and set all edge weights to 1
            for edge2 in list(a.in_edges(currentNode, data = 'weight')):
                #only change the weight to 1 if the current is 0. do not change if already a 1 or if -1
                if edge2[2] == 0:
                    #instead of changing the weight, delete this edge and make a new one
                    a.remove_edge(edge2[0], edge2[1])
                    a.add_edge(edge2[0], edge2[1], weight = 1)
                    continue
            break
        
    #2. check all outgoing edges
    for edge in list(a.out_edges(currentNode, data = 'weight')):
        #if any edge has value 1...
        if edge[2] == 1:
        #if a.get_edge_data(currentNode, edge[1]) == 1:
            #...restart and set all edge weights to 1
            for edge2 in list(a.out_edges(currentNode, data = 'weight')):
                #only change the weight to 1 if the current is 0. do not change if already a 1 or if -1
                if edge2[2] == 0:
                    #instead of changing the weight, delete this edge and make a new one
                    a.remove_edge(edge2[0], edge2[1])
                    a.add_edge(edge2[0], edge2[1], weight = 1)
            break
        
    #3. return the new graph
    return a


def convert(text, a):
    returnText = ""
    previousNode = a.nodes()
    iteration = 1
    for word in text.split():
        #add current word to return
        #iterate for loop
        #find edge between perviousNode and word. if edge has 1, print comma
        #set previousWord to word, iterate for loop
        hasC = False
        hasP = False
        if word.endswith(","):
            hasC = True
            word = word[0:len(word) - 1]
        if word.endswith("."):
            hasP = True
            word = word[0:len(word) - 1]

        if iteration == 1:
            returnText += word
            previousNode = a.nodes(data = word)
            iteration += 1
        else:
            currentNode = a.nodes(data = word)
            #loop through all edges from previousNode to currentNode, if edge found print comma/space/period based on weight
            for edge in a.out_edges(previousNode._data, data = 'weight'):
                if edge[1] == currentNode._data:
                    #now, we have found the edge between rhe last word and the current word
                    break
            #now add comma/period/space depending on weight
            if edge[2] == 0:    #space
                returnText += " " + word
            elif edge[2] == -1: #period
                returnText += ". " + word
            else:               #comma
                returnText += ", " + word
            previousNode = currentNode
    #add a period at the end of the returnText if there was a period at the end of a sentence originally
    if hasP == True:
        returnText += "."
    return returnText

def add_commas(text):
    """Returns the textobtained by adding commas in appropriate places as per rules above"""
    #make a graph of text and tranverse graph and add commas then convert graph into string
    #return string
    
    #1. make graph given the text
    a = make_graph(text)
    #2. go through each node in the graph and adjust the edge weights. overwrite current graph with new data
    for currentNode in a:
        a = move_graph(currentNode, a)
    #3. convert graph to text -- creating text2 from text1 of graph
    text2 = convert(text, a)

    return text2

def main():
    # Process the input file by transforming each line of text using add_commas
    # You should print the input followed by the output (per line), with a blank line separating them.
    while True:
        text = str(input("Enter a sentence with commas: "))
        if text.endswith(".") == True:
            break
        print("enter a period at the end")
    text2 = add_commas(text)
    print(text2)
main()
