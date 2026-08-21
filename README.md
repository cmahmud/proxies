# SyndProxy private pool

## Current pool

- Alive now: 1127
- Gold now: 417
- HTTP: 392 alive / 114 gold
- HTTPS: 273 alive / 28 gold
- SOCKS4: 249 alive / 151 gold
- SOCKS5: 213 alive / 124 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30581
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
