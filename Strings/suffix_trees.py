# Given a string, find the longest repeated string
# Input : MISSISSIPPI
# ISSI
# List of suffixes
# I, PI, PPI, IPPI...MISSISSIPPI
# Create a Trie of all suffixes
# I
# PI
# ..
# ..
# ISSIPPI
# ISSISSIPPI
# In the trie, ISSI will be common path, PPI and SSIPPI are two branches
# To find longest repeated string, for every path which has branches, find longest common part.
# In this example, len(ISSI) = 4 is max, so ISSI is longest repeated substring
# To reduce space complexity, store linear list as array. During insertion in trie,
# if char does not exist, take remaining of string and insert as array. If need to break later, break
