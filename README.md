# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 388
- HTTP: 270 alive / 91 gold
- HTTPS: 224 alive / 23 gold
- SOCKS4: 198 alive / 134 gold
- SOCKS5: 202 alive / 140 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27886
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
