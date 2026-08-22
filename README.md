# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 417
- HTTP: 307 alive / 94 gold
- HTTPS: 224 alive / 29 gold
- SOCKS4: 224 alive / 160 gold
- SOCKS5: 245 alive / 134 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31014
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
