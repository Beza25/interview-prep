# Data Modeling

** [Flash Cards and Questions](https://claude.ai/artifact/DCLyrXu3tuQQHBEKeJ5EJm)
  **


A **data model** defines how your data is:
- **Structured**: entities, fields, types
- **Stored**: which database, what layout
- **Related**: how entities reference each other

## Interview Flow

1. **Choose a DB type.** This decides how data is stored and queried.
2. **Outline entities and columns.**
3. **Add primary and foreign keys.**
4. **Decide which indexes you need**, based on your access patterns.
5. **Decide whether to denormalize**, for read performance.
6. **Decide whether you need sharding.** If you do, choose a partition (shard) key.

## Three Key Factors That Drive Schema Design

| Factor | Question | Drives |
|---|---|---|
| **Data volume** | How much data? Can it fit on one machine? | Single DB vs. distributed/sharded |
| **Access patterns** | How is the data read and written? | Indexes, keys, table structure |
| **Consistency requirements** | How strict must correctness be? | ACID transactions vs. eventual consistency |

---

## Database Types

Running example: an **Instagram-style app** with three entities: `User`, `Post`, `Like`.

### 1. Relational DB (PostgreSQL, MySQL): the default choice

- Data lives in tables with a fixed schema.
- Foreign keys and constraints **prevent orphaned or invalid data**.
- Joins make complex relationships and queries straightforward.
- ACID transactions give strong consistency.

```
users (id PK, username, email, created_at)
posts (id PK, user_id FK -> users.id, content, created_at)
likes (user_id FK -> users.id, post_id FK -> posts.id, created_at)
       PRIMARY KEY (user_id, post_id)   -- a user can like a post only once
```

**Use when:** you're unsure which to pick. It's the safe default in interviews.

### 2. Document DB (MongoDB, Firestore)

- Stores JSON-like documents with a **flexible schema**. Documents in the same collection can have different fields.
- Encourages **embedding** related data in one document (denormalization), so you can read it all at once without joins.
- You can still keep separate collections (`users`, `posts`, `likes`) and reference them by ID. Joins are weaker than in SQL, though.

```json
{
  "_id": "35353322lkjl22j",
  "username": "john",
  "posts": [
    { "content": "Hello", "created_at": "2024-01-01T10:00:00Z" }
  ],
  "created_at": "2024-01-01T10:00:00Z"
}
```

> ⚠️ Embedding unbounded lists (like every post a user has ever made) is an anti-pattern because documents have size limits (16MB in MongoDB). Put posts in their own collection.

**Use when:** the schema is evolving or unknown, records vary in shape, or data is usually read as one whole unit.

### 3. Key-Value Store (Redis, DynamoDB)

- Works like a giant distributed hash map: `key -> value`.
- **Extremely fast** lookups by exact key.
- No range queries or ad-hoc queries in a pure KV store. You can only fetch by the exact key.
- Leads to **heavy denormalization**: you precompute the values you'll need and duplicate data across keys.
  - Example: to load recent posts, store `recent_posts -> [post1, post2, ...]` and update it on every new post. The post data is now duplicated.
- Very common as a **cache for hot data** in front of the main DB (Redis).
- **DynamoDB** is a hybrid of key-value and document. Values are document-like items, and with a **partition key + sort key** it *does* support range queries within a partition (e.g. all posts for `user_id` sorted by `created_at`).

**Use when:** caching, sessions, rate limiting, leaderboards, or simple lookups at massive scale.

### 4. Wide-Column DB (Cassandra, HBase, ScyllaDB)

- Rows are grouped by a **partition key**. Each row can have a different set of columns.
- Built for **massive write throughput**. Writes are append-only (LSM tree), so they're cheap.
- Data inside a partition is **sorted by a clustering key**, which makes "latest N events for X" queries fast.
- You design tables around specific queries. There are no joins, and ad-hoc queries are poor.

**Use when:** you have high-volume, fast-arriving writes that are read by key, such as time-series data, event logging, IoT/sensor data, analytics logs, or chat messages.

### 5. Graph DB (Neo4j)

- Stores data as **nodes** (entities) and **edges** (relationships).
- Good for deep relationship traversal (friends-of-friends, recommendations, fraud rings).
- **Rarely the right choice in interviews.** Even Facebook models its social graph on top of MySQL. Pick a relational DB unless traversal is the core problem.

---

## Keys and Constraints

- **Primary key (PK):** uniquely identifies each row and can't be null. Example: `users.id`.
- **Composite key:** a PK made of several columns. Example: `likes(user_id, post_id)`.
- **Foreign key (FK):** a column that references another table's PK and enforces that the referenced row exists. Example: `posts.user_id -> users.id`.
- **Constraints** enforce data rules at the DB level:
  - `UNIQUE`: e.g. `users.email` (no two accounts can share an email)
  - `NOT NULL`: e.g. `posts.user_id`
  - `CHECK`: e.g. `age >= 13`

## Indexes

- An index is a separate data structure (usually a B-tree) that speeds up lookups on a column, at the cost of **slower writes and extra storage**.
- Add indexes on the columns you **filter, join, or sort on**, based on your access patterns.
  - Example: "get a user's posts, newest first" → composite index on `posts(user_id, created_at DESC)`.
- PKs and UNIQUE columns are indexed automatically.

---

## Normalization vs. Denormalization

### Normalization
- Store each piece of information in **exactly one place**. For example, user data lives only in `users` and isn't copied into `posts`.
- Prevents **update anomalies**, where copies get out of sync.
- ✅ Consistent, with no duplicate data.
- ❌ Reads need **joins**, which can get slow at scale.

### Denormalization
- **Intentionally duplicate data** to make reads faster.
  - Example: store `like_count` on `posts` instead of running `COUNT(*)` over `likes` on every read.
  - Example: store `username` on each post so the feed doesn't need a join.
- ✅ Fast reads.
- ❌ Writes are more complex, and duplicates can drift out of sync.

**Interview tip:** start normalized, then denormalize the hot read paths and explain the trade-off. Often the denormalized view lives in a **cache** (Redis) or a precomputed table, and you accept **eventual consistency** for it.

---

## Scaling and Sharding

- **Sharding** splits data across multiple DB machines when it's too large, or the traffic too high, for one DB.
- Before sharding, consider simpler steps: vertical scaling, read replicas, and caching.
- **Choosing a shard (partition) key:**
  - Keep data that is queried together on the **same shard** to avoid cross-shard queries.
  - Spread load evenly to avoid **hot spots**.
  - Example: shard `posts` by `user_id`, so all of a user's posts sit on one shard and "get user's posts" hits a single shard.
  - Bad key: `created_at`. All new writes land on the same shard and make it a hot spot.
- **Common strategies:**
  - **Hash-based:** `hash(key) % N`. Distributes evenly, but range queries become hard. Use **consistent hashing** to limit how much data moves when you add or remove shards.
  - **Range-based:** e.g. user IDs 1–1M go to shard 1. Range queries are easy, but this is prone to hot spots.
- **Trade-offs:** cross-shard joins and transactions become hard, and rebalancing is painful.
