class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0;
        int r = matrix.size() - 1;

        while (l <= r) {
            int temp = (l + r) / 2;
            if (matrix[temp][0] <= target) {
                if (temp == matrix.size() - 1 || matrix[temp + 1][0] > target) {
                    // do second binary search
                    return innerMatrixSearch(matrix[temp], target);
                }
                else {
                    // continue this binary search
                    l = temp + 1;
                }
            }
            else {
                r = temp - 1;
            }
        }
        return false;
    }

    bool innerMatrixSearch(vector<int> &matrixRow, int target) {
        int l = 0;
        int r = matrixRow.size() - 1;

        while (l <= r) {
            int temp = (l + r) / 2;
            if (matrixRow[temp] == target) {
                return true;
            }
            else if (matrixRow[temp] < target) {
                l = temp + 1;
            }
            else {
                r = temp - 1;
            }
        }
        return false;
    }
};
