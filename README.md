# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 534
- HTTP: 355 alive / 157 gold
- HTTPS: 266 alive / 87 gold
- SOCKS4: 231 alive / 149 gold
- SOCKS5: 220 alive / 141 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18072
- Ever gold: 714

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
