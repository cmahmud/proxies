# SyndProxy private pool

## Current pool

- Alive now: 578
- Gold now: 228
- HTTP: 179 alive / 37 gold
- HTTPS: 89 alive / 10 gold
- SOCKS4: 153 alive / 103 gold
- SOCKS5: 157 alive / 78 gold

## Historical pool

- Discovered: 86653
- Ever alive: 5728
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
