# RevenueCat Interview Prep: 4-Week Daily Plan

About 84 hours total, 5 days a week, roughly 4 to 4.5 hours a day. Write all code yourself and ask the AI only for review afterwards.

## 📊 Progress

| Area | Progress | Done |
| --- | --- | --- |
| 🗓️ **Overall** (days with full hours) | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0 / 20 days |
| 🧩 **Algorithms** (problems solved) | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0 / 20 problems |
| 🐍 **Python** (sessions) | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0 / 11 sessions |
| 🗄️ **SQL** (sessions) | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0 / 8 sessions |
| 📱 **iOS app** (milestones) | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0 / 7 milestones |
| 🏗️ **System design** (sessions) | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ | 0 / 7 sessions |

App milestones: runs on iPhone · enrolled · App Store Connect set up · screen built · paywall working · submitted · live. Each 🟩 is 10%. Updated at each daily check-in.

## Hours by area

| Area | Hours |
| --- | --- |
| Algorithms | 27 |
| Python | 20 |
| App (App Store) | 15 |
| System design | 12 |
| SQL | 10 |

## Requirements

- Mac with Xcode (free) and your iPhone
- Apple Developer Program, $99/year: buy on Day 8, needed for App Store Connect, subscriptions, sandbox testing, TestFlight and submission. Apple's SwiftUI tutorials and docs are free without it.
- Python 3.12+, PostgreSQL, an IDE (VS Code or PyCharm)
- Free accounts: GitHub, LeetCode, Exercism, RevenueCat
- Hello Interview premium (already have)

## Infrastructure

- One repo, `interview-prep`, with folders `python/`, `algorithms/`, `sql/`. The Week 2 API lives in `python/`.
- A separate repo for the iOS app (Xcode project).
- Commit every study day; the GitHub streak doubles as a progress signal.

## Resources

