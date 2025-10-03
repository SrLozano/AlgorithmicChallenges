# 🔐 Encode and Decode Strings

Design an algorithm to **encode** a list of strings into a single string, and then **decode** that string back into the original list of strings.

Your task is to implement two functions:

* `encode(strs: List[str]) -> str`
* `decode(s: str) -> List[str]`

## ✨ Example 1

**Input:**

```
["neet", "code", "love", "you"]
```

**Output:**

```
["neet", "code", "love", "you"]
```

## ✨ Example 2

**Input:**

```
["we", "say", ":", "yes"]
```

**Output:**

```
["we", "say", ":", "yes"]
```

## 📏 Constraints

* `0 <= strs.length < 100`
* `0 <= strs[i].length < 200`
* Each string may contain any UTF-8 characters

## ⚡️ Recommended Complexity

* **Time Complexity:** `O(m)` for each `encode()` and `decode()` call
* **Space Complexity:** `O(m + n)`

  * `m = total number of characters across all strings`
  * `n = number of strings`

## 💡 Hints

1. 🤔 A naive approach might use a special delimiter character — but what if that character appears in the strings themselves?
2. 🧠 Think about encoding lengths: how can you separate string lengths from the string data?
3. 🔑 One good method:

   * Encode each string as **`length#string`**
   * Decode by reading digits until `#` to get the length, then extract the substring of that length.