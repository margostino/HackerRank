class Tree():
    def __init__(self):
        self.nodes = {}
        self.depths = {1:0}
        self.probs = {}

    def __repr__(self):
        return str(self.nodes)

    def __getitem__(self,child):
        return self.nodes[child]

    def insert(self, parent, child, prob):
        self.nodes[child] = parent
        self.depths[child] = self.depths[parent] + 1
        self.probs[child] = prob / 100.0

    def probability(self, nodeA, nodeB):
        if (nodeA == nodeB): return 1
        prob = 1
        while nodeA != nodeB:
            da = self.depths[nodeA]
            db = self.depths[nodeB]
            if (da == db):
                prob *= self.probs[nodeA] * self.probs[nodeB]
                nodeA, nodeB = tree[nodeA], tree[nodeB]
            elif (da < db):
                prob *= self.probs[nodeB]
                nodeA, nodeB = nodeA, tree[nodeB]
            elif (da > db):
                prob *= self.probs[nodeA]
                nodeA, nodeB = tree[nodeA], nodeB
        return prob

tree = Tree()

def init_server():
    print "Reading training set"
    for line in open("training.txt"):
        if "," in line:
            parent, child, prob = map(int, line.strip().split(","))
            tree.insert(parent, child, prob)
    sys.stdout.flush()

def process_client_connection(connection):
    while 1:
        message = read_string_from_socket(connection)
        if message == "END": break
        a, b, threshold = map(float, message.split(","))
        prob = tree.probability(int(a), int(b))
        if prob <= 10 ** threshold: answer = "NO"
        else: answer = "YES"
        write_string_to_socket(connection, answer)
    connection.close()
