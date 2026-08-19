# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 552
- HTTP: 399 alive / 187 gold
- HTTPS: 281 alive / 99 gold
- SOCKS4: 186 alive / 120 gold
- SOCKS5: 222 alive / 146 gold

## Historical pool

- Discovered: 124835
- Ever alive: 19229
- Ever gold: 770

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
