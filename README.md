# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 405
- HTTP: 356 alive / 96 gold
- HTTPS: 228 alive / 23 gold
- SOCKS4: 203 alive / 135 gold
- SOCKS5: 277 alive / 151 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27914
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
