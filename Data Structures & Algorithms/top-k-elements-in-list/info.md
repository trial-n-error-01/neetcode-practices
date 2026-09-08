<https://neetcode.io/problems/top-k-elements-in-list/history?submissionIndex=1>

### Step 3: Gather the top `k` elements

The `freq` array stores numbers according to how often they appear. The index is the frequency:

```python
freq[1] = [1]       # numbers appearing once
freq[2] = [2]       # numbers appearing twice
freq[3] = [3]       # numbers appearing three times
```

For `nums = [1, 2, 2, 3, 3, 3]`, the buckets look like this:

```python
freq = [[], [1], [2], [3], [], [], ...]
```

Step 3 checks the buckets from the highest frequency to the lowest frequency. For `k = 2`, it finds `3` first because it appears three times, then `2` because it appears twice:

```python
res = [3, 2]
```

The order does not matter, so `[3, 2]` is a valid answer.

The original loop uses negative indexes:

```python
counter = 0

while len(res) < k:
 commenest = freq[-1 - counter]
 res += commenest
 counter += 1
```

Here, `freq[-1]` checks the highest-frequency bucket, `freq[-2]` checks the next one, and so on. A clearer version is:

```python
for frequency in range(len(freq) - 1, 0, -1):
 for number in freq[frequency]:
  res.append(number)
  if len(res) == k:
   return res
```
