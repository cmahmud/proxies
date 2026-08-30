# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 429
- HTTP: 115 alive / 81 gold
- HTTPS: 64 alive / 22 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44312
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
