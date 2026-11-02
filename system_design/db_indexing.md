# Database Indexing

## Key goals
- Understand which of your queries will be inefficient.
- Decide which columns need an index.
- Decide whether you need a specialized index type.

## Decision flowchart
1. Do you need efficient data access?
   - No → full table scan is fine.
   - Yes → go to step 2.
2. Do you have a lot of rows?
   - No → full table scan is fine.
   - Yes → go to step 3.
3. What type of data are you querying?
   - Full-text search → **Inverted index**
   - Location (lat/long) → **Geospatial index**
   - In-memory exact matches → **Hash index**
   - Everything else → **B-Tree**

## The problem indexing solves
Without an index, the database has to do a full table scan: it loads one page from disk into RAM, checks it for the matching rows, and if they aren't there, moves on to the next page. This repeats until every page has been read. For large tables or high-traffic queries, this is far too slow.

## How an index solves it
An index is a separate data structure that acts as a map of where data lives. Instead of reading every page, the database looks up the value in the index, which tells it exactly which page(s) to read.

## Types of indexes

### 1. B-Tree (most popular, the default)
- Each node holds a sorted list of keys, with pointers to child nodes between them. The leaf nodes point to where the actual rows live.
- To find a value, you start at the root and follow the pointer for the range your value falls into, going down one level at a time. Lookup is O(log n).
- Example: `SELECT * FROM users WHERE age = 51` walks down the tree to the key `51` and follows its pointer to the row.
- Because the keys are sorted, B-Trees also handle range queries well (e.g. `WHERE age > 50`).
- In practice, most databases use a **B+ Tree**: all rows (or row pointers) live in the leaves, and the leaves are linked together. A range query finds the start key, then just walks along the leaves.
- **Bad at:** text searches with a leading wildcard (`LIKE '%pizza%'`), 2D queries like "near this lat/long", and low-cardinality columns (e.g. a boolean `is_active`), where the index barely narrows anything down.

### 2. Hash index
- A hash map stored on disk. You hash the key, and the value is the location of the page holding the row.
- Lookups are O(1), but hash indexes are rarely used in production databases. A B-Tree is almost as fast for exact matches and also supports range queries (`WHERE age > 50`) and sorting, which a hash index can't do.
- Hashing is mostly used for in-memory key-value stores and caches (e.g. Redis).
- **Bad at:** range queries (`WHERE age > 50`), sorting (`ORDER BY`), and prefix matches (`LIKE 'piz%'`). Hashing scatters neighboring values randomly, so it only answers "exactly equal."

### 3. Geospatial indexes (for two-dimensional data)
If you're searching by latitude and longitude, a B-Tree isn't a good fit: it's great at sorting along one dimension, but location has two.

#### a. Geohashing (very popular, e.g. Redis)
- Split the world map into 4 boxes labeled `0`, `1`, `2`, `3`. Then split each box into 4 smaller boxes, and append a digit to the label: box `2` becomes `20`, `21`, `22`, `23`. Keep splitting recursively.
- Each extra digit means a smaller box, so a longer label is more precise. At a short length a box might cover a whole region; at a longer length it might cover a single neighborhood.
- This turns a (latitude, longitude) pair into a single one-dimensional string: the **geohash**.
- Nearby places share a common prefix. For example, if Franklin is in box `21`, places near Franklin also start with `21`. To find things nearby, you search for geohashes with the same prefix.
- Since a geohash is just a string, you can put a regular B-Tree index on it and do fast prefix (range) lookups, O(log n).
- Caveat: two points right next to each other across a box border can have very different prefixes, so real implementations also check the neighboring boxes.
- Note: real geohashes use base32 (32 boxes per level, not 4), but the idea is the same.
- **Bad at:** "nearest to me" queries near box borders (you have to search the neighbor boxes too), and uneven data density: a fixed precision gives too many results in a city and too few in a rural area.

#### b. Quadtrees (less common in production databases)
- Also split the map recursively into 4 quadrants, but store the result as a tree: each node has 4 children, one per quadrant.
- You pick a capacity `k`. If a quadrant contains more than `k` points, it gets split into 4 more quadrants. This repeats until every leaf has `k` or fewer points.
- Result: dense areas (cities) get split deeply, sparse areas (oceans) stay as large boxes.
- **Bad at:** frequent writes or moving points (e.g. live driver locations), since points crossing quadrants force constant splits and merges. It's also a poor fit for disk storage: deep trees mean many random reads.

