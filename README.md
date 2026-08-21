# SyndProxy private pool

## Current pool

- Alive now: 805
- Gold now: 405
- HTTP: 245 alive / 87 gold
- HTTPS: 136 alive / 21 gold
- SOCKS4: 201 alive / 142 gold
- SOCKS5: 223 alive / 155 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29454
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
