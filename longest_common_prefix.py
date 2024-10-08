def longestCommonPrefix(strs):
    if not strs:
        return ""  # If the input list is empty, return an empty string

    prefix = strs[0]  # Assume the first string is the prefix

    # Compare the prefix with each string in the list
    for i in range(1, len(strs)):
        j = 0
        # Find the length of the common prefix with the current string
        while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
            j += 1
        # Update the prefix to the portion that matched
        prefix = prefix[:j]
        
        # If the prefix is empty, no need to check further
        if prefix == "":
            return ""
    
    return prefix