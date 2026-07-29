class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        final = []

        for i in range(m):
            final.append(nums1[i])
            print(final)

        for i in range(n):
            final.append(nums2[i])
            print(final)

        final.sort()
        print(final)
        for i in range (len(final)):
            nums1[i] = final[i]