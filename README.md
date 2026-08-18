# SyndProxy private pool

## Current pool

- Alive now: 1110
- Gold now: 282
- HTTP: 448 alive / 29 gold
- HTTPS: 234 alive / 7 gold
- SOCKS4: 208 alive / 126 gold
- SOCKS5: 220 alive / 120 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13094
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
