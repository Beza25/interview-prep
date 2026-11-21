# Sharding

## [Flash Card and Questions](https://claude.ai/artifact/FyuZtKEP9UG3r9jDka63cV)


## In the Interview

**You don't always need to shard! Do the math first.**
A single well-tuned database (e.g., Postgres) can handle a few TB of data and thousands of writes/sec. Only shard when the numbers say you've outgrown that.

**Back-of-the-envelope example**
- Users table: 500M users × 2 KB = **1 TB** → fits on one database. No sharding needed.
- Posts table: 500M users × 2 posts/day × 1 KB × 365 days × 5 years ≈ **1.8 PB** → way past one machine. Shard.
- Writes: 1B posts/day ÷ 100K sec/day ≈ **10K writes/sec** average (more at peak) → at or past one primary's limit. Another reason to shard.

Bring up sharding in the deep dive when you're talking about scaling one of these:
1. Storage
2. Write throughput
3. Read throughput (try caching and read replicas first; shard only if those aren't enough)

What to say:
1. Propose a shard key based on your access pattern
2. Choose your distribution strategy
3. Call out the trade-offs
4. Explain how you'll handle growth (adding shards, rebalancing)

## Why Shard?

- We outgrow a single database (storage, writes, or reads).
- Solution: horizontal scaling.
- **Sharding** splits your data and stores it across multiple machines. No single shard has all the data.
- Problems it introduces:
  - What do we shard by?
  - How do we distribute the data across machines?
  - What happens when the load is uneven (hot spots / load imbalance)?
  - How do we maintain consistency across shards?

## How Do You Shard?

### 1. What to shard by (the shard key)

- **Shard key**: the field used to group the data.
- Answers *how we group* the data.

**Good shard key**
- High cardinality (lots of unique values)
- Even distribution (each shard gets roughly the same amount of data and traffic)
- Aligns with queries: the shard key matches how you query the data
- Example: shard key = `user_id`, query = "get all posts for a user" → hits one shard

**Bad shard key**
- Low cardinality, e.g., `is_premium` (only 2 values → at most 2 useful shards)
- Uneven or monotonic, e.g., `created_at` (all new writes land on the "latest" shard → write hot spot)
- Common queries require **scatter-gather** (querying every shard and merging the results)

### 2. How to distribute data

Answers *how we spread the grouped data* across the databases.

**a. Range-based**
- Example: shard 1 = `user_id` 0–10M, shard 2 = `user_id` 10M–20M, ...
- Great: range queries are efficient (scan one shard). Used in real systems (Bigtable, HBase, CockroachDB, MongoDB ranged sharding).
- Problem: uneven distribution. Early on, all users live on shard 1. Later, the newest shard holds the newest (often most active) users and gets most of the traffic.

**b. Hash-based (industry default)**
- `shard = hash(shard_key) % number_of_shards`
- Great: even distribution.
- Trade-off: hard to rebalance, and range queries become scatter-gather.
  - Example: you have `hash(key) % 3` and add a 4th shard. Now it's `hash(key) % 4`, so most keys map to a different shard and must move. That's a lot of data movement and writes.
- **Consistent hashing** solves the rebalancing problem:
  - Hash both the keys and the shards onto a virtual ring (circle).
  - A key belongs to the first shard found walking clockwise from the key's position.
  - Adding or removing a shard only moves the keys between it and its neighbor (~1/N of the data), not everything.
  - Use **virtual nodes** (each physical shard appears at many points on the ring) to keep the distribution even.

**c. Directory-based (rarely the best interview answer)**
- Instead of a formula, use a lookup table that maps each shard key (or key range) to a shard.
- Great: flexibility. If a user becomes super popular, you can move them to their own shard by updating the table.
- Trade-offs:
  - Extra lookup on every request (two hops instead of going straight to the shard). Usually mitigated by caching the directory.
  - The directory is a single point of failure and a bottleneck unless it's replicated.

### 3. Handling growth (resharding without downtime)

When you add shards, data has to move. You can't take the system offline, so:
1. **Double-write**: the app writes to both the old and the new shard for affected keys.
2. **Backfill**: a background job copies existing data from the old shard to the new one.
3. **Verify**: compare the old and new shards (counts, checksums) until they match.
4. **Cut over reads** to the new shard, gradually (e.g., 1% → 10% → 100%), watching for errors.
5. **Stop double-writing** and delete the moved data from the old shard.

Tips:
- **Over-provision logical shards**: start with many logical shards (e.g., 1,024) mapped onto a few physical machines. Growing means moving whole logical shards to new machines, never re-hashing keys.
- Consistent hashing keeps the amount of data that moves small (~1/N).

## Challenges of Sharding

### 1. Hot spots (load imbalance)

- **Celebrity problem**: e.g., Taylor Swift's data/traffic overwhelms a single shard.
- Solutions:
  1. **Compound shard key**, e.g., `hash(user_id + created_at)`, spreads one user's data across shards.
     Trade-off: reading all of that user's data now requires scatter-gather.
  2. **Key salting**: append a random suffix (0–N) to hot keys only, so writes spread over N shards.
  3. **Dedicated shard** for celebrity / hot keys.
  4. For read-heavy hot spots: **cache** and add **read replicas**.

### 2. Cross-shard queries

- You need data from multiple shards. Usually happens when the shard key doesn't align with the query.
- You can't eliminate this entirely; you minimize it.
- Solutions:
  1. **Cache** the result of the expensive query. The first query is slow, later ones are fast.
  2. **Denormalize** the data: duplicate it so each query hits one shard. Reads get fast at the cost of more storage and more writes (and keeping copies in sync).

### 3. Maintaining consistency

- You lose **atomic transactions** across shards.
- Example: Bob sends $5 to Alice. Since we shard by `user_id`, Bob and Alice may live on different shards. On a single database this is one atomic transaction; across shards, if one side fails, rolling back is much harder.

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 5
WHERE name = 'Bob';

UPDATE accounts
SET balance = balance + 5
WHERE name = 'Alice';

COMMIT;
```

- Solutions:
  1. **Avoid it in the first place**: choose a shard key so data that changes together lives on the same shard.
  2. **Two-Phase Commit (2PC)**: a central coordinator asks every shard "are you ready to commit?" (prepare phase). If all say yes, it tells them to commit (commit phase); otherwise, everyone aborts.
     Works in theory, but in practice it's slow (extra round trips, locks held the whole time) and fragile: if the coordinator crashes after "prepare," the shards are stuck holding locks until it recovers (it's a *blocking* protocol). Most production systems avoid it.
  3. **Saga pattern**: a sequence of small local transactions, each with a **compensating action** that undoes it.
     - Step 1: deduct $5 from Bob
     - Step 2: add $5 to Alice
     - If step 2 fails → refund $5 to Bob (the compensating action)
     - Trade-off: no isolation. Other requests can see the in-between state (Bob debited, Alice not yet credited). The system is *eventually* consistent.

## End-to-End Example: Twitter-Style Feed

**1. Do the math**
- 500M users, 200M daily active, 500M tweets/day × 1 KB ≈ **0.5 TB/day** → ~1 PB over 5 years. One database can't hold it.
- Writes: 500M ÷ 100K sec ≈ **5K tweets/sec** (≈15K at peak).
- Reads: 200M users × 20 timeline loads/day ≈ **40K reads/sec**. Very read-heavy.
- Verdict: the **tweets** table must be sharded. The **users** table (~1 TB) can stay on one primary with read replicas.

**2. Shard key**
- Tweets: shard by `author_id`. Query "get a user's tweets" hits one shard.
- Tweet IDs are time-sortable (Snowflake-style: timestamp + machine ID + sequence), so a user's tweets are already in time order within their shard.
- Follows: shard by `follower_id` ("who do I follow?" hits one shard).

**3. Distribution**
- Hash-based with consistent hashing over **1,024 logical shards** mapped onto ~20 physical machines.
- Range on `created_at` is rejected: every new tweet would hit the newest shard.

**4. Cross-shard problem: the home timeline**
- "Show me tweets from everyone I follow" spans many shards → scatter-gather on every load is too slow at 40K reads/sec.
- Fix: **denormalize with fan-out on write**. When a user tweets, push the tweet ID into each follower's precomputed timeline (a cache like Redis, sharded by `follower_id`). Loading a timeline = one read from one shard.
- Cost: more writes and storage. Accepted, because reads far outnumber writes.

**5. Hot spots: celebrities**
- A user with 100M followers would trigger 100M timeline writes per tweet.
- Fix: **hybrid fan-out**. Normal users → fan-out on write. Celebrities (e.g., > 1M followers) → fan-out on read: their tweets are fetched at read time and merged into the timeline.
- Celebrity tweets get heavy read traffic → **cache** them and serve from **read replicas**.
- Like counts on viral tweets are hot keys → **salt** the counter (`tweet_id:0` … `tweet_id:15`) and sum them on read.

**6. Consistency**
- Following someone writes to two places: the follows table (by `follower_id`) and the follower list (by `followee_id`), possibly on different shards.
- No 2PC. Use a **saga / async event**: write the follow, publish an event, a worker updates the follower list. If it fails, retry (or compensate by removing the follow).
- Eventual consistency is fine here: a follower count that lags a few seconds is acceptable. (Payments would not be.)

**7. Growth**
- Add physical machines and move whole logical shards to them using **double-write → backfill → verify → cut over**. No key re-hashing, no downtime.
