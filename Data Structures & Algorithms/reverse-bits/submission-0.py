class Solution:
    def reverseBits(self, n: int) -> int:
        n_s = list(bin(n)[2:].zfill(32))

        for i in range(len(n_s)//2):
            n_s[i], n_s[-1-i] = n_s[-1-i], n_s[i]

        return int(''.join(n_s), 2)