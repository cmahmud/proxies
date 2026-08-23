# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 363
- HTTP: 88 alive / 42 gold
- HTTPS: 39 alive / 9 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 177 alive / 156 gold

## Historical pool

- Discovered: 173622
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
