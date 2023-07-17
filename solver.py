import random

def load_dictionary(filename, encoding="ISO-8859-13"):
  with open(filename, "r", encoding=encoding) as f:
    words = f.readlines()
  words = [word.strip() for word in words]
  return words

def trie_set(trie, node, distance):
  result = set()
  for i in range(len(trie[node])):
    if distance == 0:
      result.add(i)
    else:
      result.update(trie_set(trie, trie[node][i], distance - 1))
  return result

def traversal(n, is_icoordinate):
  result = []
  for k in range(n * 2):
    for j in range(min(k, n), 0, -1):
      i = k - j
      if i < n and j <= i:
        result.append(is_icoordinate * i + j)
  return result

def word_square(trie, words, n):
  grid = [[list(word) for word in words] for _ in range(n)]
  for step in range(n * (n + 1) // 2):
    i = traversal(n, True)[step]
    j = traversal(n, False)[step]
    options = trie_set(trie, grid[i][j][0], n - step - 1)
    if len(options) == 0:
      return False
    grid[i][j].append(random.choice(options))
  return True

def main():
  trie = load_dictionary("8_length_words.txt")
  words = load_dictionary("8_length_words.txt")
  n = 8
  if not word_square(trie, words, n):
    print("No solution found")
  else:
    print(grid)

if __name__ == "__main__":
  main()