| Area | Resource |
| --- | --- |
| Python | Claude-written exercises tailored to your Kotlin/Rails background; Exercism Python track (free mentor feedback); official Python tutorial as reference |
| Algorithms | NeetCode 150 roadmap (by pattern, with videos) |
| SQL | LeetCode SQL 50, DataLemur; Use The Index, Luke for performance |
| System design | Hello Interview (paste problems or answers to Claude for review; Claude can't log in) |
| App | Apple SwiftUI tutorials; RevenueCat iOS quickstart and paywall docs |

## Daily schedule and weekly rhythm

| Slot | Time | Use it for |
| --- | --- | --- |
| 🙏 Prayer | 5:00–5:30 | Spiritual time, 30 min. If missed, do it at night before bed |
| 🌅 Morning | 5:30–7:30 | 🧩 Algorithms, while fresh and uninterrupted |
| 😴 Nap time | \~30 min, optional | Job applications and replies, or rest |
| 🌙 Evening | \~6:30–9:00 | 🐍 Python, 🗄️ SQL, 📱 app (hands-on work) |
| 🛏️ Bed | by 10:00 | Protect sleep; never stay up late to catch up |

- **Weekdays:** the daily plan, 4–5 hours, coverage or not.
- **Full-coverage weekdays** (change week to week; pick them at the start of each week): up to 5 hours of catch-up and deep work, like mocks and fiddly app problems.
- **Saturday:** backup day for anything that slipped, plus family time.
- **Sunday:** full rest.
- **Bad night?** Move that morning's algorithms to the evening instead of cutting sleep.
- From Week 2, solve at least one problem a day out loud, as if to an interviewer.
- Message your referral contact after Day 5 with progress, and ask about the fourth interview, the allowed languages and the debugging format.
- Treat this as a draft: review it daily and adjust based on real experience.

**Also each week:**

- 🏋️ **Gym, 3× a week (non-negotiable):** on full-coverage days, plus Saturday if needed.
- 💡 **Entrepreneurship, 2–3 h:** one block on Saturday or a full-coverage day.
- **If behind, protect in this order:** sleep → gym → study. Entrepreneurship pauses first.

## 🛑 When I'm stuck or scrolling

**Prevent:** blocker on during study slots, phone in another room. Only face the next checkbox. Being behind is expected; Saturday catches it.

**Urge to scroll?** Stand up, get water, then do one tiny step.

**Already scrolling?** Close it, no judgement. Move your body for 2 minutes. Do one 5-minute task. Lost time goes to Saturday, not to guilt.

**Baby wakes?** Write "next: …" first. Come back, read it, set a 10-min timer, do that one step. Lost time moves to the evening.

**Music:** never open YouTube to get it. Use Spotify or Apple Music, started before the session, and block youtube.com on the laptop during study slots.

## 💪 Minimum day

**The 2-hour morning block = a win, full stop.** The evening is a bonus. Four to five hours stays the target; two hours is the promise.

**Day 1 minimum:** repo created, Python installed, debugger working, and tutorial section 3 read with the examples typed out. Exercises can wait for the evening or Saturday.

> **Key:** 🐍 Python · 🧩 Algorithms · 🗄️ SQL · 📱 iOS app · 🏗️ System design · 🗣️ Behavioural · 🛠️ Setup

## Week 1: Python core, SQL refresher, Apple setup (\~19h)

### Day 1 (4h)

- 🌅 **Morning, 5:30–7:30: setup and first Python**
  - [x] 5:30–5:45 · Create GitHub repo `interview-prep` with folders `python/`, `algorithms/`, `sql/`; clone it
  - [x] 5:45–5:55 · Create LeetCode and Exercism accounts
  - [x] 5:55–6:15 · Install `uv`, then Python 3.12+; create a virtual env in the repo
  - [x] 6:15–6:30 · Open the repo in VS Code or PyCharm; run a one-line script with a breakpoint to confirm the debugger works
  - [ ] 6:30–7:20 · Read the official Python tutorial: [section 3](https://docs.python.org/3/tutorial/introduction.html) and [section 5.1](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists): numbers, strings, slicing, lists. Type every example yourself
  - [ ] 7:20–7:30 · Commit and push
- 😴 **Nap time (optional, 30 min)**
  - [ ] Job applications and replies, or rest
- 🌙 **Evening, 6:30–9:00: exercises**
  - [ ] 6:30–7:00 · Read tutorial [sections 5.3–5.5](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences): tuples, sets, dicts
  - [ ] 7:00–8:30 · Write the 10 exercises below in `python/day01_basics.py`, each with a few `assert` checks. No AI, use the docs only
  - [ ] 8:30–8:50 · Paste your file to Claude for review
  - [ ] 8:50–9:00 · Commit, push, and write tomorrow's first task on a sticky note
- 🐍 **Day 1 exercises**
  - [ ] 1\. `word_count(text)` → dict of word → count, case-insensitive
  - [ ] 2\. `reverse_words(s)` → "hello big world" becomes "world big hello" (split, slicing, join)
  - [ ] 3\. `is_palindrome(s)` → ignore case and non-letters (`isalnum`, `[::-1]`)
  - [ ] 4\. `dedupe(items)` → remove duplicates, keep original order
  - [ ] 5\. `chunk(items, n)` → split a list into lists of size n (slicing, `range` with a step)
  - [ ] 6\. `invert(d)` → swap keys and values; duplicate values map to a list of keys
  - [ ] 7\. `top_k_words(text, k)` → k most common words, ties broken alphabetically (`sorted` with a tuple key)
  - [ ] 8\. `min_max(nums)` → return a tuple, then unpack it: `lo, hi = min_max(...)` (like Kotlin's `Pair` destructuring)
  - [ ] 9\. `common(a, b, c)` → items in all three lists (set intersection)
  - [ ] 10\. Build a 3×3 grid with `[[0] * 3] * 3`, set `grid[0][0] = 1`, print it, explain the bug, then fix it with a comprehension

**Starter file:** copy this into `python/day01_basics.py`, replace each `pass` with your code, and run `python python/day01_basics.py`. When every check passes, it prints "All passed".

```python
# Day 1: Python basics. Replace each `pass` with your code. No AI.

def word_count(text):
    """Return a dict of word -> count, case-insensitive."""
    pass

def reverse_words(s):
    """Reverse the order of words: 'hello big world' -> 'world big hello'."""
    pass

def is_palindrome(s):
    """True if s reads the same backwards, ignoring case and non-letters."""
    pass

def dedupe(items):
    """Remove duplicates, keeping the first occurrence's order."""
    pass

def chunk(items, n):
    """Split a list into lists of size n; the last may be shorter."""
    pass

def invert(d):
    """Swap keys and values; each value maps to a list of its keys."""
    pass

def top_k_words(text, k):
    """The k most common words (lowercase), ties broken alphabetically."""
    pass

def min_max(nums):
    """Return (smallest, largest) as a tuple."""
    pass

def common(a, b, c):
    """Sorted list of items present in all three lists."""
    pass

def make_grid(rows, cols):
    """A rows x cols grid of zeros where each row is independent.
    First try [[0] * cols] * rows, set grid[0][0] = 1, print it, and explain the bug."""
    pass


if __name__ == "__main__":
    assert word_count("The cat the hat") == {"the": 2, "cat": 1, "hat": 1}
    assert word_count("") == {}

    assert reverse_words("hello big world") == "world big hello"
    assert reverse_words("one") == "one"

    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")
    assert is_palindrome("")

    assert dedupe([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert dedupe([]) == []

    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([], 3) == []

    assert invert({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}

    assert top_k_words("b a b c a b", 2) == ["b", "a"]
    assert top_k_words("x y z", 2) == ["x", "y"]

    lo, hi = min_max([4, -2, 9, 0])
    assert (lo, hi) == (-2, 9)

    assert common([1, 2, 3, 4], [2, 4, 6], [4, 2, 8]) == [2, 4]

    grid = make_grid(3, 3)
    grid[0][0] = 1
    assert grid == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

    print("All passed")
```

### Day 2 (4h)

- 🐍 **Python** — functions and iteration (2.5h)
  - [ ] Control flow, functions, \*args/\*\*kwargs, default-argument pitfalls (1.5h)
  - [ ] Comprehensions, generators, enumerate/zip (1h)
- 🗄️ **SQL** — setup and basics (1.5h)
  - [ ] Install PostgreSQL locally and load a sample dataset
  - [ ] Practise SELECT, WHERE, GROUP BY, HAVING

### Day 3 (4h)

- 🐍 **Python** — classes and errors (3h)
  - [ ] Classes, dataclasses, dunder methods vs Kotlin data classes (2h)
  - [ ] Exceptions, context managers, file I/O (1h)
- 🗄️ **SQL** — joins (1h)
  - [ ] Inner, left and self joins
  - [ ] Write 8 queries

### Day 4 (3.5h)

- 🐍 **Python** — testing (2h)
  - [ ] pytest: fixtures, parametrize, test structure
  - [ ] Write tests for Day 1–3 code (1.5h)
  - [ ] Step through a failing test with the debugger (30 min)
- 🗄️ **SQL** — subqueries and CTEs (1.5h)
  - [ ] Work through subquery and CTE problems

### Day 5 (3.5h)

- 🐍 **Python** — mini project (2h)
  - [ ] Build a CLI to-do or expense tracker with classes, file storage and tests
  - [ ] Ask AI to review it
- 🗄️ **SQL** — window functions intro (1h)
  - [ ] ROW\_NUMBER, RANK, SUM OVER
- 📱 **iOS app** — hello world (30 min)
  - [ ] Install Xcode
  - [ ] Create a SwiftUI hello-world
  - [ ] Run it on your iPhone with your free Apple ID

## Week 2: Python in practice, easy algorithms, SQL depth (\~21h)

### Day 6 (4h)

- 🐍 **Python** — FastAPI basics (2h)
  - [ ] Routes, Pydantic models, request validation
- 🧩 **Algorithms** — two pointers (2h)
  - [ ] Learn the two pointers pattern (45 min)
  - [ ] Two Sum II (35 min)
  - [ ] Container With Most Water (40 min)

### Day 7 (4h)

- 🐍 **Python** — CRUD API (2h)
  - [ ] Build a small CRUD API backed by PostgreSQL
- 🗄️ **SQL** — performance (1h)
  - [ ] EXPLAIN / EXPLAIN ANALYZE on your API's queries
  - [ ] Add indexes and compare
- 🧩 **Algorithms** — sliding window (2h)
  - [ ] Learn the sliding window pattern (45 min)
  - [ ] Maximum Sum Subarray of Size K (35 min)
  - [ ] Longest Substring Without Repeating Characters (40 min)

### Day 8 (4.5h)

- 🐍 **Python** — testing the API (2h)
  - [ ] Write pytest tests for the API
  - [ ] Add 3 deliberate bugs, find them with tests and the debugger
- 🗄️ **SQL** — window functions (30 min)
  - [ ] Solve 3 window-function problems
- 📱 **iOS app** — enrol (10 min)
  - [ ] Enrol in the Apple Developer Program, $99/year (approval can take days; needed by Day 11)
- 🧩 **Algorithms** — stack (2h)
  - [ ] Learn the stack pattern (45 min)
  - [ ] Valid Parentheses (35 min)
  - [ ] Daily Temperatures (40 min)

### Day 9 (4h)

- 🐍 **Python** — idioms and pitfalls (1.5h)
  - [ ] Mutability and copying
  - [ ] collections: Counter, defaultdict, deque
  - [ ] heapq
- 🗄️ **SQL** — mixed practice (1h)
  - [ ] Advanced mixed set on LeetCode or DataLemur
- 🧩 **Algorithms** — binary search (2h)
  - [ ] Learn the binary search pattern (45 min)
  - [ ] Koko Eating Bananas (35 min)
  - [ ] Search in Rotated Sorted Array (40 min)

### Day 10 (4.5h)

- 🐍 **Python** — wrap up API (30 min)
  - [ ] Finish the API
  - [ ] Ask AI for a review
- 🗄️ **SQL** — final review (1.5h)
  - [ ] Write queries from scratch, no notes
- 🧩 **Algorithms** — review (1h)
  - [ ] Redo 4 earlier problems from memory, untimed
- 🧩 **Algorithms** — linked list (1.5h)
  - [ ] Learn the linked list pattern (30 min)
  - [ ] Linked List Cycle (30 min)
  - [ ] Remove Nth Node From End (30 min)

## Week 3: Consolidate algorithms, ship the app, start system design (\~22h)

### Day 11 (4.5h)

- 📱 **iOS app** — App Store Connect (1.5h)
  - [ ] Set up App Store Connect
  - [ ] Sign the paid apps agreement, add tax and banking
  - [ ] Create the subscription product
- 🏗️ **System design** — foundations (1h)
  - [ ] Hello Interview framework and core concepts
- 🧩 **Algorithms** — intervals (2h)
  - [ ] Learn the intervals pattern (45 min)
  - [ ] Merge Intervals (35 min)
  - [ ] Insert Interval (40 min)

### Day 12 (4.5h)

- 📱 **iOS app** — build the screen (2.5h)
  - [ ] Build a one-screen SwiftUI app (notes list or counter) (2h)
  - [ ] Note Swift questions for review (30 min)
- 🧩 **Algorithms** — tree DFS (2h)
  - [ ] Learn the tree DFS pattern (45 min)
  - [ ] Maximum Depth of Binary Tree (30 min)
  - [ ] Validate Binary Search Tree (45 min)

### Day 13 (4.5h)

- 📱 **iOS app** — subscriptions (2.5h)
  - [ ] Integrate the RevenueCat SDK
  - [ ] Add the prebuilt paywall
  - [ ] Test a purchase with a sandbox account
- 🧩 **Algorithms** — BFS (2h)
  - [ ] Learn the BFS pattern (45 min)
  - [ ] Binary Tree Level Order Traversal (35 min)
  - [ ] Rotting Oranges (40 min)

### Day 14 (4h)

- 📱 **iOS app** — submit (1.5h)
  - [ ] Lock one feature behind the subscription
  - [ ] Add privacy policy, screenshots, metadata
  - [ ] Submit for review
- 🏗️ **System design** — concepts (30 min)
  - [ ] One Hello Interview core concept
- 🧩 **Algorithms** — graphs (2h)
  - [ ] Learn the graphs pattern (45 min)
  - [ ] Number of Islands (35 min)
  - [ ] Course Schedule (40 min)

### Day 15 (4.5h)

- 🧩 **Algorithms** — timed review (2h)
  - [ ] Redo 5 problems timed, explaining your thinking aloud
- 🏗️ **System design** — walkthrough (2.5h)
  - [ ] Read one guided problem walkthrough, e.g. a URL shortener

## Week 4: Interview mode (\~22h)

### Day 16 (4.5h)

- 🏗️ **System design** — solo attempt (1.5h)
  - [ ] Attempt a problem alone for 45 min
  - [ ] Compare with the solution
- 📱 **iOS app** — review feedback (1h)
  - [ ] Respond to App Review feedback, if any
- 🧩 **Algorithms** — heap (2h)
  - [ ] Learn the heap pattern (45 min)
  - [ ] Kth Largest Element in an Array (35 min)
  - [ ] K Closest Points to Origin (40 min)

### Day 17 (4.5h)

- 🧩 **Algorithms** — weak spots (2h)
  - [ ] Redo 4 problems from your weakest patterns, timed
- 🏗️ **System design** — RevenueCat-style problem (2h)
  - [ ] Design a payments/subscription system
- 📱 **iOS app** — buffer (30 min)
  - [ ] Catch up on anything outstanding

### Day 18 (4.5h)

- 🧩 **Algorithms** — mock interview (2h)
  - [ ] 2 problems, 45 min each, no AI, talking aloud
- 🐍 **Python** — debugging drill (1.5h)
  - [ ] Open an unfamiliar small repo
  - [ ] Reproduce, test and fix a bug
- 📱 **iOS app** — buffer (1h)
  - [ ] Resubmit if rejected

### Day 19 (4.5h)

- 🧩 **Algorithms** — weakest pattern (2h)
  - [ ] Medium problems on your weakest pattern
- 🏗️ **System design** — full mock (2h)
  - [ ] Full run-through on Hello Interview
- 📱 **iOS app** — wrap up (30 min)
  - [ ] Confirm the app is live
  - [ ] Write down the pain points you hit

### Day 20 (4h)

- 🧩 **Algorithms** — final mock (1.5h)
  - [ ] 2 problems, timed
- 🏗️ **System design** — second mock (1.5h)
  - [ ] Another full run-through
- 🗣️ **Behavioural** — stories (1h)
  - [ ] Prepare 5 STAR stories
  - [ ] Prepare your app-shipping story

## Rules

- No AI while solving. Use it for review only.
- Algorithms: stuck after 30 min? Study the answer, then redo it the next day.
- Miss a day? Drop that day's newest material, not the practice or review.
- App rejected? That's part of the lesson. Use the buffer slots.
- Backtracking, greedy and hard problems wait until the interview process.

## Progress tracker

Tick each day when done.

- [ ] Day 1
- [ ] Day 2
- [ ] Day 3
- [ ] Day 4
- [ ] Day 5
- [ ] Day 6
- [ ] Day 7
- [ ] Day 8
- [ ] Day 9
- [ ] Day 10
- [ ] Day 11
- [ ] Day 12
- [ ] Day 13
- [ ] Day 14
- [ ] Day 15
- [ ] Day 16
- [ ] Day 17
- [ ] Day 18
- [ ] Day 19
- [ ] Day 20

## Algorithm log

| Date | Problem | Pattern | Solved without help? | Time (min) |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## ✅ Daily check-in (8:50 pm, 5 min)

Open this project and tell Claude, typed or by voice:

1. **Finished:** which checkboxes I ticked today
2. **Worked:** what went well
3. **Blocker:** what got in the way (sleep, baby, a hard problem, scrolling)
4. **Didn't work:** what I'd change
5. **Skipped:** anything to move to Saturday

Claude then updates the progress bars, adjusts the plan, and confirms tomorrow's first task. Write that task on a sticky note.
