class Solution {
public:
    std::vector<std::vector<int>> matrix;

    void setSize(int rows, int cols) {
        matrix.resize(rows);
        for (auto& row : matrix) {
            row.resize(cols);
        }
    }

    int solve(int i, int j, int m, int n){
        if( i == m-1 || j == n-1){
            return 1;
        }
        if(matrix[i][j]!=0){
            return matrix[i][j];
        }
        matrix[i][j] = solve(i,j+1,m,n) + solve(i+1, j,m,n);
        return matrix[i][j];
    }
    
    int uniquePaths(int m, int n) {
        setSize(m, n);
        return solve(0,0,m,n);
    }
};