#### c. R-Trees (used in production, e.g. PostGIS)
- Instead of always splitting into 4 fixed quadrants, an R-Tree groups nearby objects into bounding rectangles whose size and shape adapt to the data. These rectangles can overlap.
- Each node is a rectangle that contains its children's rectangles, similar to how B-Tree nodes contain ranges of keys.
- More flexible than a quadtree, but fairly complex to implement.
- **Bad at:** write-heavy workloads, since inserts can trigger costly rectangle splits. Lookups also slow down when rectangles overlap heavily, because a search has to go down several branches at once.

### 4. Inverted index (full-text search, e.g. Elasticsearch, Postgres full-text search)
- B-Trees are bad at queries like `SELECT * FROM business WHERE name LIKE '%pizza%'`. The keys are sorted from the start of the string, so a leading wildcard means the tree can't narrow anything down, and you end up scanning everything.
- An inverted index maps each word to the list of documents that contain it:
  - `"pizza" → [doc1, doc3, doc4]`
- To search, you look up the word and immediately get every document it appears in.
- **Bad at:** numeric and range queries (`WHERE price < 20`), exact structured lookups (`WHERE id = 5`), and matches inside a word (`izz` won't find `pizza` unless you index n-grams). Writes are also expensive, since one document updates many word lists.

## Beyond the basics (what interviewers probe)

### Indexes aren't free
- Every `INSERT`, `UPDATE`, and `DELETE` also has to update every index on the table, so more indexes means slower writes.
- Indexes take extra storage, and ideally should fit in RAM.
- Rule: index the columns used in your most frequent `WHERE`, `JOIN`, and `ORDER BY` clauses, not every column.

### Selectivity (cardinality)
- An index helps most when a value narrows the result to a small fraction of rows.
- `email` has high selectivity, so it's a great index. `is_active` (true/false) has low selectivity, and the database will often ignore the index and do a full scan anyway.

### Composite (multi-column) indexes
- An index on `(last_name, first_name)` is sorted by `last_name` first, then by `first_name` within each last name, like a phone book.
- **Leftmost prefix rule:** it helps `WHERE last_name = ?` and `WHERE last_name = ? AND first_name = ?`, but **not** `WHERE first_name = ?` alone.
- Column order: put equality columns first and range columns last, e.g. `(user_id, created_at)` for `WHERE user_id = 5 AND created_at > '2026-01-01'`.

### Covering indexes
- If the index contains every column the query needs, the database answers straight from the index and never touches the table (an "index-only scan").
- Example: an index on `(user_id, created_at, status)` fully covers `SELECT status FROM orders WHERE user_id = 5 ORDER BY created_at`.

### Clustered vs. non-clustered
- **Clustered:** the table's rows are physically stored in index order. There can only be one per table (e.g. the primary key in MySQL InnoDB). Range scans on it are very fast.
- **Non-clustered (secondary):** a separate structure that points back to the row. A lookup costs an extra hop.

### Write-heavy workloads: LSM trees
- B-Trees update pages in place, which means random disk writes. For write-heavy systems (logs, metrics, messaging), databases like Cassandra and RocksDB use **LSM trees**: writes go to an in-memory buffer, get flushed to sorted files on disk, and are merged in the background.
- Tradeoff: very fast writes, slower reads (you may have to check several files).

### Verify, don't guess
- Use `EXPLAIN` / `EXPLAIN ANALYZE` to see whether a query actually uses your index or falls back to a full scan.

## Interview cheat sheet
| Index | Best for | Bad at |
|---|---|---|
| B-Tree | Exact match, ranges, sorting (the default) | Leading-wildcard text, 2D location, low-cardinality columns |
| Hash | In-memory exact match | Ranges, sorting, prefixes |
| Geohash | Proximity search, simple to build on a B-Tree | Box borders, uneven density |
| Quadtree | In-memory spatial data with uneven density | Frequent updates, disk storage |
| R-Tree | Production spatial queries (PostGIS) | Heavy writes, overlapping rectangles |
| Inverted | Full-text keyword search | Ranges, exact IDs, substrings inside words |
| LSM tree | Write-heavy workloads | Read latency |
