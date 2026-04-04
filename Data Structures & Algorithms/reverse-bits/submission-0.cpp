class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res;
        for (int i = 0; i < 32; i++) {
            uint32_t temp = (n >> i) & 1;
            res += (temp << (31 - i));

            
            // 101000
            // 000101
        }
        return res;
    }
};
