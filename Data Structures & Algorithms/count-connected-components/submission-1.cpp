class DSU {
public: 
    vector<int> par, sz;
    DSU(int n){
        for(int i = 0; i < n; i++){
            par.push_back(i);
        }
        for(int i = 0 ; i < n; i ++){
            sz.push_back(0);
        }
    }

    int findPar(int x){
        if(par[x] == x) return x;
        return findPar(par[x]);
    }

    void unite(int a, int b){
        a = findPar(a);
        b = findPar(b);
        if(sz[a] < sz[b]){
            swap(a, b);
        }
        par[b] = a;
        sz[a] += sz[b];
    }

};


class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        // O(n + edges * log(n))
        vector<vector<int>> adj(n);
        vector<bool> visited(n, false);
        
        for(auto& edge: edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        auto dfs = [&](auto&& self, int i) -> void{
            visited[i] = true;

            for(int j = 0; j < adj[i].size(); j++){
                if(!visited[adj[i][j]]){
                    self(self, adj[i][j]);
                }
            }
        };

        int count = 0;
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                count ++;
                dfs(dfs, i);
            }
        }
        return count;
        
    }
};
