class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        return ":;".join(strs)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        return str.split()


newSol = Solution();
print(newSol.encode(strs=["boy", "girl","dad","mum"]))
print(newSol.decode(str="I am a good boy right"))
