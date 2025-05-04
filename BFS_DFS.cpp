#include<iostream>
#include<queue>
#include<vector>

using namespace std;

class Graph {
    int v;
    vector<vector<int>> adj;

public:
    Graph(int v);
    void addEdge(int u, int v);
    void BFS(int start);
    void DFS(int start);
    void DFSUtil(int node, vector<bool>& visited);
    void printAdjList();  // NEW function
};

Graph::Graph(int v) {
    this->v = v;
    adj.resize(v);
}

void Graph::addEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u); // Undirected graph
}

void Graph::printAdjList() {
    cout << "\nAdjacency List:\n";
    for (int i = 0; i < v; ++i) {
        cout << i << ": ";
        for (int neighbor : adj[i]) {
            cout << neighbor << " ";
        }
        cout << endl;
    }
}

void Graph::BFS(int start) {
    vector<bool> visited(v, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    cout << "\nBFS traversal starting from node " << start << ":\n";

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int neighbour : adj[node]) {
            if (!visited[neighbour]) {
                visited[neighbour] = true;
                q.push(neighbour);
            }
        }
    }
    cout << endl;
}

void Graph::DFS(int start) {
    vector<bool> visited(v, false);
    cout << "\nDFS traversal starting from node " << start << ":\n";
    DFSUtil(start, visited);
    cout << endl;
}

void Graph::DFSUtil(int node, vector<bool>& visited) {
    visited[node] = true;
    cout << node << " ";

    for (int neighbour : adj[node]) {
        if (!visited[neighbour]) {
            DFSUtil(neighbour, visited);
        }
    }
}

int main() {
    int vertices, edges;
    cout << "Enter number of vertices: ";
    cin >> vertices;

    Graph g(vertices);

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Enter " << edges << " edges (u v):\n";
    for (int i = 0; i < edges; ++i) {
        int u, v;
        cin >> u >> v;
        g.addEdge(u, v);
    }

    int startNode;
    cout << "Enter the starting node for traversal: ";
    cin >> startNode;

    g.printAdjList();      // Show adjacency list
    g.BFS(startNode);      // Perform BFS
    g.DFS(startNode);      // Perform DFS

    return 0;
}
