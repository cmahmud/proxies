# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 411
- HTTP: 273 alive / 83 gold
- HTTPS: 200 alive / 24 gold
- SOCKS4: 214 alive / 150 gold
- SOCKS5: 239 alive / 154 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28921
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
