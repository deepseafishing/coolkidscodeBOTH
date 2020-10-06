from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)

        all_combo_dict = defaultdict(list)
        #  pre-processing O(N*M)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # bfs
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        queue = deque([beginWord])
        distance = 1

        while endWord not in queue:
            temp = deque([])
            for current_word in queue:
                for i in range(len(current_word)):
                    for k in range(ord('a'), ord('z') + 1):
                        word = current_word[:i] + chr(k) + current_word[i+1:]
                        if word in wordList:
                            temp.append(word)
                            idx = wordList.index(word)
                            wordList = wordList[:idx]  + wordList[idx + 1 :]
            distance += 1
            if not temp: return 0
            queue = temp

        return distance
