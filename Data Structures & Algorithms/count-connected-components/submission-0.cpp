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
        DSU dsu(n);
        for(auto& edge: edges){
            dsu.unite(edge[0], edge[1]);
        }
        int count = 0;
        for(int i = 0; i < n; i++){
            if(dsu.findPar(i) == i) count ++;

        }
        return count;
    }
};
