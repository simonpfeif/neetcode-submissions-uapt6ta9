class Solution {
    /**
     * @param {number[][]} isConnected
     * @return {number}
     */
    findCircleNum(isConnected) {
        let res = 0
        const n = isConnected.length
        const visited = new Array(n).fill(false)

        function dfs(node) {
            visited[node] = true
            for (let nei = 0; nei < n; nei++) {
                if (!visited[nei] && isConnected[node][nei] === 1) {
                    dfs(nei)
                }
            }
        }


        for (let i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i)
                res++;
            }
        }
        return res
    }
}
