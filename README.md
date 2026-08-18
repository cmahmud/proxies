# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 281
- HTTP: 345 alive / 28 gold
- HTTPS: 155 alive / 5 gold
- SOCKS4: 226 alive / 135 gold
- SOCKS5: 216 alive / 113 gold

## Historical pool

- Discovered: 100083
- Ever alive: 12547
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
